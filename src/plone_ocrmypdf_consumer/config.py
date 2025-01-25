import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL", "")

API_URL = os.getenv("API_URL", "")
API_USERNAME = os.getenv("API_USERNAME", "")
API_PASSWORD = os.getenv("API_PASSWORD", "")

TEMP_PDF_DIR = "/tmp"
