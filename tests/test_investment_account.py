"""
Description: Unit tests for the ChequingAccount class.
Author: Dominique Villanueva
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
    
"""

__author__ = "Dominique Villanueva"
__version__ = "1.1.1"

import unittest
from datetime import date, datetime, timedelta
from bank_account import *


class InvestmentAccountTests(unittest.TestCase):

    def setUp(self):

        test_date = datetime(2025, 1, 1).date()

        self.investment_account = \
            InvestmentAccount(101,
                              3116553,
                              5000.00,
                              test_date,
                              45)

    def test_init_valid_args_attributes_set(self):
        test = self.investment_account
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
            45, test._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_type_correct_set(self):
        test_date = datetime(2025, 1, 1).date()

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 "BigFee")

        self.assertEqual(2.55, test._InvestmentAccount__management_fee)

    def test_get_service_charges_more_than_ten_years_correct_return(self):
        test_date = datetime(2005, 1, 1).date()

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 45)

        self.assertEqual(45.5, test.get_service_charges())

    def test_get_service_charges_exactly_ten_years_correct_return(self):
        test_date = date.today() - timedelta(days=(10 * 365.25))

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 45)

        self.assertEqual(0.5, test.get_service_charges())

    def test_get_service_charges_less_than_ten_years_correct_return(self):
        test_date = datetime(2025, 1, 1).date()

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 45)

        self.assertEqual(0.5, test.get_service_charges())

    def test_str_created_date_greater_than_ten_years_correct_return(self):
        test_date = datetime(2005, 1, 1).date()
        expected = "Account Number: 101 Balance: $5,000.00\n" \
            "Date Created: 2005-01-01 "\
            "Management Fee: Waived Account Type: Investment"

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 45)

        self.assertEqual(expected, str(test))

    def test_str_created_date_less_than_ten_years_correct_return(self):
        test_date = datetime(2025, 1, 1).date()
        expected = "Account Number: 101 Balance: $5,000.00\n" \
            "Date Created: 2025-01-01 "\
            "Management Fee: $45.00 Account Type: Investment"

        test = InvestmentAccount(101,
                                 3116553,
                                 5000.00,
                                 test_date,
                                 45)

        self.assertEqual(expected, str(test))
