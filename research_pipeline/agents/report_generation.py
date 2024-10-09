from .base_agent import BaseAgent
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss

class ReportGenerationAgent(BaseAgent):
    def __init__(self, state):
        super().__init__(state)
        self.index = self._create_index()

    def _create_index(self):
        documents = SimpleDirectoryReader("data/report_generation").load_data()
        parser = SimpleNodeParser.from_defaults()
        nodes = parser.get_nodes_from_documents(documents)

        dimension = 1536  # This should match the dimension of your embeddings
        faiss_index = faiss.IndexFlatL2(dimension)
        vector_store = FaissVectorStore(faiss_index=faiss_index)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        return VectorStoreIndex(nodes, storage_context=storage_context)

    def run(self, input_text, chat_history=None):
        query_engine = self.index.as_query_engine()
        response = query_engine.query(f"Generate a report for: {input_text}")
        return str(response)