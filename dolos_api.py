import aiohttp


class DolosAPI:
    BASE_URL = "http://localhost:3000"

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def submit_report(self,
                            name: str,
                            zipfile_object: str | bytes,
                            programming_language: str = "") -> dict:
        """
        Submit a ZIP-file to the Dolos API for plagiarism detection and return the report details.

        :param name: The name of the dataset.
        :param zipfile_object: Bytes ZIP-file object or path to the ZIP-file to be submitted.
        :param programming_language: (Optional) Programming language of the submissions.
        :return: A dictionary containing the report details including the 'html_url'.
        """
        if isinstance(zipfile_object, str):
            zipfile_object = open(zipfile_object, "rb")

        data = {
            'dataset[name]': name,
            'dataset[programming_language]': programming_language,
            'dataset[zipfile]': zipfile_object
        }

        async with self.session.post(url=f'{self.BASE_URL}/reports',
                                     data=data) as response:
            response.raise_for_status()
            return await response.json()

    async def get_report_info(self, report_id: str) -> dict:
        """
        Retrieve the status and information of a specific report.

        :param report_id: The unique identifier of the report.
        :return: A dictionary containing the report information.
        """
        async with self.session.get(f'{self.BASE_URL}/reports/{report_id}') as response:
            response.raise_for_status()
            return await response.json()

    async def get_report_data(self,
                              report_id: str,
                              file_type: str) -> bytes:
        """
        Retrieve specific report data (metadata, files, kgrams, pairs).

        :param report_id: The unique identifier of the report.
        :param file_type: The type of report data to retrieve ('metadata', 'files', 'kgrams', 'pairs').
        :return: The URL to the report data file.
        """
        async with self.session.get(f'{self.BASE_URL}/reports/{report_id}/data/{file_type}.csv') as response:
            if response.status == 200:
                return await response.content.read()

            response.raise_for_status()

    async def delete_report(self,
                            report_id: str) -> None:
        """
        Delete a specific report and its corresponding dataset files.

        :param report_id: The unique identifier of the report.
        """
        async with self.session.delete(f'{self.BASE_URL}/reports/{report_id}') as response:
            if response.status != 204:
                response.raise_for_status()

    async def close(self):
        """Close the aiohttp session."""
        await self.session.close()
