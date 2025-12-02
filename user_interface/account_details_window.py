__author__ = "ACE Faculty"
__version__ = "2.4.4"
__credits__ = "Dominique Villanueva"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy


class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        
        Args:
            account: The bank account to be displayed.
        Returns:
            None

        """
        super().__init__()

        if (isinstance(account, BankAccount)):
            self.__account = copy.copy(account)
            self.account_number_label.setText(
                str(self.__account.account_number))
            self.balance_label.setText(
                f"${self.__account.balance:,.2f}")

            self.deposit_button.clicked.connect(
                self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(
                self.__on_apply_transaction)
            self.exit_button.clicked.connect(
                self.__on_exit)
        else:
            self.reject()

    @Slot()
    def __on_apply_transaction(self):
        """
        Validates transaction amount, and executes transaction 
        on the account selected.

        """
        amount = 0.00
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError as e:
            QMessageBox.information(self,
                                    "Invalid Data",
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        transaction = ""

        try:
            sender = self.sender()
            if (sender == self.deposit_button):
                transaction = "Deposit"
                self.__account.deposit(amount)
            if (sender == self.withdraw_button):
                transaction = "Withdraw"
                self.__account.withdraw(amount)

            self.balance_label.setText(
                f"${self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.__account)
        except Exception as e:
            QMessageBox.information(self,
                                    f"{transaction} Failed",
                                    f"{str(e)}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self):
        """
        Closes current window.

        """
        self.close()
