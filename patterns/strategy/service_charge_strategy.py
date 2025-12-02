__author__ = "Dominique Villanueva"
__version__ = "1.0.1"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    This class defines the overall structure of this strategy pattern.
    
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        This method is to be implemented by its subclasses.
        Should produce a calculated service charge.

        Returns:
            float: The calculated service charge.
        
        """
        pass


