import logging
import ocrmypdf


def process_pdf(file_path):
    """Process the PDF with OCRmyPDF."""
    try:
        ocrmypdf.ocr(file_path, file_path, language="eng")
        logging.info(f"Processed PDF saved to: {file_path}")
        return True
    except ocrmypdf.exceptions.EncryptedPdfError:
        logging.info("Skipped document because it is encrypted.")
        return False
    except ocrmypdf.exceptions.PriorOcrFoundError:
        logging.info("Skipped document because it already contained text.")
        return False
    except ocrmypdf.exceptions.DigitalSignatureError:
        logging.info("Skipped document because it has a digital signature.")
        return False
    except ocrmypdf.exceptions.TaggedPDFError:
        logging.info("Skipping processing as the PDF is marked as Tagged.")
        return False
    except Exception as e:
        logging.error(f"Error processing PDF: {e}")
        return None
