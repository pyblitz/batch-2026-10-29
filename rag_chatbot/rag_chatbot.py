"""Ask Your Notes Anything - a tiny RAG chatbot (no API key needed).
1. Split notes.txt into chunks. 2. Score chunks by question-word overlap.
3. Answer with the best chunk QUOTED as the source.
Run: python3 rag_chatbot.py "What is Python?"
"""
import re, sys

def load_chunks(path="notes.txt"):
    text = open(path, encoding="utf-8").read()
    return [c.strip() for c in text.split("\n") if c.strip()]

def words(s):
    return set(re.findall(r"[a-z]+", s.lower()))

def ask(question, chunks):
    qw = words(question) - {"what", "is", "a", "the", "how", "does", "do", "why"}
    best, best_score = None, -1
    for chunk in chunks:
        score = len(qw & words(chunk))
        if score > best_score:
            best, best_score = chunk, score
    return best

if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "What is Python?"
    chunks = load_chunks()
    answer = ask(question, chunks)
    print("Q:", question)
    print("A:", answer)
    print("Source: notes.txt ->", repr(answer))
