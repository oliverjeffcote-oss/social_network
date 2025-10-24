from lib.account_repository import AccountRepository
from lib.account import Account


'''
Given user accounts in the db
account_repository.all() returns all user accounts
'''

def test_all_returns_user_accounts(db_connection):

    repo = AccountRepository(db_connection)

    assert repo.all() == [
        Account(1, 'elliot.smith@example.com', 'ElliotS'),
        Account(2, 'joan.baez@example.com', 'JoanB'),
        Account(3, 'kendrick.lamar@example.com', 'KDot'),
        Account(4, 'daft.punk@example.com', 'DPunk')
    ]