# CS111 -- starter file for dataclasses, updates, and memory

from dataclasses import dataclass

@dataclass
class Post:
    by: str
    # num_likes: int
    who_likes: list # usernames of likes
    content: str

post1 = Post("Andrew", [], "project released")

def like_post(p: Post, username: str):
    """record that given username liked the given post"""

    

# ==================================

@dataclass
class Account:
    id_num: int
    balance: float

acct1 = Account(8200, 150)
acct2 = Account(8201, 300)
# list of all the accounts
all_accounts = [acct1, acct2, Account(8202, 250)] 

def deposit(to_acct: Account, amt: float):
    """add the given amt to the account balance"""
    to_acct.balance = to_acct.balance + amt

def withdraw(from_acct: Account, amt: float):
    """withdraw the given amt from the account balance if there are enough funds"""
    if amt > from_acct.balance:
        raise ValueError("Not enough funds")
    from_acct.balance = from_acct.balance - amt
    

pass