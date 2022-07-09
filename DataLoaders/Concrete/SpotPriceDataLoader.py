import json

from DataLoaders.Abstract.AbstractAwsDataLoader import AbstractAwsDataLoader


class SpotPriceDataLoader(AbstractAwsDataLoader):
    url = 'http://spot-price.s3.amazonaws.com/spot.js'
    data_files_folder = r'data\SpotPrice'
    data_file_name_format = 'spot-price-data-{date}.json'

    @staticmethod
    def transform_response(response: str):
        json_string = response.lstrip('callback(').rstrip(');')
        raw_prices_data = json.loads(json_string)

        cooked_price_data = {}

        for region_section in raw_prices_data['config']['regions']:
            region_name = region_section['region']
            cooked_price_data[region_name] = {}

            for type_section in region_section['instanceTypes']:
                for size_section in type_section['sizes']:
                    instance_type = size_section['size']
                    cooked_price_data[region_name][instance_type] = {}

                    for os_section in size_section['valueColumns']:
                        os_name = os_section['name']
                        if os_name == 'linux':
                            os_name = 'Linux'
                        elif os_name == 'mswin':
                            os_name = 'Windows'

                        cooked_price_data[region_name][instance_type][os_name] = os_section['prices']['USD']

        return json.dumps(cooked_price_data)


