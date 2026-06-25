from rag import query_embedder, retrieve
from llm import prompt_builder, response


def ask_rag(query):
    query_embeddings = query_embedder(query)
    retrieved_data = retrieve(query_embeddings)
    prompt = prompt_builder(query, retrieved_data)
    answer = response(prompt)

    return answer