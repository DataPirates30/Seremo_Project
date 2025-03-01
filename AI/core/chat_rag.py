# # import os
# # import subprocess
# # from rag_retriever import get_rag_context  # Import RAG retriever

# # def run_chatbot():
# #     """
# #     Runs chatbot.py while injecting RAG-retrieved context into user queries.
# #     """
# #     while True:
# #         user_prompt = input("You: ")
# #         if user_prompt.lower() == "exit":
# #             break

# #         # Retrieve context from RAG
# #         retrieved_context = get_rag_context(user_prompt)

# #         # Modify prompt to include RAG context
# #         final_prompt = f"Context: {retrieved_context}\nQuestion: {user_prompt}"

# #         # Run chatBot.py with modified prompt
# #         subprocess.run(["python", "core/chatBot.py", final_prompt])

# # if __name__ == "__main__":
# #     run_chatbot()

# import os
# import subprocess
# from rag_retriever import get_rag_context  # ✅ Use updated RAG retriever

# def run_chatbot():
#     """
#     Runs chatBot.py while injecting RAG-retrieved context into user queries.
#     """
#     while True:
#         user_prompt = input("You: ")
#         if user_prompt.lower() == "exit":
#             break
#         # ✅ Retrieve relevant context from RAG
#         retrieved_context = get_rag_context(user_prompt)

#         # ✅ Modify prompt to include retrieved context
#         final_prompt = f"Context: {retrieved_context}\nQuestion: {user_prompt}"

#         # ✅ Run chatBot.py with enhanced prompt
#         subprocess.run(["python", "core/chatBot.py", final_prompt])

# if __name__ == "__main__":
#     run_chatbot()
