# tokenizer.py
# import re

# def tokenize(text):
#     return re.findall(r"\b[a-z]+\b", text.lower())




import re

STOP_WORDS = {
    "is","are","the","and","a","an","in","on","of","to","for","with","this","that"
}

def tokenize(text):
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return [w for w in words if w not in STOP_WORDS]
