__author__ = "Dominique Villanueva"
__version__ = "2.3.5"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy import *


class InvestmentAccount(BankAccount):
    """
    Instance of BankAccount. Handles banking transactions and functions,
    catered for a client with a long-term savings plan.

    """

    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 management_fee: float):
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
            management_fee (float):
            A float value that stores the flat-rate fee
            the bank charges for managing this account.


        Raises:
            ValueError: When given account number or
            client number is non-numeric.

        """

        super().__init__(account_number,
                         client_number,
                         balance,
                         date_created)

        # Initialization of variables.

        self.TEN_YEARS_AGO = \
            date.today() - timedelta(days=(10 * 365.25))

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(date_created,
                                                management_fee)

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The InvestmentAccount instance formatted as a string.

        """

        management_fee_message = \
            "Waived" if (self._date_created < self.TEN_YEARS_AGO) \
            else f"${self.__management_fee:,.2f}"

        return_message = (f"{super().__str__()}"
                          + f"Date Created: "
                          + f"{self._date_created} "
                          + f"Management Fee: {management_fee_message} "
                          + f"Account Type: Investment")

        return return_message

    def get_service_charges(self) -> float:
        """
        Returns service charges based off of account.

        Returns:
            float: Calculated service charge.

        """

        return self.__strategy.calculate_service_charges(self)
