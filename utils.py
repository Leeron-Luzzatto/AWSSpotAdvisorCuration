import json
import pandas as pd


def get_raw_machines_data_from_json(json_path: str) -> list:
    doc = json.load(open(json_path))
    machines = []
    for region in doc['spot_advisor']:
        subdoc = doc['spot_advisor'][region]
        for os in subdoc:
            subsubdoc = subdoc[os]
            for instanceType in subsubdoc:
                major, minor = instanceType.split('.')

                subsubsubdoc = subsubdoc[instanceType]

                machine = {
                    'interruption_rate': subsubsubdoc['r'],
                    'discount': subsubsubdoc['s'],
                    'region': region,
                    'os': os,
                    'instanceType': instanceType,
                    'major': major,
                    'minor': minor
                }

                for attr in doc['instance_types'][instanceType]:
                    machine[attr] = doc['instance_types'][instanceType][attr]

                machines.append(machine)
    return machines


def get_machines_df(json_path: str) -> pd.DataFrame:
    machines = get_raw_machines_data_from_json(json_path)

    df = pd.DataFrame(machines)
    df = df.astype({
        'interruption_rate': int,
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

    return df
