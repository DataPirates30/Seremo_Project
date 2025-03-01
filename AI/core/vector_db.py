# # import os
# # import fitz  # PyMuPDF for PDF processing
# # import faiss
# # import numpy as np
# # from sentence_transformers import SentenceTransformer
# # from llama_stack_client.types import Document

# # # Load SentenceTransformer for embedding generation
# # embedder = SentenceTransformer("all-MiniLM-L6-v2")

# # class VectorDB:
# #     def __init__(self):
# #         self.dimension = 384  # Output dimension of SBERT
# #         self.index = faiss.IndexFlatL2(self.dimension)
# #         self.text_data = []  # Store extracted text
# #         self.documents = []  # Store Document objects

# #     def extract_text_from_pdf(self, pdf_path):
# #         """Extracts text from a PDF file."""
# #         text = ""
# #         doc = fitz.open(pdf_path)
# #         for page in doc:
# #             text += page.get_text() + "\n"
# #         return text.strip()

# #     def add_documents(self, pdf_folder):
# #         """Processes PDFs, generates embeddings, and stores them in FAISS."""
# #         for i, pdf_file in enumerate(os.listdir(pdf_folder)):
# #             if pdf_file.endswith(".pdf"):
# #                 pdf_path = os.path.join(pdf_folder, pdf_file)
# #                 text = self.extract_text_from_pdf(pdf_path)
# #                 self.text_data.append(text)

# #                 # Create Document object for LlamaStack
# #                 document = Document(
# #                     document_id=f"pdf-{i}",
# #                     content=text,
# #                     mime_type="text/plain",
# #                     metadata={"filename": pdf_file}
# #                 )
# #                 self.documents.append(document)

# #         # Convert text to embeddings
# #         embeddings = embedder.encode(self.text_data)
# #         self.index.add(np.array(embeddings).astype("float32"))

# #     def search(self, query, top_k=2):
# #         """Finds relevant text using FAISS similarity search."""
# #         query_embedding = embedder.encode([query]).astype("float32")
# #         distances, indices = self.index.search(query_embedding, top_k)
# #         return [self.text_data[i] for i in indices[0]]

# # # Initialize vector database and process PDFs
# # vector_db = VectorDB()
# # vector_db.add_documents("data")  # Ensure PDFs are placed inside "adata"
# import os
# import fitz  # PyMuPDF for PDF processing
# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Load embedding model
# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# class VectorDB:
#     def __init__(self):
#         self.dimension = 384  # SBERT output dimension
#         self.index = faiss.IndexFlatL2(self.dimension)
#         self.text_data = []

#     def extract_text_from_pdf(self, pdf_path):
#         """Extracts and cleans text from a PDF file."""
#         text = ""
#         doc = fitz.open(pdf_path)
#         for page in doc:
#             text += page.get_text() + "\n"
#         return text.strip()

#     def add_documents(self, pdf_folder):
#         """Processes PDFs, generates embeddings, and stores them in FAISS."""
#         if not os.path.exists(pdf_folder):
#             os.makedirs(pdf_folder)  # Ensure folder exists
        
#         for pdf_file in os.listdir(pdf_folder):
#             if pdf_file.endswith(".pdf"):
#                 pdf_path = os.path.join(pdf_folder, pdf_file)
#                 text = self.extract_text_from_pdf(pdf_path)
#                 self.text_data.append(text)

#         # Convert text to embeddings
#         embeddings = embedder.encode(self.text_data)
#         self.index.add(np.array(embeddings).astype("float32"))

#     def search(self, query, top_k=2):
#         """Finds relevant text using FAISS similarity search."""
#         query_embedding = embedder.encode([query]).astype("float32")
#         distances, indices = self.index.search(query_embedding, top_k)
#         return [self.text_data[i] for i in indices[0]]

# # Initialize vector database
# vector_db = VectorDB()
# vector_db.add_documents("data")  # Ensure PDFs are inside "AI/data"
