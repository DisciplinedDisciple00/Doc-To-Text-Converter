from backend.services.rag import query_embedder, retrieve
from backend.services.llm import prompt_builder, llm_response


def ask_rag(query):
    query_embeddings = query_embedder(query)
    retrieved_data = retrieve(query_embeddings)
    prompt = prompt_builder(query, retrieved_data)

    return llm_response(prompt)