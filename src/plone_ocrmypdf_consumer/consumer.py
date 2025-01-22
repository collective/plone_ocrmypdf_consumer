import json
import logging
import redis
import requests
from time import sleep
from requests.auth import HTTPBasicAuth

from config import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_CHANNEL,
    API_URL,
    API_USERNAME,
    API_PASSWORD,
)
from processor import process_pdf
from utils import cleanup_temp_file
from downloader import download_pdf
from uploader import create_tus_replace_url, upload_processed_pdf


class OCRConsumer:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        self.pubsub = self.redis_client.pubsub()

    def start(self):
        """Start reading messages from Redis PubSub channel."""
        self.pubsub.subscribe(REDIS_CHANNEL)
        logging.info(f"Subscribed to Redis channel: {REDIS_CHANNEL}")

        try:
            for message in self.pubsub.listen():
                if message["type"] == "message":
                    self.process_message(message)
        except redis.exceptions.ConnectionError as e:
            logging.error(f"Redis connection error {e}")

    def process_message(self, message):
        """Process the OCR task."""
        try:
            data = json.loads(message["data"])
            uid = data["uid"]

            headers = {"Accept": "application/json"}
            url = f"{API_URL}/@search?UID={uid}"
            basic = HTTPBasicAuth(API_USERNAME, API_PASSWORD)
            sleep(1)

            response = requests.get(url, headers=headers, auth=basic)

            if response.status_code != 200:
                logging.error(f"Error fetching object by UID {uid}: {response.content}")
                return

            result = response.json()
            if not result or "items" not in result or len(result["items"]) == 0:
                logging.error(f"No object found with UID {uid}")
                return

            item = result["items"][0]
            file_url = item["@id"]
            filename = item["title"]

            downloaded_pdf_path = download_pdf(file_url, filename)
            if downloaded_pdf_path:
                processed = process_pdf(downloaded_pdf_path)

                if processed:
                    upload_url = create_tus_replace_url(file_url, downloaded_pdf_path)
                    if upload_url:
                        upload_processed_pdf(downloaded_pdf_path, upload_url)
                else:
                    logging.info(f"File {filename} already processed. Skipping upload.")

                cleanup_temp_file(downloaded_pdf_path)

        except Exception as e:
            logging.error(f"Error processing message {e}")
