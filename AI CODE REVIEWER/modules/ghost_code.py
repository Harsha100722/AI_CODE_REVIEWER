import re

def analyze(code):
    # Simple pattern: variable assigned but not used elsewhere
    assigned = re.findall(r'\b(\w+)\s*=', code)
    unused = []
    for var in set(assigned):
        if code.count(var) == 1:
            unused.append(var)
    if unused:
        return f"Potential dead/ghost code: variables assigned but apparently unused: {', '.join(unused)}"
    return "No ghost/dead code found."
