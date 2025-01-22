import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def setup_temp_dir(temp_dir):
    """Ensure temporary directory exists."""
    Path(temp_dir).mkdir(parents=True, exist_ok=True)


def cleanup_temp_file(file_path):
    """Clean up the temporary file after processing and upload."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"Temporary file {file_path} cleaned up successfully.")
        else:
            logging.warning(f"Temporary file {file_path} not found for cleanup.")
    except Exception as e:
        logging.error(f"Error cleaning up temporary file {file_path}: {e}")
