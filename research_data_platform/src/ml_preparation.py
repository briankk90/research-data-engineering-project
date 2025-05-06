from sklearn.preprocessing import StandardScaler
from transformers import AutoTokenizer, AutoModel
import torch
from src.utils import setup_logger

logger = setup_logger('ml_preparation')

def prepare_ml_data(df, text_column=None):
    """Prepare data for ML modeling."""
    try:
        # Feature scaling for numeric data
        scaler = StandardScaler()
        numeric_cols = df.select_dtypes(include='float64').columns
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
        # Generate text embeddings if text data exists
        if text_column:
            tokenizer = AutoTokenizer.from_pretrain('distilbert-base-uncased')
            model = AutoModel.from_pretrained('distilbert-base-uncased')
            embeddings = []
            for text in df[text_column]:
                inputs = tokenizer(text, return_tensors='pt', truncation=True)
                outputs = model(**inputs)
                embeddings.append(outputs.last_hidden_state.mean(dim=1).detach().numpy())
            df['embeddings'] = embeddings
        
        logger.info("ML data preparation completed")
        return df
    except Exception as e:
        logger.error(f"Error preparing ML data: {e}")
        raise