from consumer import OCRConsumer
from config import TEMP_PDF_DIR
from utils import setup_temp_dir

if __name__ == "__main__":
    setup_temp_dir(TEMP_PDF_DIR)
    consumer = OCRConsumer()
    consumer.start()
