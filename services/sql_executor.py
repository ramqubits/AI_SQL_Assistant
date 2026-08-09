import sqlite3
import pandas as pd

def execute(sql):

    conn = sqlite3.connect("database/sales.db")

    df = pd.read_sql_query(sql, conn)

    conn.close()

    return df