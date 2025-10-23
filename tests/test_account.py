from lib.account import Account

def test_account_details_initialised():

    account = Account(1, "test@email.com", "test user")

    assert account.id == 1
    assert account.email == "test@email.com"
    assert account.username == "test user"

def test_account_equality():

    account1 = Account(1, "test@email.com", "test user")
    account2 = Account(1, "test@email.com", "test user")

    assert account1 == account2

def test_account_formatting():

    account = Account(1, "test@email.com", "test user")

    assert str(account) == "Account(1, test@email.com, test user)"