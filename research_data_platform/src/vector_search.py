from qdrant_client import QdrantClient
import yaml
from src.utils import setup_logger

logger = setup_logger('vector_search')

def store_embeddings(embeddings, collection_name):
    """Store embeddings in Qdrant."""
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    qdrant_url = config['qdrant']['url']
    try:
        client = QdrantClient(url=qdrant_url)
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config={'size': embeddings[0].shape[1], 'distance': 'Cosine'}
        )
        client.upload_collection(
            collection_name=collection_name,
            vectors=embeddings,
            payload=[{'id': i} for i in range(len(embeddings))]
        )
        logger.info(f"Embeddings stored in {collection_name}")
    except Exception as e:
        logger.error(f"Error storing embeddings: {e}")
        raise