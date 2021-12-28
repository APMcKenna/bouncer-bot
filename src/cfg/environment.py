import os

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
COMMAND_SYMBOL = os.getenv("DISCORD_COMMAND_SYMBOL", "!")

RESTRICTED_CHANNELS = os.getenv("DISCORD_RESTRICTED_CHANNELS", '["notice-board", "welcome-mat", "bot-logs"]')

MAX_STRIKE_COUNT = os.getenv("DISCORD_MAX_STRIKE_COUNT", 3)
STRIKE_DURATION = os.getenv("DISCORD_STRIKE_DURATION", 7)

AUDIT_TABLE_NAME = os.getenv("DISCORD_AUDIT_TABLE_NAME", "message_log")
AUDIT_CHANNEL = os.getenv("DISCORD_AUDIT_CHANNEL_NAME", "managers-log")
LOGGING_CHANNEL = os.getenv("DISCORD_LOGGING_CHANNEL_NAME", "bot-logs")

# Only set to true for testing, set default to false normally
KICK_USERS = (os.getenv("DISCORD_KICK_USERS", False).lower() == 'true')
