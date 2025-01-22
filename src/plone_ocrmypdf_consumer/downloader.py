import os
import logging
import requests
from requests.auth import HTTPBasicAuth
from config import API_USERNAME, API_PASSWORD, TEMP_PDF_DIR


def download_pdf(url, filename):
    """Download the PDF."""
    try:
        headers = {"Accept": "application/pdf"}
        basic = HTTPBasicAuth(API_USERNAME, API_PASSWORD)

        logging.info(f"Downloading PDF from {url}")
        response = requests.get(url, headers=headers, auth=basic)

        if response.status_code != 200:
            logging.error(f"Error downloading PDF from {url}: {response.content}")
            return None

        file_path = os.path.join(TEMP_PDF_DIR, filename)

        with open(file_path, "wb") as f:
            f.write(response.content)

        logging.info(f"PDF downloaded successfully: {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"Error downloading PDF: {e}")
        return None
