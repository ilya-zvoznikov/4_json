import json
import sys
import os


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data_dict):
    print(json.dumps(data_dict, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print('Не указан путь к файлу')
        sys.exit()

    try:
        data_dict = load_data(filepath)
        pretty_print_json(data_dict)
    except FileNotFoundError:
        print('Файл не найден')
    except json.decoder.JSONDecodeError:
        print('Данные не в формате JSON')
