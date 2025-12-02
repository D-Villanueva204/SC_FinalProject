"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.2.1"
__credits__ = "Dominique Villanueva"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from bank_account import *
from datetime import date, datetime


# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.

chequing_account = None

try:
    chequing_account = ChequingAccount(43,
                                       1,
                                       1500,
                                       datetime(2025, 1, 1).date(),
                                       2000,
                                       1.5)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.

print(chequing_account)

print(f"Service Charges: {chequing_account.get_service_charges()}")


# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.

try:

    chequing_account.deposit(2000)
    print(chequing_account)
    print(f"Service Charges: {chequing_account.get_service_charges()}")
except ValueError as e:
    print(e)

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.

savings_account = None

try:
    savings_account = SavingsAccount(33,
                                     2,
                                     3000.00,
                                     datetime(2024, 11, 15).date(),
                                     1500)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.

print(savings_account)
print(f"Service Charges: {savings_account.get_service_charges()}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.

try:
    savings_account.withdraw(2000)
    print(savings_account)
    print(f"Service Charges: {savings_account.get_service_charges()}")
except ValueError as e:
    print(e)

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.

investment_account = None

try:
    investment_account = InvestmentAccount(8585,
                                           3,
                                           2000,
                                           datetime(2025, 1, 1).date(),
                                           30.00)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.

print(investment_account)
print(f"Service Charges: {investment_account.get_service_charges()}")

# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.

second_investment_account = None

try:
    second_investment_account = InvestmentAccount(8585,
                                                  3,
                                                  2000,
                                                  datetime(2005, 1, 1).date(),
                                                  30.00)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.

print(second_investment_account)
print(f"Service Charges: {second_investment_account.get_service_charges()}")


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.

bank_accounts = {chequing_account,
                 savings_account,
                 investment_account,
                 second_investment_account}
try:
    for bank_account in bank_accounts:
        bank_account.withdraw(bank_account.get_service_charges())
except ValueError as e:
    print(e)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

for bank_account in bank_accounts:
    print(bank_account)