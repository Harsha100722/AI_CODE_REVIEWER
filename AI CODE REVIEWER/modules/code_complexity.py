import re

def analyze(code):
    lines = code.strip().splitlines()
    non_empty_lines = [ln for ln in lines if ln.strip()]
    length = len(non_empty_lines)
    avg_len = sum(len(ln) for ln in non_empty_lines) / length if length else 0
    max_len = max((len(ln) for ln in non_empty_lines), default=0)
    max_indent = max((len(ln) - len(ln.lstrip())) for ln in non_empty_lines) if non_empty_lines else 0
    nesting = len(re.findall(r'(def |function |class |\{|})', code))
    summary = (
        f"Lines of code: {length}\n"
        f"Max line length: {max_len}\n"
        f"Average line length: {avg_len:.1f}\n"
        f"Estimated nesting/blocks: {nesting}\n"
    )
    if length > 50 or max_len > 100 or nesting > 10:
        summary += "\n⚠️ Code is lengthy or deeply nested; could be hard to maintain."
    elif length < 15 and nesting <= 5:
        summary += "\n✅ Short/simple code—likely maintainable."
    else:
        summary += "\nClarity/compexity: moderate."
    return summary
