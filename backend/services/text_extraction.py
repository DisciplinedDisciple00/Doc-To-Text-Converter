from backend.services.functions import converter

def text_extraction(file_bytes, targets):
    result = converter(file_bytes, targets)
    return result