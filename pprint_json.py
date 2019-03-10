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

    try:
        json_format_data = load_data(filepath)
        pretty_print_json(json_format_data)
    except json.decoder.JSONDecodeError:
        print('Некорректные входные данные')
    except NameError:
        print('Не указан путь к исходному файлу')
    except FileNotFoundError:
        print('Файл не найден')
    except Exception:
        print('Что-то пошло не так...\n'
              'Попробуйте еще раз')
