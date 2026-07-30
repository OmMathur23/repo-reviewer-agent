import subprocess

def search_code(path:str,pattern:str)->str:
    result = subprocess.run(
        ["git","grep","-n","-i",pattern],
        cwd = path,
        text = True,
        capture_output= True,
        timeout = 60
    )

    if result.returncode not in (0,1):
        return RuntimeError(f"search_code failed: {result.stderr}")

    if not result.stdout.strip():
        return f"No matches found for {pattern!r}"

    return result.stdout