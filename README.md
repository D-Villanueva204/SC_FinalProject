# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Dominique Villanueva

## Assignment
Assignment 1: "Classes, Encapsulation and Unit Test Planning"
Assignment 2: "Abstraction, Inheritance, and Polymorphism."
Assignment 3: "Design Patterns."
Assignment 4: "Programming Paradigms"
Assignment 5: "Algorithms, Documentation, and Distribution"

## Encapsulation
In programming languages, the ability to control the access of modification of class/object variables is very important. 
What if someone puts in a value of the wrong data type for a class variable? You don't want to entirely restrict these values to those who want to use your object.
You encapsulate your ability to retrieve and modify the class values through the use of defined methods called mutators and accessors (or getters or setters when I was learning programming at 17 lol)

To demonstrate these concepts, in BankAccount, we have an accessor method for each defined class variable. This helps prevent the direct access of private variables by giving a cleaner way to access them through returning the value of the variable, but not the variable itself. For modifying the balance, BankAccount features the methods update_balance, deposit, and withdraw. These methods help encapsulate the modification of variables and also adds extra protection via data validation. We give the user a friendly way to change their balance, but only in controlled ways that it logically works within the intended functionality of the class. So, no setting "dog" as the balance, you hear?

## Polymorphism
Polymorphism was achieved by SavingsAccount, ChequingAccount, InvestmentAccount, despite having different behaviours, demonstrating their common methods inherited from the BankAccount superclass.
When we put all of these types into one collection, we knew that we could call a method that all of them would have, the withdraw() and get_service_charges() method, because they 
inherit BankAccount methods. They produced different results, but still accomplished BankAccount behaviours.

## Strategy Pattern
A strategy pattern was used to enhance and simplify the BankAccounts subclasses. A base ServiceChargeStrategy was created that
created a reusable structure that BankAccount classes could use to achieve different behaviours via different ServiceChargeStrategy subclasses.

## Observer Pattern
The observer pattern was implemented and used to monitor suspicious transactions. The Observer class was implemented in the Client class, which contains functions on how to notify the real client, but not monitoring what was needed to be notified.
This purpose was done by the Subject class, which was implemented by the BankAccount class and its subclasses. Subject contains methods on notifying Observers to a certain behaviour, which in this case was low balance after a transaction
and a large amount transaction, both implemented and used by BankAccount instances.


## Event-Driven Programming Paradigm
We make heavy use of Event-Driven Programming Paradigms in the ClientLookupWindow and AccountDetailsWindow classes. AccountDetailsWindow inherits the withdraw_button, deposit_button, and exit_button attributes, which are Signal objects.
We connect them with a *clicked* event, with event-handling Slot objects in the same class. It also shows that Classes could contain both Slots and Signals. balance_updated (which I did not embarassingly spend hours wondering why 'balance_label' wasn't connecting)
is a Signal object, which is connected in ClientLookupWindow with the update_data Slot instance. The event is handled with an "emit" of the Signal object which occurs after each successful transaction in AccountDetailsWindow, with the previous Slot we 
defined and connected previously, which runs the behaviour of updating account data. 

## Filtering
The filtering algorithm was implemented on client_lookup_window's on_filter_clicked method. It makes 
use of the data in account_table, and checks if data in each row matches the criteria, and returns a collection (visually) of those matching items.
            