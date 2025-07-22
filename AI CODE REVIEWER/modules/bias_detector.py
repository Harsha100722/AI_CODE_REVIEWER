import re

def analyze(code):
    bias_terms = [
        "gender", "race", "age", "religion", "nationality", "ethnic", "disabled",
        "female", "male", "asian", "black", "white", "hispanic", "marital"
    ]
    found = [term for term in bias_terms if re.search(r'\b' + term + r'\b', code, re.I)]
    return (
        f"Bias-related terms detected: {', '.join(found)}"
        if found else "No explicit bias-prone terms detected."
    )
