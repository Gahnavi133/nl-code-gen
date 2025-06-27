def safe_exec(code):
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return "✅ Code ran successfully", ""
    except Exception as e:
        return "", f"❌ Error: {e}"
