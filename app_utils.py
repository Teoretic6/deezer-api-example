import json
from datetime import datetime


def read_json(filename: str) -> dict:
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    return data


def write_json(filename: str, data: dict) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_listening_history(deezer, url_to_get):
    all_history = []
    is_next = True

    try:
        while is_next:
            result = deezer.get(url_to_get).json()

            data = result['data']
            all_history += data

            is_next = 'next' in result
            if is_next:
                url_to_get = result['next']
    except Exception as e:
        print('While loading history exception has occurred! {}'.format(e))

    return all_history


def write_history_to_file(all_data) -> None:
    history_filename = 'deezer_history{}.json'.format(datetime.now().strftime('%d_%m_%Y'))
    dict_to_write = {
        "data": all_data
    }
    write_json(history_filename, dict_to_write)