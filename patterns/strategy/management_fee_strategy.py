__author__ = "Dominique Villanueva"
__version__ = "1.0.2"

from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account import *


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Subclass of ServiceChargeStrategy. Implements
    calculate_service_charge with respect to account age.

    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self,
                 date_created: date,
                 management_fee: float):
        """
        Initializes the class attributes with argument values.

        Args:
            date_created (date): 
            The date of account creation.
            management_fee (float): 
            A float value that stores the flat-rate fee
            the bank charges for managing this account.

        """

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge based off account age.

        Returns:
            float: The calculated service charge.

        """

        service_charge = self.BASE_SERVICE_CHARGE

        if (self.__date_created < self.TEN_YEARS_AGO):
            service_charge = (self.BASE_SERVICE_CHARGE
                              + self.__management_fee)

        return service_charge
