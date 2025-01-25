import os
import base64
import logging
import requests

from requests.auth import HTTPBasicAuth
from config import API_USERNAME, API_PASSWORD


def create_tus_replace_url(file_url, file_path):
    """Initiate a TUS replace upload."""
    content_type = "application/pdf"
    file_name = os.path.basename(file_path)
    b64_file_name = base64.b64encode(file_name.encode("utf-8")).decode("utf-8")
    b64_content_type = base64.b64encode(content_type.encode("utf-8")).decode("utf-8")
    file_metadata = f"filename {b64_file_name},content-type {b64_content_type},"

    headers = {
        "Accept": "application/json",
        "Tus-Resumable": "1.0.0",
        "Upload-Length": str(os.path.getsize(file_path)),
        "Upload-Metadata": file_metadata,
    }

    response = requests.post(
        f"{file_url}/@tus-replace",
        headers=headers,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
    )

    if response.status_code == 201:
        location = response.headers.get("Location")
        logging.info(f"Upload URL created: {location}")
        return location
    else:
        logging.error(
            f"Failed to create replace upload URL: {response.status_code}, {response.content}"
        )
        return None


def upload_processed_pdf(file_path, upload_url):
    """Upload the processed PDF using TUS."""
    headers = {
        "Accept": "application/json",
        "Tus-Resumable": "1.0.0",
        "Upload-Offset": "0",
        "Content-Type": "application/offset+octet-stream",
    }

    with open(file_path, "rb") as f:
        file_data = f.read()

    # Add "ocr=1" parameter to indicate that the file is processed.
    url = upload_url + "?ocr=1"
    response = requests.patch(
        url,
        headers=headers,
        data=file_data,
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
    )

    if response.status_code == 204:
        final_url = response.headers.get("Location")
        logging.info(f"Processed PDF uploaded successfully, {final_url}")
    else:
        logging.error(
            f"Error uploading processed PDF: {response.status_code}, {response.content}"
        )
