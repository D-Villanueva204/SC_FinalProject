"""
Description: Unit tests for the ChequingAccount class.
Author: Dominique Villanueva
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py

"""

__author__ = "Dominique Villanueva"
__version__ = "1.0.4"

import unittest
from datetime import date, datetime
from bank_account import *


class ChequingAccountTests(unittest.TestCase):

    def setUp(self):
        test_date = datetime(2025, 1, 1).date()

        self.chequing_account = ChequingAccount(101,
                                                3116553,
                                                5000.00,
                                                test_date,
                                                3000,
                                                0.25)

    def test_init_valid_args_attributes_set(self):
        test = self.chequing_account
        test_date = datetime(2025, 1, 1).date()

        self.assertEqual(101, test._BankAccount__account_number)

        self.assertEqual(
            3116553, test._BankAccount__client_number)

        self.assertEqual(5000.00, test._BankAccount__balance)

        self.assertEqual(
            test_date, test._date_created)

        self.assertEqual(
            3000, test._ChequingAccount__overdraft_limit)

        self.assertEqual(
            0.25, test._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_correct_return(self):
        test_date = datetime(2025, 1, 1).date()
        test = ChequingAccount(101,
                               3116553,
                               5000.00,
                               test_date,
                               "threethousand",
                               0.25)
        self.assertEqual(
            -100.00, test._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate_correct_return(self):
        test_date = datetime(2025, 1, 1).date()
        test = ChequingAccount(101,
                               3116553,
                               5000.00,
                               test_date,
                               3000,
                               "25%")
        self.assertEqual(
            0.05, test._ChequingAccount__overdraft_rate)

    def test_init_invalid_data_created_correct_return(self):
        test = ChequingAccount(101,
                               3116553,
                               5000.00,
                               "TODAY",
                               3000,
                               0.25)
        self.assertEqual(
            date.today(), test._date_created)

    def test_get_service_charges_greater_balance_correct_return(self):
        test = self.chequing_account
        expected = 0.50

        self.assertEqual(expected, test.get_service_charges())

    def test_get_service_charges_lesser_balance_correct_return(self):
        expected = 1000.5
        test_date = datetime(2025, 1, 1).date()
        test = ChequingAccount(101,
                               3116553,
                               5000.00,
                               test_date,
                               9000,
                               0.25)

        self.assertEqual(expected, test.get_service_charges())

    def test_str_correct_return(self):
        self.assertEqual("Account Number: 101 Balance: $5,000.00\n"
                         "Overdraft Limit: $3000.0 "
                         "Overdraft Rate: 25.00% "
                         "Account Type: Chequing", str(self.chequing_account))
