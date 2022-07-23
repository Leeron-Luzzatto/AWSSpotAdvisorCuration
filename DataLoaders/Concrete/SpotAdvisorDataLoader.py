from DataLoaders.Abstract.AbstractAwsDataLoader import AbstractAwsDataLoader


class SpotAdvisorDataLoader(AbstractAwsDataLoader):
    url = 'https://spot-bid-advisor.s3.amazonaws.com/spot-advisor-data.json'
    data_files_folder = r'data/SpotAdvisor'
    data_file_name_format = 'spot-advisor-data-{date}.json'
