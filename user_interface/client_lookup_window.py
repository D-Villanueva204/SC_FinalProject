__author__ = "ACE Faculty"
__version__ = "2.4.7"
__credits__ = "Dominique Villanueva"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):
    """
    Subclass of LookupWindow. Responsible for event handling and GUI for
    looking at client and account files.

    """

    def __init__(self):
        """
        Initializes class attributes for this instance.

        """

        super().__init__()
        self.__client_listing, self.__accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)

    @Slot()
    def __on_lookup_client(self):
        """
        Retrieves a Client object based on entered client_number,
        and displays associated data. 
        Prompts when no matching data is found.

        """

        user_input = None

        try:
            user_input = int(self.client_number_edit.text())
        except ValueError as e:
            QMessageBox.information(self,
                                    "Input Error",
                                    "The client number must be a numeric value.")
            self.reset_display()

        try:
            if (isinstance(user_input, int)):
                retrieved_client = \
                    self.__client_listing[user_input]
                self.client_info_label.setText(f"Client Name: " +
                                               f"{retrieved_client.first_name} " +
                                               f"{retrieved_client.last_name}")
                for account_number in self.__accounts:
                    account = self.__accounts[account_number]
                    if retrieved_client.client_number == account.client_number:
                        new_row = self.account_table.rowCount()
                        self.account_table.insertRow(new_row)
                        account_number_item = \
                            QTableWidgetItem(str(account.account_number))
                        account_number_item.setTextAlignment(
                            Qt.AlignVCenter | Qt.AlignHCenter)
                        balance_item = \
                            QTableWidgetItem(f"${account.balance:,.2f}")
                        balance_item.setTextAlignment(
                            Qt.AlignRight | Qt.AlignVCenter)
                        date_created_item = \
                            QTableWidgetItem(str(account._date_created))
                        date_created_item.setTextAlignment(
                            Qt.AlignVCenter | Qt.AlignHCenter)
                        account_type_item = \
                            QTableWidgetItem(f"{account.__class__.__name__}")
                        account_type_item.setTextAlignment(
                            Qt.AlignVCenter | Qt.AlignHCenter)
                        self.account_table.setItem(
                            new_row, 0, account_number_item)
                        self.account_table.setItem(new_row, 1, balance_item)
                        self.account_table.setItem(
                            new_row, 2, date_created_item)
                        self.account_table.setItem(
                            new_row, 3, account_type_item)
                self.account_table.resizeColumnsToContents()
        except KeyError as e:
            QMessageBox.information(self,
                                    "Not Found",
                                    f"Client number: {user_input} not found.")
            self.reset_display()

        self.__toggle_filter(False)

    @Slot()
    def __on_text_changed(self):
        """
        Removes all records from the account_table when a
        new client number is entered.

        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self,
                            row: int,
                            column: int):
        """
        Identifies the account selected and transfers control to 
        an AccountDetailsWindow instance.

        Args:
            row (int): The row of the selected cell.
            column: (int): The column of the cell.

        """

        account_number = self.account_table.item(row, 0).text()

        if (len(str(account_number).strip()) > 0):
            account_number = int(account_number)
            if (account_number in self.__accounts):
                retrieved_account = self.__accounts[account_number]
                bank_window = AccountDetailsWindow(retrieved_account)
                bank_window.balance_updated.connect(self.__update_data)
                bank_window.exec_()
            elif (account_number not in self.__accounts):
                QMessageBox.information(self,
                                        "No Bank Account",
                                        "Bank Account selected does not exist.")
            elif (account_number == None):
                QMessageBox.information(self,
                                        "Invalid Selection",
                                        "Please select a valid record.")

    @Slot(BankAccount)
    def __update_data(self,
                      account: BankAccount):
        """
        Updates the account data in the account_details_table, and in the accounts.csv file 
        with specified BankAccount instance.
        Slot instance.

        Args:
            account (BankAccount): The account to update from.

        """
        for row in range(self.account_table.rowCount()):
            account_number = int(self.account_table.item(row, 0).text())
            if (account_number == account.account_number):
                self.account_table.item(row, 1).setText(
                    f"${account.balance:,.2f}")
        self.__accounts[account.account_number] = account
        update_data(account)

    @Slot()
    def __on_filter_clicked(self):
        """
        Grabs user-defined filter input, and
        retrieve records based off that criteria.

        """

        filter_state = self.filter_button.text()
        if (filter_state == "Apply Filter"):
            filter_value = self.filter_combo_box.currentIndex()
            criteria = self.filter_edit.text()

            for row in range(self.account_table.rowCount()):
                retrieved_value = \
                    self.account_table.item(row, filter_value).text()
    
                if retrieved_value == criteria:
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)
            self.__toggle_filter(True)
        else:
            self.__toggle_filter(False)

    def __toggle_filter(self,
                        filter_on: bool):
        """
        Toggles the display of filter widgets to indicate to the user 
        if filtering is currently in progress, and to reset the table.

        Args:
            filter_on (boolean): If true, indicates to user that filtering is taking place,
            if false, indicates to user that they can apply new filter criteria.

        """

        self.filter_button.setEnabled(True)
        self.filter_combo_box.setEnabled(not filter_on)
        self.filter_edit.setEnabled(not filter_on)

        if (filter_on == True):
            self.filter_button.setText("Reset")
            self.filter_label.setText("Data is Currently Filtered.")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_edit.setText("")
            self.filter_label.setText("Data is Not Currently Filtered.")

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
