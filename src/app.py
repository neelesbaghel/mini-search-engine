from flask import Flask, request, jsonify, render_template
import os

from document_loader import load_documents
from search import search   # this is your search function

app = Flask(__name__)

# -------------------------
# Load documents (SAFE PATH)
# -------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "..", "data")
documents = load_documents(DATA_PATH)

# -------------------------
# HOME PAGE (Frontend)
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------
# SEARCH PAGE (Frontend)
# -------------------------
@app.route("/search-page")
def search_page():
    query = request.args.get("q")

    if not query:
        return render_template("index.html", results=[])

    results = search(query, documents)
    return render_template("index.html", results=results)

# -------------------------
# SEARCH API (JSON)
# -------------------------
@app.route("/search", methods=["GET"])
def search_api():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    results = search(query, documents)
    return jsonify(results)

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import os
from document_loader import load_documents
from search import search

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "..", "data")

documents = load_documents(DATA_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search_api():
    query = request.args.get("q")
    if not query:
        return jsonify([])
    return jsonify(search(query, documents))

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

















# from flask import Flask, request, jsonify, render_template
# import os
# from document_loader import load_documents
# from search import search

# app = Flask(__name__)

# BASE_DIR = os.path.dirname(__file__)
# DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

# documents = load_documents(DATA_PATH)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/search")
# def search_api():
#     query = request.args.get("q")
#     if not query:
#         return jsonify([])
#     return jsonify(search(query, documents))

# if __name__ == "__main__":
#     app.run(debug=True)





