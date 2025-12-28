# def build_index(documents, tokenize):
#     index = {}

#     for doc, text in documents.items():
#         for word in tokenize(text):
#             index.setdefault(word, set()).add(doc)

#     return index



from collections import defaultdict

def build_index(documents, tokenize):
    index = defaultdict(set)
    vocabulary = set()

    for doc, text in documents.items():
        tokens = tokenize(text)
        for token in tokens:
            index[token].add(doc)
            vocabulary.add(token)

    return index, sorted(vocabulary)
