from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load Knowledge Base for RAG-style retrieval
with open("knowledge_base.txt", "r") as f:
    kb_sentences = [line.strip() for line in f.readlines() if line.strip()]

# TF-IDF Vectorizer Initialization
vectorizer = TfidfVectorizer().fit(kb_sentences)
kb_vectors = vectorizer.transform(kb_sentences)


def rag_answer(query):
    # Convert query to vector
    query_vec = vectorizer.transform([query])

    # Compute similarity to each KB sentence
    similarity_scores = cosine_similarity(query_vec, kb_vectors).flatten()

    # Retrieve top 3 relevant tips
    top_indices = similarity_scores.argsort()[-3:][::-1]

    results = [kb_sentences[i] for i in top_indices if similarity_scores[i] > 0]

    if not results:
        return "Water is precious! Try closing taps, fixing leaks, and using water wisely."

    return "\n".join(f"• {r}" for r in results)


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_q = request.form["question"]
        response = rag_answer(user_q)
    return render_template("index.html", answer=response)


if __name__ == "__main__":
    app.run(debug=True)
