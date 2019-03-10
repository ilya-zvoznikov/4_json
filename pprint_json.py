import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_file):
    print(json.dumps(json_file, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    filepath = sys.argv[1] if (len(sys.argv) > 1) else None
    try:
        json_data = load_data(filepath)
        pretty_print_json(json_data)
    except FileNotFoundError:
        print('Файл не найден')
    except json.decoder.JSONDecodeError:
        print('Данные не в формате JSON')
