import os
from pathlib import Path

import requests

MODEL_NAME = "cs5704-tutor"  # make sure you created this
LECTURE_DIR = Path(__file__).parent / "Spring 2026 (MD)"
MAX_LECTURE_CHARS = 12000


def load_lecture_content():
    """Load relevant lecture markdown files with a safe size cap."""
    if not LECTURE_DIR.exists():
        return "[Lecture folder not found]"

    relevant_keywords = (
        "testing",
        "coverage",
        "metrics",
        "exam review",
        "code analysis",
    )

    selected_files = []
    for root, _, files in os.walk(LECTURE_DIR):
        for file_name in files:
            if not file_name.lower().endswith(".md"):
                continue
            full_path = Path(root) / file_name
            rel = str(full_path.relative_to(LECTURE_DIR)).lower()
            if any(keyword in rel for keyword in relevant_keywords):
                selected_files.append(full_path)

    # Fallback: if filtering misses everything, use all markdown files.
    if not selected_files:
        selected_files = sorted(LECTURE_DIR.rglob("*.md"))
    else:
        selected_files = sorted(selected_files)

    chunks = []
    total_chars = 0

    for file_path in selected_files:
        try:
            text = file_path.read_text(encoding="utf-8")
        except OSError:
            continue

        if not text.strip():
            continue

        rel_name = str(file_path.relative_to(LECTURE_DIR))
        chunk = f"\n---\nSource: {rel_name}\n{text}\n"
        remaining = MAX_LECTURE_CHARS - total_chars
        if remaining <= 0:
            break

        if len(chunk) > remaining:
            chunk = chunk[:remaining]

        chunks.append(chunk)
        total_chars += len(chunk)

    if not chunks:
        return "[No lecture markdown content loaded]"

    return "".join(chunks)


LECTURE_CONTENT = load_lecture_content()

def chat(prompt):
    url = "http://localhost:11434/api/generate"
    full_prompt = f"""You are a CS5704 Software Testing Study Assistant.

Use ONLY the following lecture material to answer.
If the answer is not in the lecture material, say: "not covered in lecture."

Lecture material:
{LECTURE_CONTENT}

Student question:
{prompt}
"""

    response = requests.post(url, json={
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    })
    payload = response.json()

    # Standard /api/generate success shape.
    if "response" in payload:
        return payload["response"]

    # Some Ollama flows return chat-style payloads.
    if "message" in payload and isinstance(payload["message"], dict):
        if "content" in payload["message"]:
            return payload["message"]["content"]

    # Graceful error surface for model/endpoint issues.
    if "error" in payload:
        return f"[Ollama error] {payload['error']}"

    return f"[Unexpected response] {payload}"

def main():
    print("=== CS5704 Software Testing Chatbot ===")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = chat(user_input)
        print("\nBot:\n", response, "\n")

if __name__ == "__main__":
    main()