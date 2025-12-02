__author__ = "Dominique Villanueva"
__version__ = "2.0.0"


from datetime import date
from bank_account.bank_account import *
from patterns.strategy import *


class SavingsAccount(BankAccount):
    """
    Instance of BankAccount. Handles banking transactions and functions,
    catered for a client that will
    mostly deposit funds and rarely withdraws.

    """

    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 minimum_balance: float):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int):
            An integer representing the bank account number.
            client_number (int):
            An integer representing the account holder.
            balance (float):
            A float value representing the balance.
            date_created (date):
            A date value representing the date created.
            minimum_balance (float):
            A float value to represent the minimum balance
            before service charges are applied.

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
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

        self.__strategy = MinimumBalanceStrategy(minimum_balance)

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The SavingsAccount instance formatted as a string.

        """
        return_message = (f"{super().__str__()}"
                          + f"Minimum Balance: "
                          + f"${self.__minimum_balance:,.2f}"
                          + f" Account Type: Savings")

        return return_message

    def get_service_charges(self) -> float:
        """
        Returns service charges based off minimum balance.

        Returns:
            float: Calculated service charge.

        """

        return self.__strategy.calculate_service_charges(self)