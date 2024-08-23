import asyncio
import io
import os
import pathlib
import zipfile

from dolos_api import DolosAPI


def create_zip_binary(folder_path):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(".csv"):
                    continue
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)

    zip_buffer.seek(0)

    return zip_buffer.getvalue()


async def process_homework(dolos, homework, subject_path, base_results_dir, programming_language):
    print(f"[{homework}] started")

    zipfile_object = create_zip_binary(subject_path.joinpath(homework))

    in_hw_results_dir = subject_path.joinpath(f"{homework}/results")
    in_hw_results_dir.mkdir(exist_ok=True)

    base_hw_results_dir = base_results_dir.joinpath(homework)
    base_hw_results_dir.mkdir(exist_ok=True)

    report = await dolos.submit_report(homework,
                                       zipfile_object,
                                       programming_language)

    report_status = "queued"

    while report_status != "finished":
        report_info = await dolos.get_report_info(report["id"])

        report_status = report_info["status"]
        print(f"[{homework}] status:", report_status)

        if report_status == "failed":
            print(report_info["stderr"])

        if report_status == "error":
            print(report_info["error"])

        await asyncio.sleep(1)

    csv_names = ["metadata", "files", "kgrams", "pairs"]

    for csv_name in csv_names:
        csv_file = await dolos.get_report_data(report["id"],
                                               csv_name)

        with open(in_hw_results_dir.joinpath(f"{csv_name}.csv"), "wb") as file:
            file.write(csv_file)

        with open(base_hw_results_dir.joinpath(f"{csv_name}.csv"), "wb") as file:
            file.write(csv_file)

    print(f"[{homework}] results saved to:", in_hw_results_dir)
    print(f"[{homework}] results saved to:", base_hw_results_dir)


async def main():
    dolos = DolosAPI()

    subject_path = pathlib.Path(os.path.join(os.getcwd(), "sample", "Python"))
    programming_language = "python"

    base_results_dir = subject_path.joinpath("results")
    base_results_dir.mkdir(exist_ok=True)

    homeworks = list(os.walk(subject_path))[0][1]

    homeworks.remove("results")

    await asyncio.gather(
        *[process_homework(dolos, homework, subject_path, base_results_dir, programming_language)
          for homework in homeworks]
    )

    await dolos.close()


asyncio.run(main())
