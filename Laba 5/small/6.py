from pathlib import Path

# Указываем путь к папке и файлу со списком отсутствующих файлов
dirpath = Path('.')
missing_files_path = dirpath / 'missing_files.txt'

# Проверяем существование файла со списком отсутствующих файлов
if missing_files_path.exists() and missing_files_path.is_file():
    missing_files = missing_files_path.read_text(encoding='utf-8').splitlines()
    
    for file_name in missing_files:
        file_path = dirpath / file_name
        file_path.touch()
        print(f"Создан файл: {file_path}")
else:
    print("Файл со списком отсутствующих файлов не найден.")