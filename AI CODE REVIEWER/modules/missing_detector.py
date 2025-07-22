import re

def analyze(code):
    missing = []
    if not re.search(r'def\s+\w+|function\s+\w+', code):
        missing.append("No functions found.")
    if not re.search(r'return |print |console\.log|System\.out\.print', code):
        missing.append("No output statements found.")
    if "test" not in code.lower():
        missing.append("No test references or test cases found.")
    return (
        "Missing Elements:\n" + "\n".join(f"- {m}" for m in missing)
        if missing else "No essential elements missing."
    )
