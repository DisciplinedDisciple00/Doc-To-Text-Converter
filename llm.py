import ollama


#Appropriate prompt builder
def prompt_builder(query, retrieved_data):
    chunks_content = retrieved_data["documents"][0]
    cleaned_data = "\n\n".join(chunks_content)
    pg_nums = retrieved_data["metadatas"][0]

    prompt = (f"""You are a helpful assistant for a RAG pipeline that will answer user queries based ONLY on the context provided for that query and give source(page number) if possible. 
    The query is : {query}
    The context is : {cleaned_data}
    The source is : {pg_nums}
    If the answer cannot be found in the provided context, say that the information is not available in the document.""")

    return prompt


#LLM response
def response(prompt, model="gpt-oss:20b"):
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )

    return response["message"]["content"]