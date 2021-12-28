import json

from discord import DMChannel
from discord.ext import commands
from src.cfg.environment import BOT_TOKEN, COMMAND_SYMBOL, RESTRICTED_CHANNELS
from src.commands import bot_commands
from src.member.discipline import discipline_member

bot = commands.Bot(command_prefix=COMMAND_SYMBOL)


@bot.event
async def on_ready():
    """
    Runs when the bot is setup and ready to catch events.
    """
    guild = bot.guilds[0]
    print(f"Running on: {bot.user.name}. With the ID: {str(bot.user.id)}. On the guild: {guild.name}.")
    print("Bot is ready to be run...")


@bot.event
async def on_message(message):
    """
    Runs when a message is sent in a server the bot is in.
    """
    if not isinstance(message.channel, DMChannel):
        restricted_channels = json.loads(RESTRICTED_CHANNELS)

        if (message.channel.name in restricted_channels) and \
                (not message.author.bot) and \
                (not message.author.top_role.name == "Landlord"):
            await discipline_member(message)

        await bot.process_commands(message)

for command in bot_commands:
    bot.add_command(command)

bot.run(BOT_TOKEN)
