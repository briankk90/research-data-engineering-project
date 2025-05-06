import pandas as pd
import requests
from src.utils import setup_logger

logger = setup_logger('ingestion')

def ingest_csv(file_path):
    """Ingest data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Successfully ingested {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error ingesting {file_path}: {e}")
        raise

def ingest_api(api_url):
    """Ingest data from a REST API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = pd.DataFrame(response.json())
        logger.info(f"Successfully ingested data from {api_url}")
        return data
    except Exception as e:
        logger.error(f"Error ingesting API data: {e}")
        raise