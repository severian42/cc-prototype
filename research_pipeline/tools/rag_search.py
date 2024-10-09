from llama_index.core import VectorStoreIndex, Document
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

async def rag_search(query: str, index: VectorStoreIndex):
    """Finds specialist information using RAG search."""
    print(">>> rag_search")
    retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
    query_engine = RetrieverQueryEngine(retriever=retriever)
    response = query_engine.query(query)
    return str(response)