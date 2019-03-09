import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def pretty_print_json(json_file):
    print(json.dumps(json_file, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'alco_shops.json'

    alco_shops_json_file = load_data(filepath)
    pretty_print_json(alco_shops_json_file)
