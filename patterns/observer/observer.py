__author__ = "Dominique Villanueva"
__version__ = "1.0.1"

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Interface for subclassed observer that require notification of 
    changes in their subject(s).

    """

    @abstractmethod
    def update(self, message: str):
        """
        This method is to be implemented by its subclasses.
        Notifies observers when there are changes in the subject.

        """
        pass
