import os
import pathlib

dir_path = input('Enter a directory path: ')

file_extension = [".py"]
content = ""
for address, dirs, files in os.walk(dir_path):
    for file in files:
        ex = pathlib.Path(file).suffix
        if ex not in file_extension:
            continue

        with open(os.path.join(address, file), encoding="utf-8") as f:
            content += f.read() + "\n"

with open("result.py", "w") as file:
    file.write(content)


