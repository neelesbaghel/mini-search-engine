# from document_loader import load_documents
# from tokenizer import tokenize
# from indexer import build_index
# from search import search

# DATA_FOLDER = "../data"

# def main():
#     print("Mini Search Engine Started")

#     documents = load_documents(DATA_FOLDER)
#     index = build_index(documents, tokenize)

#     while True:
#         query = input("\nSearch (or type exit): ")

#         if query.lower() == "exit":
#             break

#         results = search(query, documents, index)

#         if not results:
#             print("No results found")
#         else:
#             for doc, score in results:
#                 print(f"{doc} -> score {score}")

# if __name__ == "__main__":
#     main()



from document_loader import load_documents
from search import search
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "data")

documents = load_documents(DATA_FOLDER)

while True:
    q = input("Search (exit to quit): ")
    if q.lower() == "exit":
        break

    results = search(q, documents)
    for r in results:
        print(f"{r['document']} -> {r['sentence']} ({r['score']:.2f})")
