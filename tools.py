from langchain_ollama import ChatOllama
import os
import subprocess
from langchain_core.tools import tool

@tool
def write_file(file_path: str, content: str):
    """
    Writes content to a file inside ./builds/.
    Auto-creates missing directories.
    """

    root = os.path.abspath("builds")
    abs_path = os.path.abspath(file_path)

    if not abs_path.startswith(root):
        return "Error: write_file is restricted to the ./builds/ directory."

    try:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully wrote {len(content)} bytes to {abs_path}"

    except Exception as e:
        return f"Error writing file: {e}"


@tool
def read_file(file_path: str):
    """Reads a file. Args: file_path"""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def list_files(root_path: str):
    """
    Returns a simple directory tree structure as a string.
    Useful for agents to quickly inspect files and folders.

    Args:
        root_path: The directory to scan (must be inside ./builds/)
    """

    import os

    if "builds/" not in root_path:
        return "Error: Only allowed to inspect files inside 'builds/' directory."

    if not os.path.exists(root_path):
        return f"Error: Path does not exist -> {root_path}"

    tree_output = []

    # walk the directory
    for base, dirs, files in os.walk(root_path):
        level = base.replace(root_path, "").count(os.sep)
        indent = "  " * level
        tree_output.append(f"{indent}{os.path.basename(base)}/")

        sub_indent = "  " * (level + 1)
        for f in files:
            tree_output.append(f"{sub_indent}{f}")

    return "\n".join(tree_output)


@tool
def run_shell_command(command: str, work_dir: str):
    """
    Executes a terminal command.
    Args:
        command: e.g., 'python main.py' or 'npm install'
        work_dir: the directory to run in (e.g., ./builds/app-1)
    """
    try:
        result = subprocess.run(
            command,
            cwd=work_dir,
            shell=True,
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            return f"SUCCESS:\n{result.stdout}"
        else:
            return f"FAILED:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    except Exception as e:
        return f"System Error: {e}"

llm = ChatOllama(
    model="llama3.1:8b", 
    temperature=0,
    format="json" 
)

llm_worker = llm.bind_tools([write_file, read_file, run_shell_command])