__author__ = "Dominique Villanueva"
__version__ = "3.5.11"

from abc import abstractmethod, ABC
from datetime import date
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject


class BankAccount(Subject, ABC):
    """
    BankAccount class: Handles banking transactions and functions.

    """

    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date):
        super().__init__()
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

        Raises:
            ValueError: When given account number or 
            client number is non-numeric. 

        """

        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        self.LOW_BALANCE_LEVEL = 50.0

        # Validation of variables.

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    # Accessor Methods

    @property
    def account_number(self) -> int:
        """
        Accessor for account number attribute

        Returns:
            int: The account number value.

        """

        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute

        Returns:
            int: The client number value.

        """

        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Accessor for balance attribute

        Returns:
            float: The balance of the current account.

        """

        return self.__balance

    # Update Balance

    def update_balance(self,
                       amount: float):
        """
        Method that adds a given amount to the current balance.
        Non-numeric amount values will not be added to account.

        Args:
            amount (float): 
            The amount that will be added onto the balance.

        """

        try:
            amount = float(amount)

            if (abs(amount) > self.LARGE_TRANSACTION_THRESHOLD):
                msg = (f"Large transaction ${amount:,.2f}: "
                       + f"on account {self.__account_number}.")
                self.notify(msg)

            self.__balance += amount

            if (self.__balance < self.LOW_BALANCE_LEVEL):
                msg = (f"Low balance warning ${self.__balance:,.2f}: "
                       + f"on account {self.__account_number}.")
                self.notify(msg)
        except ValueError:
            amount = 0

    # Deposit

    def deposit(self,
                amount: float):
        """
        Method that handles the deposit of valid amounts to account balance

        Args:
            amount (float): 
            The amount that will be deposited onto the balance.

        Raises:
            ValueError: If amount is non-numeric or non-positive.

        """

        if (isinstance(amount, (int, float))) == False:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount < 0:
            raise ValueError(f"Deposit amount:"
                             + f"${amount:,.2f} must be positive.")

        if (isinstance(amount, (int, float)) and
                amount > 0):
            self.update_balance(amount)

    # Withdraw

    def withdraw(self,
                 amount: float):
        """
        Method that handles the withdrawal of specified amount from account

        Args:
            amount (float): 
            The amount to withdraw from account.

        Raises:
            ValueError: If amount is non-numeric, 
            non-positive, or exceeds balance.

        """

        if (isinstance(amount, (int, float))) == False:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount < 0:
            raise ValueError(f"Deposit amount:"
                             + f"${amount:,.2f} must be positive.")

        if (float(amount) > self.__balance):
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} "
                             + f"must not exceed the account balance: ${self.__balance:,.2f}")
        else:
            amount *= -1
            self.update_balance(amount)

    # str method

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The BankAccount instance formatted as a string.

        """

        return (f"Account Number: {self.__account_number} "
                + f"Balance: ${self.__balance:,.2f}\n")

    @abstractmethod
    def get_service_charges() -> float:
        """
        To be defined in subclasses.

        Returns:
            float: Service charges, formula based on subclass type.

        """

        pass

    def attach(self,
               observer: Observer):
        """
        Function that adds a new observer to list.

        Args:
            observer (Observer):
            The new observer to add.

        """

        self._observers.append(observer)

    def detach(self, observer):
        """
        Function that removes specified observer from list.

        Args:
            observer (Observer): 
            The observer to remove from list.

        """

        self._observers.remove(observer)

    def notify(self, message: str):
        """
        Notifies all observers in list with specified message.

        Args:
            message (str):
            The message to notify the observers with.

        """
        for observer in self._observers:
            observer.update(message)
