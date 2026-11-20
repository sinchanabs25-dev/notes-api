from flask import Flask, jsonify, request

app = Flask(__name__)

notes = []


@app.route("/")
def home():
    return jsonify(message="Hello DevOps! Kannada Notes API 🚀")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify(error="text is required"), 400
    note = {"id": len(notes) + 1, "text": data["text"]}
    notes.append(note)
    return jsonify(note), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)