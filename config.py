# config.py

DB_PATH = "data/database.db"
SENSOR_INTERVAL = 5  # seconds between sensor reads

# Thresholds (can be learned by ML too)
TEMP_LIMIT = 80        # °C
VIBRATION_LIMIT = 5.0  # arbitrary units
PRESSURE_LIMIT = 150   # PSI
