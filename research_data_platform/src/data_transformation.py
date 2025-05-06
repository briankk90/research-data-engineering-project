import pandas as pd
import numpy as np
from src.utils import setup_logger

logger = setup_logger('transformation')

def transform_data(df):
    """Clean and transform raw data."""
    try:
        # Handle missing values
        df = df.fillna(df.mean(numeric_only=True))
        # Normalize numeric columns
        numeric_cols = df.select_dtypes(include=np.number).columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()
        logger.info("Data transformation completed")
        return df
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise