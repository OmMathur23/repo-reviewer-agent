import subprocess
import tempfile
#input: github repo link , output: local directory path
def clone_repo(url:str)->str:

    if not url.startswith((
        "https://github.com/",
        "git@github.com:"
    )):
        raise ValueError(f"Only GitHub URLs are supported for now, got: {url!r}")

    dest = tempfile.mkdtemp(prefix="repo-reviewer")

    result = subprocess.run(
        ["git","clone","--depth","1",url,dest],
        capture_output=True,
        text= True,
        timeout = 60
    )

    if result.returncode != 0:
        raise RuntimeError(f"git clone failed for {url}: \n {result.stderr}")

    return dest