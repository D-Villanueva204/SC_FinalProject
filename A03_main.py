"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "2.0.0"
__credits__ = "Dominique Villanueva"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client


# 2. Create a Client object with data of your choice.
try:
    client_one = Client(1,
                        "Doug",
                        "Mann",
                        "dog2@rrc.ca")
except ValueError as e:
    print(e)


# 3a. Create a ChequingAccount object with data of your choice, using the client_number
# of the client created in step 2.

try:
    chequing_one = ChequingAccount(12,
                                   1,
                                   3000.00,
                                   date.today,
                                   5000,
                                   3.5)
except ValueError as e:
    print(e)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number
# of the client created in step 2.


try:
    savings_one = SavingsAccount(55,
                                 1,
                                 3000.00,
                                 date.today,
                                 2000)
except ValueError as e:
    print(e)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

savings_one.attach(client_one)
chequing_one.attach(client_one)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number
# of the client created in this step.

client_two = Client(3,
                    "Kate",
                    "Pearson",
                    "catperson4@rrc.ca")

try:
    savings_two = SavingsAccount(80,
                                 3,
                                 5000.00,
                                 date.today,
                                 4000)
    savings_two.attach(client_two)
except ValueError as e:
    print(e)


# 6. Use the ChequingAccount and SavingsAccount objects created
# in steps 3 and 5 above to perform transactions (deposits and withdraws)
# which would cause the Subject (BankAccount) to notify the Observer
# (Client) as well as transactions that would not
# cause the Subject to notify the Observer.  Ensure each
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such
# that any exception messages are printed to the console.

# Deposit Error
try:
    chequing_one.withdraw(2980)
except ValueError as e:
    print(e)

try:
    chequing_one.deposit(10000)
except ValueError as e:
    print(e)

try:
    chequing_one.deposit(500)
except ValueError as e:
    print(e)


# Transaction
try:
    savings_one.deposit(3000000.00)
except ValueError as e:
    print(e)

try:
    savings_one.withdraw(3003000.00)
except ValueError as e:
    print(e)

try:
    savings_one.deposit(500.00)
except ValueError as e:
    print(e)


try:
    savings_two.deposit(10500.00)
except ValueError as e:
    print(e)

try:
    savings_two.withdraw(15470.00)
except ValueError as e:
    print(e)

try:
    savings_two.deposit(90.00)
except ValueError as e:
    print(e)
