import os
import re

def detect_language(code, filename=None):
    # Try to use guesslang
    try:
        from guesslang import Guess
        guess = Guess()
        lang = guess.language_name(code) if code.strip() else None
        if lang and lang != "Unknown":
            return lang
    except Exception:
        pass

    # Fallback: Use file extension
    ext_map = {
        ".py": "Python", ".js": "JavaScript", ".java": "Java", ".cpp": "C++", ".c": "C",
        ".cs": "C#", ".php": "PHP", ".html": "HTML", ".ts": "TypeScript", ".go": "Go",
        ".rb": "Ruby", ".rs": "Rust"
    }
    if filename:
        ext = os.path.splitext(filename)[-1].lower()
        if ext in ext_map:
            return ext_map[ext]

    # Fallback: regex-based heuristic
    text = code.lower()
    if '<html' in text or '<!doctype html' in text: return "HTML"
    if 'def ' in code and 'import ' in code: return "Python"
    if 'function ' in code: return "JavaScript"
    return "Text/Unknown"
