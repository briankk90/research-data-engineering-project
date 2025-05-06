from sqlalchemy import create_engine
import yaml
from src.utils import setup_logger

logger = setup_logger('loading')

def load_data(df, table_name):
    """Load data into PostgreSQL."""
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    db_url = config['database']['url']
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info(f"Data loaded into {table_name}")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise