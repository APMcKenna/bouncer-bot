from mysql.connector import cursor

from .connection import open_database_connection, close_database_connection


def execute_sql_select(statement, cur):
    """ Executes a single sql select """
    if not statement['args']:
        cur.execute(statement['statement'])
    else:
        cur.execute(statement['statement'], statement['args'])

    return cur.fetchall()


def execute_sql_selects(statements):
    """ Executes a list of sql selects """
    results = []

    con = open_database_connection()
    cur = con.cursor()

    for statement in statements:
        results.append(execute_sql_select(statement, cur))

    close_database_connection(con)

    return results


def execute_sql_insert(statement, cur):
    """ Executes a single sql insert """
    if not statement['args']:
        cur.execute(statement['statement'])
    else:
        cur.execute(statement['statement'], statement['args'])


def execute_sql_inserts(statements):
    """ Executes a list of sql inserts """
    results = []

    con = open_database_connection()
    cur = con.cursor()

    for statement in statements:
        results.append(execute_sql_insert(statement, cur))

    close_database_connection(con)
