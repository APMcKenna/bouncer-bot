import datetime
import emoji
import discord

from datetime import datetime, timedelta
from src.cfg.environment import STRIKE_DURATION, MAX_STRIKE_COUNT, AUDIT_TABLE_NAME, LOGGING_CHANNEL, KICK_USERS, AUDIT_CHANNEL
from src.database.execute import execute_sql_selects, execute_sql_inserts

logging_channel = None
audit_channel = None


async def discipline_member(message):
    """
    Discipline the member for breaking the rules.

    :param message:
    :return:
    """
    global logging_channel
    logging_channel = discord.utils.find(lambda tc: tc.name == LOGGING_CHANNEL, message.guild.channels)

    global audit_channel
    audit_channel = discord.utils.find(lambda tc: tc.name == AUDIT_CHANNEL, message.guild.channels)

    log_message(message)
    await delete_message(message)
    strike_count = get_strike_count(message)

    if strike_count >= MAX_STRIKE_COUNT and KICK_USERS is True:
        await kick_member(message, strike_count)
        pass
    else:
        await warn_member(message, strike_count, False)
    pass


async def kick_member(message, strike_count):
    """
    Kicks a member for receiving too many strikes.

    :param message:
    :param strike_count:
    :return:
    """
    await warn_member(message, strike_count, True)
    member = message.author

    global logging_channel
    try:
        await member.kick(reason=f"Messaging in restricted channels")
    except discord.Forbidden:
        logging_channel.send(f"Bot does not have permission to kick member: {member.id}.")
    except discord.HTTPException as e:
        logging_channel.send(f"Bot failed to kick member due to unknown HTTPException: {e}")

    await audit_kick_case(member, strike_count)


async def audit_kick_case(member, strike_count):
    """
    Audits the case of kicking the member for the managers.

    :param member:
    :param strike_count:
    :return:
    """
    sql_statement = {
        'statement': f'SELECT * FROM {AUDIT_TABLE_NAME} WHERE UserID="{member.id}"',
        'args': None
    }

    results = execute_sql_selects([sql_statement])[0]

    embed = discord.Embed(
        title='Kick audit',
        description=f'member has been kicked',
        colour=discord.Colour.blue()
    )

    embed.add_field(name="User name", value=member.name, inline=True)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Current strike count", value=strike_count, inline=True)

    i = 0
    for result in results:
        embed.add_field(name=f"Message #{i}", value=emoji.emojize(result[2]), inline=False)
        i += 1

    await send_to_audit_channel(embed)


async def send_to_audit_channel(embed):
    """
    Sends the audit embed to the audit channel.

    :param embed:
    :return:
    """
    global audit_channel
    global logging_channel

    try:
        await audit_channel.send(embed=embed)
    except discord.Forbidden:
        await logging_channel.send(f"Bot does not have proper permissions to send messages in {audit_channel.name}.")
    except discord.HTTPException as e:
        await logging_channel.send(f"Bot failed to send message to {audit_channel.name} due to unknown HTTPException: {e}.")


async def warn_member(message, strike_count, member_to_be_kicked):
    """
    Warn a member for messaging in a restricted channel.

    :param strike_count:
    :param message:
    :param member_to_be_kicked:
    :return:
    """
    member = message.author
    embed = discord.Embed(
        title='Warning',
        description='Message in restricted channel'
    )

    embed.add_field(name="Text channel", value=message.channel.name, inline=False)
    embed.add_field(name="Message content", value=message.clean_content, inline=False)
    embed.add_field(name="Your current strike count", value=f"{strike_count}/{MAX_STRIKE_COUNT}", inline=False)
    if member_to_be_kicked:
        embed.add_field(name="Max strike count exceeded", value="Due to this you have been kicked from the server")
        embed.colour = discord.Colour.red()
    else:
        embed.colour = discord.Colour.orange()

    await message_member(member, embed)


async def message_member(member, embed):
    """
    Send a direct message to a member.

    :param member:
    :param embed:
    :return:
    """
    global logging_channel
    try:
        await member.send(embed=embed)
    except discord.Forbidden:
        await logging_channel.send(f"Bot does not have proper permissions to send Direct messages. Failed to send to {member.id}.")
    except discord.HTTPException as e:
        await logging_channel.send(f"Bot failed to send message to {member.id} due to unknown HTTPException: {e}.")


def get_strike_count(message):
    """
    Get the number of strikes that the member is currently on from the database.

    :param message:
    :return:
    """
    member_id = message.author.id
    current_time = datetime.now()
    oldest_allowed_time = current_time - timedelta(days=STRIKE_DURATION)

    sql_statement = {
        'statement': f'SELECT COUNT(*) FROM {AUDIT_TABLE_NAME} WHERE UserID="{member_id}" AND Message_time BETWEEN "{oldest_allowed_time}" AND "{current_time}"',
        'args': None
    }

    strike_count = execute_sql_selects([sql_statement])[0][0][0]

    return strike_count


def log_message(message):
    """
    Log the message in the database for evidence.

    :param message:
    :return:
    """
    user_id = message.author.id
    message_time = message.created_at
    message_content = emoji.demojize(message.clean_content)

    sql_statement = {
        'statement': f'INSERT INTO {AUDIT_TABLE_NAME} (UserID, Message_time, Message_content) '
                     f'VALUES ("{user_id}", "{message_time}", "{message_content}")',
        'args': None
    }

    execute_sql_inserts([sql_statement])


async def delete_message(message):
    """
    Deletes the message that raised the bot event.

    :param message:
    :return:
    """
    global logging_channel

    try:
        await message.delete()
    except discord.Forbidden:
        await logging_channel.send(f"Bot does not have permission to delete message in {message.channel.name}.")
    except discord.NotFound:
        await logging_channel.send(f"The message in {message.channel.name} was deleted already.")
    except discord.HTTPException as e:
        await logging_channel.send(f"Bot could not delete message in {message.channel.name} due to unknown HTTPException: {e}.")
