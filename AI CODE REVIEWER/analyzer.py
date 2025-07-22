import importlib

def run_analysis(module_name, code):
    try:
        module = importlib.import_module(f"modules.{module_name}")
        analyze_func = getattr(module, "analyze", None)
        if callable(analyze_func):
            return analyze_func(code)
        return f"[Module Error] '{module_name}' lacks an analyze() function."
    except Exception as e:
        return f"[Loader Error] Could not load module '{module_name}'.\nDetails: {e}"
