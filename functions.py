from pypdf import PdfReader
from PIL import Image
from io import BytesIO
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream


# Finding length of doc for slider limit
def len_finder(file):
    reader = PdfReader(file)
    file_pages = reader.pages

    max_pages = len(file_pages)
    return max_pages


# Main text extraction
def converter(file, targets):
    conv = DocumentConverter()

    file_bytes = file.getvalue()
    stream_obj = BytesIO(file_bytes)
    source = DocumentStream(name="User-File", stream=stream_obj)

    extracted_data = conv.convert(source, page_range=targets).document
    result = extracted_data.export_to_markdown(page_break_placeholder="Page End")

    pages = result.split("Page End")

    return pages

def chunker(pages):
    chunking_data = {}
    for content in pages:
        for i in range(len(pages)):
            chunking_metadata = {i: content}

    return chunking_metadata