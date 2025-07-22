import re

def analyze(code):
    summary = []
    if re.search(r'def\s+\w+\s*\(|function\s+\w+\s*\(', code):
        summary.append("Contains function definitions.")
    if re.search(r'class\s+\w+', code):
        summary.append("Contains class/type definitions (OOP).")
    if re.search(r'if[ (\n]', code):
        summary.append("Conditional logic detected.")
    if re.search(r'\bfor\b|\bwhile\b', code):
        summary.append("Iterative/loop logic present.")
    if re.search(r'import\s+\w+|#include\s*<', code):
        summary.append("Imports or includes detected.")
    if "<html" in code.lower():
        summary.append("HTML structure code.")
    if not summary:
        return "No clear code intent detected."
    return "Intent Analysis:\n" + "\n".join(summary)
