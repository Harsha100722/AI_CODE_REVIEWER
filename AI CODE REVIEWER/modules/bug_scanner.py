import re

def analyze(code):
    findings = []
    if not code.strip():
        return "No code provided."
    if "TODO" in code or "todo" in code:
        findings.append("Found TODO — unfinished or placeholder code.")
    if re.search(r'def\s+\w+\s*\(|function\s+\w+\s*\(', code):
        findings.append("Function definitions detected.")
    if '{' in code and '}' in code:
        findings.append("Curly braces detected—possible block or scope usage (C/JS/Java/Go).")
    if '<html' in code.lower() or '<!doctype html' in code.lower():
        findings.append("HTML markup detected.")
    if "#include" in code or 'std::' in code:
        findings.append("Likely C/C++ code structures present.")
    if not findings:
        return "No major universal issues found."
    return "\n".join(findings)
