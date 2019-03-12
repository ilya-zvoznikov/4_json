import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data_object):
    print(json.dumps(data_object, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        sys.exit('Не указан путь к файлу')

    try:
        data_object = load_data(filepath)
        pretty_print_json(data_object)
    except FileNotFoundError:
        print('Файл не найден')
    except json.decoder.JSONDecodeError:
        print('Данные не в формате JSON')
