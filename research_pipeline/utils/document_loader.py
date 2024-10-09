import os
from llama_index import Document

def load_internal_documents(directory_path: str) -> list:
    """
    Load internal documents from the specified directory.
    """
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(os.path.join(directory_path, filename), 'r') as file:
                content = file.read()
                documents.append(content)
    return documents

def load_external_documents(api_endpoint: str) -> list:
    """
    Load external documents from an API or external storage.
    """
    # Implement API calls or external storage retrieval
    # Example placeholder
    external_data = ["External document content 1", "External document content 2"]
    return external_data