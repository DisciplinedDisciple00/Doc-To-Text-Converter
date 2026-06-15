from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


#Initializing chunk splitter, embedder
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
emb =  SentenceTransformer("BAAI/bge-base-en-v1.5")


#Chunk converter
def chunker(chunking_md):
    chunks_data = []
    for pg, content in chunking_md.items():
        chunks = splitter.split_text(content)

        for i in chunks:
            chunks_data.append({"page": pg, "content": i})

    return chunks_data


def embedder(chunks_data):
    chunks_content = []

    for data in chunks_data:
        cc = data["content"]
        chunks_content.append(cc)

    embeddings = emb.encode(chunks_content, batch_size=128)

    return embeddings