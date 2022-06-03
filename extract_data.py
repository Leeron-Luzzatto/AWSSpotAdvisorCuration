from datetime import date
from urllib import request
import os

DATA_FOLDER_PATH = 'data'
SPOT_ADVISOR_URL = 'https://spot-bid-advisor.s3.amazonaws.com/spot-advisor-data.json'


def main():
    print(f"searching for a new data file in {SPOT_ADVISOR_URL}")
    with request.urlopen(SPOT_ADVISOR_URL) as response:
        new_data = response.read().decode('utf-8')

        if not data_exists(new_data):
            with open(f'data/spot-advisor-data-{date.today()}.json', 'w') as new_data_file:
                new_data_file.write(new_data)
            print("new data file was added successfully")
        else:
            print("no new data file was found")


def data_exists(data: str) -> bool:
    for file_name in os.listdir(DATA_FOLDER_PATH):
        with open(os.path.join(DATA_FOLDER_PATH, file_name), 'r') as data_file:
            if data_file.read() == data:
                return True

    return False


if __name__ == '__main__':
    main()
