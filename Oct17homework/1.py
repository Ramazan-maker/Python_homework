import os

def walk_directory_tree(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            yield os.path.join(root, file)

# Пример использования:
for file_path in walk_directory_tree('C:/Users/Рамазан/Documents/GitHub/Python_homework'):
    print(file_path)

