__author__ = "Dominique Villanueva"
__version__ = "1.1.2"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy import *

class ChequingAccount(BankAccount):
    """
    Instance of BankAccount. Handles banking transactions and functions,
    catered for a client that has frequent deposits and withdraws.

    """

    __strategy = None

    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 overdraft_limit: float,
                 overdraft_rate: float):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): 
            An integer representing the chequing account number.
            client_number (int): 
            An integer representing the account holder.
            balance (float): 
            A float value representing the balance.
            date_created (date): 
            A date value representing the date created.
            overdraft_limit (float):
            The maximum amount a balance can be
            overdrawn before overdraft fees.
            overdraft_rate (float):
            The rate to which overdraft fees will be applied.


        Raises:
            ValueError: When given account number or
            client number is non-numeric.

        """

        super().__init__(account_number,
                         client_number,
                         balance,
                         date_created)
        

        # Attribute validation.

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.00

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)


    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The ChequingAccount instance formatted as a string.

        """
        message = (f"{super().__str__()}"
                   + f"Overdraft Limit: ${self.__overdraft_limit} "
                   + f"Overdraft Rate: "
                   + f"{float(self.__overdraft_rate * 100):,.2f}% "
                   + f"Account Type: Chequing")
        return message

    def get_service_charges(self) -> float:
        """
        Returns service charges based off overdraft limit.

        Returns:
            float: Calculated service charge.

        """

        return self.__strategy.calculate_service_charges(self)