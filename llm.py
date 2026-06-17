import ollama


#Appropriate prompt builder
def prompt_builder(query, retrieved_data):
    cleaned_rdata = retrieved_data["documents"][0]

    prompt = (f"""You are a helpful assistant for a RAG pipeline that will answer user queries based ONLY on the context provided for that query. 
    The query is : {query}
    And the context is {retrieved_data}
    If the answer cannot be found in the provided context, say that the information is not available in the document.""")

    return prompt


#LLM response
def response(prompt, model="gemma3:12b"):
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