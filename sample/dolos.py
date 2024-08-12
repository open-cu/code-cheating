import os

base_command = 'docker run --init -v "$PWD:/dolos" ghcr.io/dodona-edu/dolos-cli -l python -f csv '

tasks_folder = input("tasks folder: ")
task_name = input("task name: ")

os.system(base_command + f"{tasks_folder}/{task_name}/*.py")
