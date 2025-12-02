__author__ = "Dominique Villanueva"
__version__ = "2.4.3"


from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility import file_utils
from datetime import datetime


class Client(Observer):
    """
    Client class: Handles client functions and data.  

    """

    def __init__(self,
                 client_number: int,
                 first_name: str,
                 last_name: str,
                 email_address: str):
        """
        Initializes the class attributes with argument values.

        Args:
            client_number (str): 
            An integer value representing the client number.
            first_name (str): 
            A string value of the client's first name.
            last_name (str):
            A string value of the client's first name.
            email_address (str): 
            A string value of the client's first name.

        Raises:
            ValueError: When the client number is non-numeric, 
            first or last name is blank.

        """

        # Validation of variables.

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")

        if (len(first_name.strip()) > 0 and first_name is not None):
            self.__first_name = first_name
        else:
            raise ValueError("First name must not be blank.")

        if (len(last_name.strip()) > 0 and last_name is not None):
            self.__last_name = last_name
        else:
            raise ValueError("Last name must not be blank.")

        try:
            validate_email(email_address, check_deliverability=False)

            self.__email_address = email_address

        except (EmailNotValidError):
            self.__email_address = "email@pixell-river.com"

    # Accessor Methods

    @property
    def client_number(self) -> int:
        """
        Accessor for client_number attribute

        Returns:
            int: The client number value.

        """

        return self.__client_number

    # Accessor Methods

    @property
    def first_name(self) -> str:
        """
        Accessor for first_name attribute

        Returns:
            str: The first name of the client.

        """

        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for last_name attribute

        Returns:
            str: The last name of the client.

        """

        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for email_address attribute

        Returns:
            str: The email address of the client.

        """

        return self.__email_address

    # str Method.

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The course instance formatted as a string.

        """

        return (f"{self.__last_name}, "
                + f"{self.__first_name} "
                + f"[{self.__client_number}] - "
                + f"{self.__email_address}\n")

    def update(self, message):
        """
        Sends an email when notified, 
        with formatted subject and message.

        Args:
            message (str):
            The message to sent. Will be formatted.
            
        """

        email_address = self.email_address
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        email_message = (f"Notification for {self.client_number}:"
                         + f" {self.first_name} {self.last_name}:"
                         + f" {message}")

        file_utils.simulate_send_email(email_address,
                                       subject,
                                       email_message)
