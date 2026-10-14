
class BankAccount: #this is a where the objects of the class are defined and seperated into private and public attributes.
    def __init__(self, account, account_number, balance): 
        self.__account_number = account
        self.__account_holder_number = account_number
        self.__balance = balance

    def deposit(self, amount): #this is where the user can deposit their money. It shows that the amount must be positive for the code to work.
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount): #this is where the user can withdraw their money. The amount must be less than the current balance and it must always be positive.
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self): #this is the code that helps the user check their balance.
        return self.__balance

    def get_account_number(self): #this sit the code that helps the user check their account number.
        return self.__account

    def display_info(self): #this displays the information of the account.
        print(f"Account: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_number}")
        print(f"Balance: {self.__balance}")

#this is where the user inputs their details.
account_number = int(input("Enter bank account: ")) 
account_holder_number = int(input("Enter account holder number: "))
initial_balance = float(input("Enter initial balance: "))

#this is for updating the balance of the users account. 
if update_balance := input("Do you want to update your balance? (yes/no): ").lower() == "yes":
    new_balance = float(input("Enter new balance: "))
    account = BankAccount(account_number, account_holder_number, new_balance)

#this displays the information of the users account if they want to.
display_info = input("Do you want to display account information? (yes/no): ").lower() == "yes"
if display_info:
    account.display_info()

#This code was made by mostly by IntelliSense. (2026, October 14).
