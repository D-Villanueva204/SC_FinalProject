__author__ = "Dominique Villanueva"
__version__ = "1.0.1"

from .service_charge_strategy import ServiceChargeStrategy
from bank_account import *


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Subclass of ServiceChargeStrategy. Implements
    calculate_service_charge with respect to an overdraft
    limit.

    """

    def __init__(self,
                 overdraft_limit: float,
                 overdraft_rate: float):
        """
        Initializes the class attributes with argument values.

        Args:
            overdraft_limit (float): 
            The specified overdraft limit.
            overdraft_rate (float): 
            The specified overdraft rate.

        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge based off the overdraft limit.

        Returns:
            float: The calculated service charge.

        """

        service_charge = self.BASE_SERVICE_CHARGE

        if account.balance < self.__overdraft_limit:
            service_charge += (self.__overdraft_limit - account.balance) \
                * self.__overdraft_rate

        return service_charge
