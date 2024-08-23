import os
import random
import pathlib

from faker import Faker
import csv

fake = Faker()

users = [fake.name().replace(" ", "_") for i in range(100)]
fieldnames = [
    "id",
    "leftFileId",
    "leftFilePath",
    "rightFileId",
    "rightFilePath",
    "similarity",
    "totalOverlap",
    "longestFragment",
    "leftCovered",
    "rightCovered",
]

base_row = [93, 2, "", 1, "", 0, 15, 7, 8, 7]
os.chdir(r"C:\Users\p6282\Desktop\my_projects\web\code-cheating\back\sample\Python\results")
for hw in range(15):
    path = os.getcwd()
    if not os.path.exists(os.path.join(path, f"HW_{hw}")):
        os.mkdir(os.path.join(path, f"HW_{hw}"))

    hw_path = os.path.join(path, f"HW_{hw}", "pairs.csv")

    with open(hw_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        rows = [fieldnames]
        for user1 in users:
            for user2 in users:
                row = base_row.copy()
                row[2] = f"/tmp/amogus/{user1}.py"
                row[4] = f"/tmp/amogus/{user2}.py"
                row[5] = random.random()
                rows.append(row)

        writer.writerows(rows)
