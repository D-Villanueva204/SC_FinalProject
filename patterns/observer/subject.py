__author__ = "Dominique Villanueva"
__version__ = "1.0.1"

from abc import ABC, abstractmethod
from .observer import Observer


class Subject(ABC):
    """
    Interface for defining a class that will
    maintain Observer instances and notifying them of 
    state changes or events.

    """

    def __init__(self):
        """
        Initializes the class attributes with argument values.

        """
        self._observers = []

    @abstractmethod
    def attach(self,
               observer: Observer):
        """
        Abstract method. Adds observer to list of observers.

        Args:
            observer (Observer):
            The observer to add to list.

        """
        pass

    @abstractmethod
    def detach(self,
               observer: Observer):
        """
        Abstract method. Removes observer from list of observers.

        Args:
            observer (Observer):
            The observer to remove from list.

        """
        pass

    @abstractmethod
    def notify(self,
               message: str):
        """
        Abstract method. Notifies observers in list.

        Args:
            message (str):
            The message to notify observers.

        """
        pass
