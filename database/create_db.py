import sqlite3

conn = sqlite3.connect("database/sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_transactions(
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    transaction_date TEXT,
    total_amount REAL,
    region TEXT
)
""")

sample_data = [
    (1,101,"2025-01-10",1200,"South"),
    (2,102,"2025-01-15",2200,"North"),
    (3,101,"2025-02-18",1800,"South"),
    (4,103,"2025-03-20",2500,"East"),
    (5,104,"2025-03-25",3000,"West"),
]

cursor.executemany(
    "INSERT INTO sales_transactions VALUES (?,?,?,?,?)",
    sample_data
)

conn.commit()
conn.close()

print("Database created successfully.")