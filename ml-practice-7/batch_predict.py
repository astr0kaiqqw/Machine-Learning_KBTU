import sqlite3
import pandas as pd
import joblib

conn = sqlite3.connect("ml_database.db")

input_data = pd.read_sql_query("""
SELECT id, sepal_length, sepal_width, petal_length, petal_width
FROM input_data
""", conn)

if input_data.empty:
    print("No input data found.")
    conn.close()
    exit()

saved_model = joblib.load("model.joblib")
model = saved_model["model"]
target_names = saved_model["target_names"]

features = input_data[[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]]

predictions = model.predict(features)

cursor = conn.cursor()

for input_id, prediction in zip(input_data["id"], predictions):
    prediction_name = target_names[prediction]

    cursor.execute("""
    INSERT INTO predictions (input_id, prediction)
    VALUES (?, ?)
    """, (int(input_id), str(prediction_name)))

conn.commit()
conn.close()

print("Batch prediction completed successfully.")