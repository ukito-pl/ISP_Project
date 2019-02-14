import json


def clean_json():
    d = {"cols": [{"id": "", "label": "Number of sample", "pattern": "", "type": "number"},
                  {"id": "", "label": "Position", "pattern": "", "type": "number"}],
         #"rows": [{"c": [{"v": 0, "f": None}, {"v": 0, "f": None}]}]}
         "rows": []}

    actual_data = d

    with open('chart_data.json', 'w') as f:
        json.dump(actual_data, f)


if __name__ == "__main__":
    clean_json()

