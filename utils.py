import copy
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
                subsubsubdoc = subsubdoc[instanceType]
                machine = copy.deepcopy(subsubsubdoc)
                machine['region'] = region
                machine['os'] = os
                machine['instanceType'] = instanceType
                machine['major'], machine['minor'] = machine['instanceType'].split('.')
                for attr in doc['instance_types'][instanceType]:
                    machine[attr] = doc['instance_types'][instanceType][attr]
                machines.append(machine)
    return machines


def get_machines_df(json_path: str) -> pd.DataFrame:
    machines = get_raw_machines_data_from_json(json_path)

    df = pd.DataFrame(machines)
    df = df.astype({
        's': int,
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
