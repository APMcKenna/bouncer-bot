import os

SQL_DB_HOST = os.getenv("SQL_DB_HOST", "127.0.0.1")
SQL_DB_PORT = os.getenv("SQL_DB_PORT", "3306")
SQL_DB_USER = os.getenv("SQL_DB_USER", "bouncer_bot")
SQL_DB_PASSWORD = os.getenv("SQL_DB_PASS", "password")
SQL_DB_NAME = os.getenv("SQL_DB_NAME", "message_audit")
