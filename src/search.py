# from tokenizer import tokenize
# from ranker import rank_documents

# def search(query, documents):
#     query_tokens = tokenize(query)
#     return rank_documents(query_tokens, documents)

# from tokenizer import tokenize
# import re

# def split_sentences(text):
#     return re.split(r'(?<=[.!?])\s+', text)

# def highlight(sentence, tokens):
#     for t in tokens:
#         sentence = re.sub(
#             rf"({re.escape(t)})",
#             r"<mark>\1</mark>",
#             sentence,
#             flags=re.IGNORECASE
#         )
#     return sentence

# def search(query, documents):
#     query_tokens = tokenize(query)
#     results = []

#     for doc, content in documents.items():
#         sentences = split_sentences(content)

#         for s in sentences:
#             words = tokenize(s)
#             score = sum(words.count(t) for t in query_tokens)

#             if score > 0:
#                 results.append({
#                     "document": doc,
#                     "sentence": highlight(s, query_tokens),
#                     "score": score
#                 })

#     return sorted(results, key=lambda x: x["score"], reverse=True)









from tokenizer import tokenize
import re

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)

def highlight(sentence, tokens):
    for token in tokens:
        sentence = re.sub(
            rf"({re.escape(token)})",
            r"<span class='highlight'>\1</span>",
            sentence,
            flags=re.IGNORECASE
        )
    return sentence

def search(query, documents):
    query_tokens = tokenize(query)
    results = []

    for doc, content in documents.items():
        sentences = split_sentences(content)

        for sentence in sentences:
            words = tokenize(sentence)
            score = sum(words.count(t) for t in query_tokens)

            if score > 0:
                results.append({
                    "document": doc,
                    "sentence": highlight(sentence, query_tokens),
                    "score": score
                })

    return sorted(results, key=lambda x: x["score"], reverse=True)






