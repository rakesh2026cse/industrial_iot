import random
import time
from datetime import datetime
import sqlite3
from config import *
from utils.db_utils import insert_sensor_data
from ml.anomaly_detector import detect_anomaly

def read_sensors():
    temperature = random.uniform(50, 90)
    vibration = random.uniform(1, 8)
    pressure = random.uniform(100, 170)
    return temperature, vibration, pressure

def run():
    while True:
        temp, vib, pres = read_sensors()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_sensor_data(temp, vib, pres, timestamp)

        is_anomaly = detect_anomaly([temp, vib, pres])
        if is_anomaly:
            print(f"[ALERT ] Anomaly detected at {timestamp} — Temp: {temp:.2f}, Vib: {vib:.2f}, Pres: {pres:.2f}")

        time.sleep(SENSOR_INTERVAL)

if __name__ == "__main__":
    run()
