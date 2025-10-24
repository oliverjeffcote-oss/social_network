from lib.account import Account

class AccountRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):

        rows = self._connection.execute('SELECT * FROM accounts')

        accounts = []

        for row in rows:
            item = Account(row["id"], row["email_address"], row["username"])
            accounts.append(item)

        return accounts