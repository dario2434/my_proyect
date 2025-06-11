import random
import sqlite3

DB_PATH = ':memory:'


def decision(other_decision: bool) -> bool:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    con.row_factory = sqlite3.Row
    cur.execute("""
    CREATE TABLE decisions(
        round INTEGER PRIMARY KEY AUTOINCREMENT,
        my_decision BOOLEAN,
        other_decision BOOLEAN,
        my_points INTEGER,
        other_points INTEGER
    )""")
    decision = my_decision(other_decision)
    sql = """
    INSERT INTO decisions (my_decision,other_decision,my_points,other_points)
    """
    cur.execute(
        sql,
        (
            decision,
            other_decision,
            get_points(decision, other_decision)[0],
            get_points(decision, other_decision)[1],
        ),
    )
    con.commit()
    return decision


def get_points(my_decision, other_decision):
    if not my_decision and not other_decision:
        return 1, 1
    elif my_decision and not other_decision:
        return 7, 0
    elif not my_decision and other_decision:
        return 0, 7
    elif my_decision and other_decision:
        return 3, 3


def my_decision(other_decision):
    if other_decision:
        return random.random() >= 0.1
    return False
