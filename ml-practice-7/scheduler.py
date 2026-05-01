import schedule
import time
import subprocess

def run_batch_prediction():
    print("Running batch prediction...")
    subprocess.run(["python", "batch_predict.py"])

schedule.every(5).minutes.do(run_batch_prediction)

print("Scheduler started. Batch prediction will run every 5 minutes.")

run_batch_prediction()

while True:
    schedule.run_pending()
    time.sleep(1)