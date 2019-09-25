import csv
import json


def load_test_data_json(json_key_first_level, json_key_second_level):
    with open("C:/Users/mi/sdelka_autotest/data_test/generated_test_data.json", 'r', encoding='utf-8') as File:
        data = json.load(File)
    return data[json_key_first_level][json_key_second_level]
