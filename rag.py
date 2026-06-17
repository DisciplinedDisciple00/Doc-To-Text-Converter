from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb


#Initializing chunk splitter, embedder
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
emb =  SentenceTransformer("BAAI/bge-base-en-v1.5")


#Initializing chromaDB
client = chromadb.PersistentClient("./chroma_db")


#Chunk converter
def chunker(chunking_md):
    chunks_data = []
    for pg, content in chunking_md.items():
        chunks = splitter.split_text(content)

        for i in chunks:
            chunks_data.append({"page": pg, "content": i})

    return chunks_data


#Embeddings generator
def embedder(chunks_data):
    chunks_content = []
    for data in chunks_data:
        cc = data["content"]
        chunks_content.append(cc)

    embeddings = emb.encode(chunks_content, batch_size=128)

    return embeddings


#Storing in chromaDB
def store(chunks_data, embeddings):
    ids = [str(i) for i in range(len(embeddings))]

    chunks_content = []
    pg_metadata = []
    for data in chunks_data:
        cc = data["content"]
        chunks_content.append(cc)
        pg = data["page"]
        pg_metadata.append({"page": pg})

    try:
        client.delete_collection(name="doc_rag")
    except:
        pass

    collection = client.get_or_create_collection(name="doc-rag")

    collection.add(ids=ids, embeddings=embeddings, metadatas=pg_metadata, documents=chunks_content)


#Generating query embeddings
def query_embedder(query):
    query_embedding = emb.encode(query)

    return query_embedding


#Returning relevant data retrieved from comparing with database
def retrieve(query_embeddings):
    collection = client.get_or_create_collection(name="doc-rag")
    retrieved_data = collection.query(query_embeddings=query_embeddings, n_results=3)

    return retrieved_data