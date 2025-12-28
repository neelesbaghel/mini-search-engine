# import os

# def load_documents(folder_path):
#     documents = {}

#     for file in os.listdir(folder_path):
#         if file.endswith(".txt"):
#             with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
#                 documents[file] = f.read()

#     return documents




import os

def load_documents(folder_path):
    documents = {}
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), encoding="utf-8") as f:
                documents[file] = f.read()
    return documents
