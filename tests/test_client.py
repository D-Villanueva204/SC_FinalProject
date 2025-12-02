"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = " ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Dominique Villanueva"

import unittest

from client.client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.client = Client(3116553,
                             "Dominique",
                             "Villanueva",
                             "Dom.Villanueva@outlook.com")

    # 1:

    def test_init_valid_args_attributes_set(self):

        # Assert

        self.assertEqual(3116553, self.client._Client__client_number)

        self.assertEqual("Dominique", self.client._Client__first_name)

        self.assertEqual("Villanueva", self.client._Client__last_name)

        self.assertEqual("Dom.Villanueva@outlook.com",
                         self.client._Client__email_address)

    # 2:

    def test_init_invalid_client_number_value_error_raise(self):

        # Arrange, Act, Assert

        with self.assertRaises(ValueError):
            test = Client("3116553",
                          "Dominique",
                          "Villanueva",
                          "Dom.Villanueva@outlook.com")

    # 3:

    def test_init_blank_first_name_value_error_raise(self):

        # Arrange, Act, Assert

        with self.assertRaises(ValueError):
            test = Client(3116553,
                          "",
                          "Villanueva",
                          "Dom.Villanueva@outlook.com")

    # 4:

    def test_init_blank_last_name_value_error_raise(self):

        # Arrange, Act, Assert

        with self.assertRaises(ValueError):
            test = Client(3116553,
                          "Dominique",
                          "",
                          "Dom.Villanueva@outlook.com")

    # 5:

    def test_init_invalid_email_correct_return(self):

        # Arrange, Act

        test = Client(3116553,
                      "Dominique",
                      "Villanueva",
                      "email@pixell-river.com")

        # Assert

        self.assertEqual("email@pixell-river.com", 
                         test._Client__email_address)

    # 6:

    def test_client_number_accessor_valid_return(self):

        # Arrange has already been done.
        # Act and Assert

        self.assertEqual(3116553, self.client.client_number)

    # 7:

    def test_first_name_accessor_valid_return(self):

        # Arrange has already been done.
        # Act and Assert

        self.assertEqual("Dominique", self.client.first_name)

    # 8:

    def test_last_name_accessor_valid_return(self):

        # Arrange has already been done.
        # Act and Assert

        self.assertEqual("Villanueva", self.client.last_name)

    # 9:

    def test_email_address_accessor_valid_return(self):

        # Arrange has already been done.
        # Act and Assert

        self.assertEqual("Dom.Villanueva@outlook.com",
                         self.client.email_address)

    # 10:

    def test_str_method_correct_return(self):

        # Arrange has already been done.
        # Act and Assert

        self.assertEqual(
            "Villanueva, Dominique [3116553] - Dom.Villanueva@outlook.com\n", str(self.client))
