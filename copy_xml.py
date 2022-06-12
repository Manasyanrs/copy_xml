import xml.etree.ElementTree as etree
import os
import shutil


source_path = ""
destination_path = ""
file_name = ""

try:
    tree = etree.parse('config.xml')
    root = tree.getroot()

    for element in root:
        try:
            for key, value in element.items():
                if key == "source_path" and os.path.exists(value):
                    source_path = value
                elif key == "destination_path" and os.path.exists(value):
                    destination_path = value
                elif key == "file_name":
                    file_name = value
                else:
                    source_path = value
                    raise FileNotFoundError
            shutil.copytree(source_path, destination_path + "\\" + file_name)
        except FileNotFoundError as f:
            print("Системе не удалось найти директорию", source_path)
        except FileExistsError as e:
            print("Невозможно создать файл, так как он уже существует:")
except FileNotFoundError as error:
    print(error)
else:
    print("Копирование файлов завершено")
