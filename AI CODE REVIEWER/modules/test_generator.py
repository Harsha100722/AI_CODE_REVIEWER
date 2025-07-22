import re

def analyze(code):
    patterns = [
        r'def\s+(\w+)\s*\(',                       # Python
        r'function\s+(\w+)\s*\(',                  # JavaScript/TypeScript
        r'(?:public|private|protected)?\s+\w+\s+(\w+)\s*\(',  # Java/C/C++
    ]
    found = set()
    for pat in patterns:
        found |= set(re.findall(pat, code))
    if not found:
        return "No functions found to generate test stubs."
    stubs = []
    for func in found:
        stubs.append(f"def test_{func}():\n    # TODO: implement test for '{func}'\n    assert False  # replace with real test")
    return "Sample Test Stubs:\n\n" + "\n\n".join(stubs)
