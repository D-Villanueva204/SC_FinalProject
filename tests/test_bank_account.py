"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = " ACE Faculty"
__version__ = "1.0.3"
__credits__ = "Dominique Villanueva"

import unittest

from bank_account.bank_account import *


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(101,
                                        3116553,
                                        5000.00)

    # 1

    def test_init_valid_args_attributes_set(self):
        # Arrange and Act is done!

        # Assert

        self.assertEqual(101, self.bank_account._BankAccount__account_number)

        self.assertEqual(
            3116553, self.bank_account._BankAccount__client_number)

        self.assertEqual(5000.00, self.bank_account._BankAccount__balance)

    # 2

    def test_init_non_numeric_balance_zero_return(self):
        test = BankAccount(101,
                           3116553,
                           "FiveThousand")

        self.assertEqual(0, test._BankAccount__balance)

    # 3

    def test_init_non_numeric_account_number_value_error_raises(self):

        with self.assertRaises(ValueError):
            test = BankAccount("101",
                               3116553,
                               5000.00)

    # 4

    def test_init_non_numeric_client_number_value_error_raises(self):

        with self.assertRaises(ValueError):
            test = BankAccount(101,
                               "3116553",
                               5000.00)

    # 5

    def test_account_number_accessor_correct_return(self):

        self.assertEqual(101, self.bank_account.account_number)

    # 6

    def test_client_number_accessor_correct_return(self):

        self.assertEqual(3116553, self.bank_account.client_number)

    # 7

    def test_balance_accessor_correct_return(self):

        self.assertEqual(5000.00, self.bank_account.balance)

    # 8

    def test_update_balance_positive_amount_correct_update(self):

        test = self.bank_account

        test.update_balance(300)

        self.assertEqual(5300.00, test._BankAccount__balance)

    # 9

    def test_update_balance_negative_amount_correct_update(self):

        test = self.bank_account

        test.update_balance(-300)

        self.assertEqual(4700, test._BankAccount__balance)

    # 10

    def test_update_balance_non_numeric_amount_correct_update(self):

        test = self.bank_account

        test.update_balance("Three Hundred")

        self.assertEqual(5000, test._BankAccount__balance)

    # 11

    def test_deposit_valid_amount_correct_update(self):

        test = self.bank_account

        test.deposit(500.00)

        self.assertEqual(5500, test._BankAccount__balance)

    # 12

    def test_deposit_invalid_amount_value_error(self):

        test = self.bank_account

        with self.assertRaises(ValueError):
            test.deposit(-500.00)

    # 13

    def test_withdraw_valid_amount_correct_update(self):

        test = self.bank_account

        test.withdraw(500.00)

        self.assertEqual(4500, test._BankAccount__balance)

    # 14

    def test_withdraw_negative_amount_value_error(self):

        test = self.bank_account

        with self.assertRaises(ValueError):
            test.withdraw(-500.00)

    # 15

    def test_withdraw_amount_exceeding_balance_value_error(self):

        test = self.bank_account

        with self.assertRaises(ValueError):
            test.withdraw(5600)

    # 16

    def test_str_method_correct_return(self):
        self.assertEqual("Account Number: 101 Balance: $5,000.00",
                         str(self.bank_account))
