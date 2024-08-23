import asyncio
import csv
import logging
import os
import statistics

import uvicorn
from fastapi import FastAPI

# from init_app import run_dolos_validation
import init_app
from models import User, Coefficient, TableItem, TableUser

app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     await init_app.run_dolos_validation()


def get_username(path: str) -> str:
    return path.rpartition("/")[2].partition(".")[0]


def get_data_files(base_dir: str) -> list[str]:
    paths = []
    for root, dirs, files in os.walk(base_dir):
        file_path = os.path.join(root, "pairs.csv")

        logging.info(f"[{file_path}] started")
        if not os.path.exists(file_path):
            logging.error(f"File {file_path} does not exist")
            continue

        paths.append(file_path)

    return paths


@app.get("/get/all_users")
async def get_users() -> list[User]:
    path = os.path.join(os.getcwd(), "sample", "Python", "results")
    files = get_data_files(path)
    users = {}

    for file_path in files:

        with open(file_path, "r") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                for i in (2, 4):
                    username = get_username(row[i])
                    coefficient = float(row[5])

                    user_coefficients = users.get(username)
                    if user_coefficients is None:
                        user_coefficients = set()

                    user_coefficients.add(coefficient)
                    users[username] = user_coefficients

    result_users = []
    for username, coefficients in users.items():
        result_users.append(User(
            name=username,
            level=1,
            average_coefficient=statistics.mean(coefficients),
            maximum_coefficient=max(coefficients),
            median_coefficient=statistics.median(coefficients),
        ))

    return result_users


@app.get("/get/user/{user_name}")
async def say_hello(user_name: str) -> TableUser:
    path = os.path.join(os.getcwd(), "sample", "Python", "results")

    homeworks = list(os.walk(path))[0][1]
    data_table = {}
    for hm_id, homework in enumerate(homeworks):
        with open(os.path.join(path, homework, "pairs.csv"), "r") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                user_positions = (2, 4)
                for user_position in user_positions:
                    username = get_username(row[user_position])

                    if username != user_name:
                        continue

                    pair_username = get_username(row[user_positions[user_position == 2]])
                    if not data_table.get(pair_username):
                        data_table[pair_username] = [0 for _ in range(len(homeworks))]

                    data_table[pair_username][hm_id] = float(row[5])

    table = TableUser(
        name=user_name,
        table=[
            TableItem(
                name=username,
                coefficients=[
                    Coefficient(
                        homework_id=hm_id,
                        coefficient=coefficient,
                    ) for hm_id, coefficient in enumerate(homeworks)
                ],
            ) for username, homeworks in data_table.items()
        ],
    )
    table.table.sort(key=lambda x: sum([c.coefficient for c in x.coefficients]), reverse=True)

    return table


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
