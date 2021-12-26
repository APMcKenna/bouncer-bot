from discord.ext import commands
from src.cfg.environment import BOT_TOKEN, COMMAND_SYMBOL
from src.ping.validate import validate_ping
from src.stop.validate import validate_stop

bot = commands.Bot(command_prefix=COMMAND_SYMBOL)


@bot.event
async def on_ready():
    """
    Runs when the bot is setup and ready to catch events.
    """
    guild = bot.guilds[0]
    print(f"Running on: {bot.user.name}. With the ID: {str(bot.user.id)}. On the guild: {guild.name}.")
    print("Bot is ready to be run...")


@bot.command(name='ping')
async def ping(ctx):
    """
    Allows pinging the bot to check that it is running.

    :param ctx:
    :return:
    """
    if validate_ping(ctx):
        await ctx.send(f'Pong')


@bot.command(name='stop')
async def stop(ctx):
    """
    !!!For Testing!!!
    Allows the bot to be stopped with a command.

    :param ctx:
    :return:
    """
    if validate_stop(ctx):
        await ctx.send(f'{bot.user.name} clocking off!')
        await ctx.bot.close()


bot.run(BOT_TOKEN)
