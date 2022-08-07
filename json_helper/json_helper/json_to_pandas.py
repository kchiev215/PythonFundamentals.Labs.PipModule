import json
import pandas as pd
import os


def read_json(file_name):
    with open(file_name, 'r') as f:
        json_object = json.load(f)
    return json_object


def read_all_json_files(JSON_ROOT):
    for direpath, direnames, filenames in os.walk(JSON_ROOT):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content_2 = read_json(os.path.join(JSON_ROOT, f))
                for i in json_content_2["results"]:
                    i["source"] = f
                    result.append(i)
        df_loc = pd.DataFrame(result)
        return df_loc


df_daily_summaries = read_all_json_files('./data/daily_summaries')
