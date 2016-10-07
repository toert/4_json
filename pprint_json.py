import json


def load_data(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as data:
        return json.load(data) 


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    filepath_to_json = input('Enter filepath to your json: ')
    text_from_file = load_data(filepath_to_json)
    pretty_print_json(text_from_file)
