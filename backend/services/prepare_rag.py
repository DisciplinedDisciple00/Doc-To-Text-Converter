from backend.services.rag import chunker, embedder, store
from backend.services.functions import chunker_md


def prep_rag(result):
    chunking_metadata = chunker_md(result)
    chunking_data = chunker(chunking_metadata)
    embeddings = embedder(chunking_data)
    store(chunking_data, embeddings)