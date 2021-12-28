from mysql import connector
from .environment import SQL_DB_HOST, SQL_DB_PORT, SQL_DB_USER, SQL_DB_PASSWORD, SQL_DB_NAME


def fetch_database_parameters():
    """ Creates the parameters required to connect to a SQL database"""
    return {
        'host': SQL_DB_HOST,
        'port': SQL_DB_PORT,
        'user': SQL_DB_USER,
        'password': SQL_DB_PASSWORD,
        'database': SQL_DB_NAME
    }


def open_database_connection():
    """ Creates an open connection to the database """
    db_params = fetch_database_parameters()

    con = connector.connect(**db_params)

    return con


def close_database_connection(con):
    """ Close a connection to the database """
    con.commit()
    con.close()
