from discord.ext import commands
from src.ping.validate import validate_ping
from src.stop.validate import validate_stop


@commands.command(name='ping')
async def ping(ctx):
    """
    Allows pinging the bot to check that it is running.

    :param ctx:
    :return:
    """
    if validate_ping(ctx):
        await ctx.send(f'Pong')


@commands.command(name='stop')
async def stop(ctx):
    """
    !!!For Testing!!!
    Allows the bot to be stopped with a command.

    :param ctx:
    :return:
    """
    if validate_stop(ctx):
        await ctx.send(f'{ctx.bot.user.name} clocking off!')
        await ctx.bot.close()


bot_commands = [ping, stop]
