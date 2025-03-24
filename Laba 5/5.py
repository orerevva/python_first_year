from pathlib import Path

dirpath = Path('.')

files = ["input.txt", "input_2.txt", "file1.txt"]

if not dirpath.exists() or not dirpath.is_dir():
    print(f"ERROR'{dirpath}' not found")
else:
    if files:
        present_files = [file for file in files if (dirpath / file).exists()]
        missing_files = [file for file in files if not (dirpath / file).exists()]
        
        (dirpath / 'present_files.txt').write_text('\n'.join(present_files), encoding='utf-8')
        (dirpath / 'missing_files.txt').write_text('\n'.join(missing_files), encoding='utf-8')
        
        print("files found in the folder")
        print('\n'.join(present_files) if present_files else "No files found.")
        print("\nfiles not found in the folder ")
        print('\n'.join(missing_files) if missing_files else "all files found")
    else:
        all_files = list(dirpath.glob('*'))
        total_size = sum(f.stat().st_size for f in all_files if f.is_file())
        print(f"in folder {dirpath} files: {len(all_files)}, size: {total_size} ")