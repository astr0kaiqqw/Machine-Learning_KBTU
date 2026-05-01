import sqlite3

conn = sqlite3.connect("ml_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS input_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepal_length REAL,
    sepal_width REAL,
    petal_length REAL,
    petal_width REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_id INTEGER,
    prediction TEXT,
    prediction_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("DELETE FROM input_data")
cursor.execute("DELETE FROM predictions")

sample_data = [
    (5.1, 3.5, 1.4, 0.2),
    (6.2, 3.4, 5.4, 2.3),
    (5.9, 3.0, 4.2, 1.5),
    (4.9, 3.0, 1.4, 0.2),
    (6.7, 3.1, 4.7, 1.5)
]

cursor.executemany("""
INSERT INTO input_data 
(sepal_length, sepal_width, petal_length, petal_width)
VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("Database created and sample data inserted.")