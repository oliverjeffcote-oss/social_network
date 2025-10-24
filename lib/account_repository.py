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
    
    def find(self, id):
        accounts = self._connection.execute('SELECT * FROM accounts WHERE id = %s',[id])
        account = accounts[0]
        print(account)
        return Account(account['id'], account['email_address'], account['username'])
    
    def create(self, account):
        self._connection.execute('INSERT INTO accounts (email_address, username) VALUES (%s, %s)',
                                 [account.email, account.username])
        return None