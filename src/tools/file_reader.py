from pathlib import Path
#we'll be given a path for example src/auth.py , and we have to read from it
def read_file(path:str)->str:
    return Path(path).read_text(encoding="utf-8")


