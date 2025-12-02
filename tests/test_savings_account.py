"""
Description: Unit tests for the SavingsAccount class.
Author: Dominique Villanueva
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
    
"""

__author__ = "Dominique Villanueva"
__version__ = "1.0.0"

import unittest
from datetime import datetime
from bank_account import *


class SavingsAccountTests(unittest.TestCase):

    def setUp(self):

        test_date = datetime(2025, 1, 1).date()

        self.savings_account = SavingsAccount(101,
                                              3116553,
                                              5000.00,
                                              test_date,
                                              4000.00)

    def test_init_valid_args_attributes_set(self):
        test = self.savings_account
        test_date = datetime(2025, 1, 1).date()

        self.assertEqual(
            101, test._BankAccount__account_number)

        self.assertEqual(
            3116553, test._BankAccount__client_number)

        self.assertEqual(
            5000.00, test._BankAccount__balance)

        self.assertEqual(
            test_date, test._date_created)

        self.assertEqual(
            4000.00, test._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance_correct_set(self):

        test_date = datetime(2025, 1, 1).date()

        test = SavingsAccount(101,
                              3116553,
                              5000.00,
                              test_date,
                              "Miny-Mum")

        self.assertEqual(50, test._SavingsAccount__minimum_balance)

    def test_get_service_changes_balance_greater_correct_return(self):

        test = self.savings_account

        expected = 0.5

        self.assertEqual(expected, test.get_service_charges())

    def test_get_service_changes_balance_equal_correct_return(self):

        test_date = datetime(2025, 1, 1).date()

        test = SavingsAccount(101,
                              3116553,
                              5000.00,
                              test_date,
                              5000.00)

        expected = 0.5

        self.assertEqual(expected, test.get_service_charges())

    def test_get_service_changes_balance_lesser_correct_return(self):

        test_date = datetime(2025, 1, 1).date()

        test = SavingsAccount(101,
                              3116553,
                              3500,
                              test_date,
                              5000.00)

        expected = 1.0

        self.assertEqual(expected, test.get_service_charges())

    def test_str_method_correct_return(self):

        test = self.savings_account
        expected = ("Account Number: 101 Balance: $5,000.00\n"
                    + "Minimum Balance: $4,000.00 Account Type: Savings")
        
        self.assertEqual(expected, str(test))

