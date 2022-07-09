from DataLoaders.Abstract.AbstractAwsDataLoader import AbstractAwsDataLoader


class SpotPriceDataLoader(AbstractAwsDataLoader):
    url = 'http://spot-price.s3.amazonaws.com/spot.js'
    data_files_folder = r'data\SpotPrice'
    data_file_name_format = 'spot-price-data-{date}.json'

    @staticmethod
    def transform_response(response: str):
        return response.lstrip('callback(').rstrip(');')
