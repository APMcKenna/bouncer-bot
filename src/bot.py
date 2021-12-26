from discord import Client, Intents
from src.cfg.environment import BOT_TOKEN

intents = Intents.default()
intents.members = True

bot = Client(intents=intents)


@bot.event
async def on_ready():
    guild = bot.guilds[0]
    print(f"Running on: {bot.user.name}. With the ID: {str(bot.user.id)}. On the guild: {guild.name}.")
    print("Bot is ready to be run...")


bot.run(BOT_TOKEN)
