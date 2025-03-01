from vector_db import vector_db  # Import FAISS database
import re

def clean_text(text):
    """
    Cleans retrieved text for natural conversation flow.
    - Removes bullet points and extra formatting.
    - Ensures responses flow naturally.
    """
    text = re.sub(r"^\s*[\*\-\d]+\s*", "", text, flags=re.MULTILINE)  # Remove bullets/numbers
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
    return text

def get_rag_context(user_prompt):
    """
    Retrieves relevant text from FAISS for ALL QUERIES.
    - If Hindu-related content is found, makes response more precise.
    - If general content is found, LLaMA still gets relevant context.
    """
    retrieved_docs = vector_db.search(user_prompt, top_k=2)
    cleaned_text = " ".join([clean_text(doc) for doc in retrieved_docs])

    if not cleaned_text.strip():
        return "I don't have enough information on that topic, but I'm happy to help with anything else."

    return f"Here is relevant information from our knowledge base: {cleaned_text}"
