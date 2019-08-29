import csv
from collections import defaultdict
# TODO: подумать, как сделать загрузку данных единожды в сессию


def load_test_data():
    columns = defaultdict(list)
    with open("C:/Users/mi/sdelka_autotest/data_test/address_form.csv", encoding='utf-8') as File:
        reader = csv.DictReader(File)
        # read a row as {column1: value1, column2: value2,...}
        for row in reader:
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)
    return columns
