from client.client import Client
import logging
from datetime import date, datetime
import csv
__author__ = "ACE Faculty"
__version__ = "2.2.6"
__credits__ = "Dominique Villanueva"

import os
import sys

from bank_account import *
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE

# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))

# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')

# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')

# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')

# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')

# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************


def load_data() -> tuple[dict, dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.

    Returns:
        tuple containing client dictionary and account dictionary.

    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        error_message = f"Unable to create client: "
        for row in reader:
            try:
                client_number = int(row['client_number'])
                first_name = str(row['first_name'])
                last_name = str(row['last_name'])
                email_address = str(row['email_address'])
                client = Client(client_number,
                                first_name,
                                last_name,
                                email_address)
                client_listing[client_number] = client
            except ValueError as e:
                logging.error(f"{error_message}" +
                              f"{e}")
    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        BANK_ACCOUNT_TYPES = ['ChequingAccount',
                              'SavingsAccount',
                              'InvestmentAccount']
        error_message = f"Bank Account: "
        for row in reader:
            account = None
            try:
                account_number = int(row['account_number'])
                client_number = int(row['client_number'])
                balance = float(row['balance'])
                account_type = row['account_type']
                try:
                    converted_date = datetime.strptime(
                        (row['date_created']), "%Y-%m-%d").date()
                    date_created = converted_date
                except Exception as e:
                    raise ValueError("Invalid Date Format")

                if client_number not in client_listing:
                    raise ValueError(
                        f" {account_number} contains invalid Client Number")

                if account_type == BANK_ACCOUNT_TYPES[0]:
                    overdraft_limit = row['overdraft_limit']
                    overdraft_rate = row['overdraft_rate']
                    account = ChequingAccount(account_number,
                                              client_number,
                                              balance,
                                              date_created,
                                              overdraft_limit,
                                              overdraft_rate)

                if account_type == BANK_ACCOUNT_TYPES[1]:
                    minimum_balance = row['minimum_balance']
                    account = SavingsAccount(account_number,
                                             client_number,
                                             balance,
                                             date_created,
                                             minimum_balance)
                if account_type == BANK_ACCOUNT_TYPES[2]:
                    management_fee = row['management_fee']
                    account = InvestmentAccount(account_number,
                                                client_number,
                                                balance,
                                                date_created,
                                                management_fee)

                if account_type not in BANK_ACCOUNT_TYPES:
                    raise ValueError("Not a valid account type.")
                else:
                    account.attach(client_listing[client_number])
                    accounts[account_number] = account
            except ValueError as e:
                logging.error(f"{error_message}" +
                              f"{e}")

        # RETURN STATEMENT
        return (client_listing, accounts)


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.

    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
        
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")
