from lib.account_repository import AccountRepository
from lib.account import Account

'''
Given user accounts in the db
account_repository.all() returns all user accounts
'''

def test_all_returns_user_accounts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = AccountRepository(db_connection)

    assert repo.all() == [
        Account(1, 'elliot.smith@example.com', 'ElliotS'),
        Account(2, 'joan.baez@example.com', 'JoanB'),
        Account(3, 'kendrick.lamar@example.com', 'KDot'),
        Account(4, 'daft.punk@example.com', 'DPunk')
    ]

def test_find_returns_one_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = AccountRepository(db_connection)

    assert repo.find(2) == Account(2, 'joan.baez@example.com', 'JoanB')

def test_create_new_account(db_connection):

    db_connection.seed("seeds/social_network.sql")
    repo = AccountRepository(db_connection)

    assert repo.create(Account(None, 'james.dean@example.com', 'JamesD')) == None
    assert repo.find(5) == Account(5,'james.dean@example.com', 'JamesD')
