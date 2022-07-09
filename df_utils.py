import json
import pandas as pd

NOT_FOUND_INSTANCE_PRICE = 100000  # the instance is not available, therefore - high price


def get_spot_instances_df(spot_advisor_json_path: str, spot_price_json_path: str) -> pd.DataFrame:
    instances_raw_date = get_raw_spot_advisor_data(spot_advisor_json_path)

    spot_price_data = json.load(open(spot_price_json_path))

    for instance in instances_raw_date:
        instance['spot_price_per_hour'] = calculate_spot_instance_price(spot_price_data,
                                                                        instance['region'],
                                                                        instance['instanceType'],
                                                                        instance['os'])

    df = pd.DataFrame(instances_raw_date)
    return df.astype({
        'interruption_rate': int,
        'spot_price_per_hour': float,
        'discount': int,
        'region': 'category',
        'os': 'category',
        'instanceType': 'category',
        'ram_gb': int,
        'emr': bool,
        'cores': int,
        'major': 'category',
        'minor': 'category',
    })


def get_raw_spot_advisor_data(json_path: str) -> list:
    doc = json.load(open(json_path))
    instances = []
    for region in doc['spot_advisor']:
        subdoc = doc['spot_advisor'][region]
        for os in subdoc:
            subsubdoc = subdoc[os]
            for instanceType in subsubdoc:
                major, minor = instanceType.split('.')

                subsubsubdoc = subsubdoc[instanceType]

                instance = {
                    'interruption_rate': subsubsubdoc['r'],
                    'discount': subsubsubdoc['s'],
                    'region': region,
                    'os': os,
                    'instanceType': instanceType,
                    'major': major,
                    'minor': minor
                }

                for attr in doc['instance_types'][instanceType]:
                    instance[attr] = doc['instance_types'][instanceType][attr]

                instances.append(instance)
    return instances


def calculate_spot_instance_price(spot_price_data: dict, region: str, type_name: str, os: str) -> float:
    try:
        spot_price = spot_price_data[region][type_name][os]
    except KeyError:
        return NOT_FOUND_INSTANCE_PRICE

    if spot_price != "N/A*":
        return float(spot_price)
    else:
        return NOT_FOUND_INSTANCE_PRICE
