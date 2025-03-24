from pathlib import Path

directory = Path('.')  

if not directory.exists() or not directory.is_dir():
    print(f"ERROR'{directory}' not found")
else:
    small_files = [file for file in directory.iterdir() if file.is_file() and file.stat().st_size < 2048]
    
    if small_files:
        small_dir = directory / "small"
        small_dir.mkdir(exist_ok=True)
        
        print("file:")
        for file in small_files:
            print(file.name)
            (small_dir / file.name).write_bytes(file.read_bytes())
        
        print(f"all files copy in  '{small_dir}'")
    else:
        print("files < 2K not found")
