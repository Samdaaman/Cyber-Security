import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
con = sqlite3.connect('./secuchat.db')
cur = con.cursor()


def print_db():
    print('users = [')
    rows = cur.execute(f'SELECT * from User').fetchall()
    for row in rows:
        print(f"    ('{row[0]}','{row[1].hex()}'),")
    print(']\n')

    print('parameters = [')
    rows = cur.execute(f'SELECT * from Parameters').fetchall()
    for row in rows:
        print(f"    ({row[0]},'{row[1].hex()}','{row[2].hex()}','{row[3].hex()}'),")
    print(']\n')

    print('conversations = [')
    rows = cur.execute(f'SELECT * from Conversation').fetchall()
    for row in rows:
        print(f"    ({row[0]},'{row[1]}','{row[2]}',{row[3]}),")
    print(']\n')

    print('messages = [')
    rows = cur.execute(f'SELECT * from Message').fetchall()
    for row in rows:
        print(f"    ({row[0]},{row[1]},{row[2]},{row[3]},'{row[4].hex()}'),")
    print(']\n')


def main():
    tables = ['User', 'Parameters', 'Conversation', 'Message']

    # for table in tables:
    #     res = list(cur.execute(f'SELECT * from {table} LIMIT 5'))
    #     print(res)

    




if __name__ == '__main__':
    print_db()
    
    con.close()