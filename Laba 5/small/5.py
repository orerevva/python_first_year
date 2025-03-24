from pathlib import Path

# Путь к папке по умолчанию
dirpath = Path('.')

# Задаем файлы вручную
files = ["file1.txt", "file2.txt", "file3.txt"]  # Пример списка файлов

if not dirpath.exists() or not dirpath.is_dir():
    print(f"Ошибка: папка '{dirpath}' не существует или не является директорией.")
else:
    if files:
        present_files = [file for file in files if (dirpath / file).exists()]
        missing_files = [file for file in files if not (dirpath / file).exists()]
        
        (dirpath / 'present_files.txt').write_text('\n'.join(present_files), encoding='utf-8')
        (dirpath / 'missing_files.txt').write_text('\n'.join(missing_files), encoding='utf-8')
        
        print("Файлы, найденные в папке:")
        print('\n'.join(present_files) if present_files else "Нет найденных файлов.")
        print("\nФайлы, отсутствующие в папке:")
        print('\n'.join(missing_files) if missing_files else "Все файлы найдены.")
    else:
        all_files = list(dirpath.glob('*'))
        total_size = sum(f.stat().st_size for f in all_files if f.is_file())
        print(f"В папке {dirpath} файлов: {len(all_files)}, общий размер: {total_size} байт.")