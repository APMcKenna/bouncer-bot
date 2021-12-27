from discord.ext import commands
from src.cfg.environment import BOT_TOKEN, COMMAND_SYMBOL
from src.commands import bot_commands

bot = commands.Bot(command_prefix=COMMAND_SYMBOL)


@bot.event
async def on_ready():
    """
    Runs when the bot is setup and ready to catch events.
    """
    guild = bot.guilds[0]
    print(f"Running on: {bot.user.name}. With the ID: {str(bot.user.id)}. On the guild: {guild.name}.")
    print("Bot is ready to be run...")

for command in bot_commands:
    bot.add_command(command)

bot.run(BOT_TOKEN)
