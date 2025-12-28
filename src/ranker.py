# def rank_documents(query_tokens, documents):
#     scores = {}

#     for doc, text in documents.items():
#         words = text.lower().split()
#         score = sum(words.count(token) for token in query_tokens)

#         if score > 0:
#             scores[doc] = score

#     return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# def rank_documents(query_tokens, documents):
#     scores = {}

#     for doc, text in documents.items():
#         words = text.lower().split()
#         score = sum(words.count(token) for token in query_tokens)

#         if score > 0:
#             scores[doc] = score

#     return sorted(scores.items(), key=lambda x: x[1], reverse=True)












import math
from collections import Counter

def tf_idf_score(query_tokens, documents):
    scores = {}
    N = len(documents)

    doc_freq = Counter()
    for text in documents.values():
        for w in set(text.lower().split()):
            doc_freq[w] += 1

    for doc, text in documents.items():
        words = text.lower().split()
        tf = Counter(words)
        score = 0

        for t in query_tokens:
            if t in tf:
                idf = math.log(N / (1 + doc_freq[t]))
                score += tf[t] * idf

        if score > 0:
            scores[doc] = score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)



