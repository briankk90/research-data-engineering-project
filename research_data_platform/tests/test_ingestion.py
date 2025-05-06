import unittest
import pandas as pd
from src.data_ingestion import ingest_csv

class TestIngestion(unittest.TestCase):
    def test_ingest_csv(self):
        df = ingest_csv('data/raw/sample_data.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()