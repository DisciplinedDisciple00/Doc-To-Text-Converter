from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunker(chunking_md):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)

    chunks_data = []
    for pg, content in chunking_md.items():
        chunks = splitter.split_text(content)

        for i in chunks:
            chunks_data.append({"page": pg, "content": i})

    return chunks_data