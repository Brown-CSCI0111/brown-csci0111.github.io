from dataclasses import dataclass

@dataclass
class Account:
    id_num: int
    balance: float

@dataclass
class Customer:
    name: str
    acct: Account

all_accts = [Account(8404, 120), Account(8405, 200), Account(8406, 250), Account(2407, 150)]

def find_account(num: int) -> Account:
    """find the account with the given id number from the list"""
    for acct in all_accts:
        if acct.id_num == num:
            return acct
    raise ValueError("no account with that number")

pass