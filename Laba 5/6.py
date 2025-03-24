from pathlib import Path

dirpath = Path('.')
missing_files_path = dirpath / 'missing_files.txt'

if missing_files_path.exists() and missing_files_path.is_file():
    missing_files = missing_files_path.read_text(encoding='utf-8').splitlines()
    
    for file_name in missing_files:
        file_path = dirpath / file_name
        file_path.touch()
        print(f"file done: {file_path}")
else:
    print("file not found")