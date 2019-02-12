import random
import time


def example_data():
    d = {"cols": [{"id": "", "label": "Nazwa Osi X", "pattern": "", "type": "number"},
                  {"id": "", "label": "Funkcja 1", "pattern": "", "type": "number"}],
         "rows": [{"c": [{"v": 0, "f": None}, {"v": 0, "f": None}]}]}

    # Random datas
    for i in range(5):
        time.sleep(1)
        example_row = {"c": [{"v": i, "f": None}, {"v": random.randint(1,10), "f": None}]}
        d['rows'].append(example_row)
    return d
