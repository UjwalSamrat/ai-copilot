from pathlib import Path

SUPPORTED_EXTENSIONS = (".py", ".js", ".ts", ".tsx", ".jsx")


def get_code_files(root_path):
    root_path = Path(root_path)
    code_files = []
    for file_path in root_path.rglob("*"):
        if file_path.is_file() and file_path.suffix in SUPPORTED_EXTENSIONS:
            code_files.append(str(file_path))
    return code_files


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    repositories_path = project_root / "data" / "repositories"

    files = get_code_files(repositories_path)
    print(f"Found {len(files)} code files.")
    for file in files:
        print(file)
