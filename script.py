import os
import time

def size_format(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def list_files(path):
    print()
    files = sorted(os.listdir(path))

    for file in files:
        full_path = os.path.join(path, file)
        is_dir = os.path.isdir(full_path)
        size = os.path.getsize(full_path) if not is_dir else 0
        modified_time = time.strftime('%d/%m/%Y %H:%M', time.localtime(os.path.getmtime(full_path)))
        print(f"{file.ljust(30)} {'<DIR>' if is_dir else size_format(size).rjust(10)} {modified_time}")
    
    print('', end='')

def main():
    list_files(os.getcwd())

if __name__ == "__main__":
    main()
