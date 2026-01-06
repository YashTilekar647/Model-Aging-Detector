import logging
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

REPORT_PATH = os.path.join(PROJECT_ROOT, "reports", "aging_report.txt")

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

logging.basicConfig(
    filename=REPORT_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(message):
    logging.info(message)
