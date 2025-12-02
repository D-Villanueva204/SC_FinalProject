__author__ = "Dominique Villanueva"
__version__ = "1.0.0"

from .service_charge_strategy import ServiceChargeStrategy
from bank_account import *


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Subclass of ServiceChargeStrategy. Implements
    calculate_service_charge with respect to minimum balance,
    and service charge premium.

    """

    __minimum_balance = None
    SERVICE_STRATEGY_PREMIUM = 2.0

    def __init__(self,
                 minimum_balance: float):
        """
        Initializes the class attributes with argument values.

        Args:
            minimum_balance (float):
            A float value to represent the minimum balance
            before service charges are applied.

        """

        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge based off minimum balance,
        adds premiums if below minimum balance.

        Returns:
            float: The calculated service charge.

        """

        service_charge = self.BASE_SERVICE_CHARGE

        if (account.balance < self.__minimum_balance):
            service_charge *= self.SERVICE_STRATEGY_PREMIUM

        return service_charge
