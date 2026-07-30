from tools.file_reader import read_file
from tools.clone_repo import clone_repo
from tools.list_directory import list_directory
from tools.search import search_code

TOOLS = {
    "read_file": read_file,
    "clone_repo" : clone_repo,
    "list_directory" : list_directory,
    "search_code" : search_code,
}