from datetime import date
from urllib import request
import os

from abc import ABC, abstractmethod, abstractproperty


class AbstractAwsDataLoader(ABC):
    @property
    @abstractmethod
    def url(self):
        pass

    @property
    @abstractmethod
    def data_files_folder(self):
        pass

    @property
    @abstractmethod
    def data_file_name_format(self):
        pass

    def fetch(self):
        print(f"searching for a new data file in {self.url}")
        with request.urlopen(self.url) as response:
            response = response.read().decode('utf-8')

            new_data = self.__class__.transform_response(response)

        if not self.__data_exists(new_data):
            new_data_file_path = os.path.join(self.data_files_folder,
                                              self.data_file_name_format.format(date=date.today()))

            with open(new_data_file_path, 'w') as new_data_file:
                new_data_file.write(new_data)

            print(f"new data file was added successfully: {new_data_file_path}")

        else:
            print(f"no new data file was found in {self.url}")

    @staticmethod
    def transform_response(response: str):
        return response

    def __data_exists(self, data: str) -> bool:
        for file_name in os.listdir(self.data_files_folder):
            with open(os.path.join(self.data_files_folder, file_name), 'r') as data_file:
                if data_file.read() == data:
                    return True

        return False
