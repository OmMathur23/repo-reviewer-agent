from pathlib import Path 

def list_directory(path:str)->str:
    entries = sorted(Path(path).iterdir())

    visible = []
    for entry in entries:
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            visible.append(entry.name + "/")
        else:
            visible.append(entry.name)
    
    if not visible:
        return "(empty directory)"

    return "\n".join(visible)
        