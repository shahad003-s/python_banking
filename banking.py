import csv
import os

class Data:

    bank_info = [
        {"account_id": "10001","first_name": "suresh","last_name": "sigera","password": "juagw362","balance_checking": 1000,"balance_savings": 10000 ,"status": "active","overdraft_count": 0},
        {"account_id": "10002","first_name": "james","last_name": "taylor","password": "idh36%@#FGd","balance_checking": 10000,"balance_savings": 10000,"status": "active","overdraft_count": 0},
        {"account_id": "10003","first_name": "melvin","last_name": "gordon","password": "uYWE732g4ga1","balance_checking": 2000,"balance_savings": 20000,"status": "active","overdraft_count": 0},
        {"account_id": "10004","first_name": "stacey","last_name": "abrams","password": "DEU8_qw3y72$","balance_checking": 2000,"balance_savings": 20000,"status": "active","overdraft_count": 0},
        {"account_id": "10005","first_name": "jake","last_name": "paul","password": "d^dg23g)@","balance_checking": 100000,"balance_savings": 100000 ,"status": "active","overdraft_count": 0 },
    ]
  
    fieldnames = ["account_id","first_name","last_name","password","balance_checking","balance_savings","status" ,"overdraft_count"]
   
    if not os.path.exists("./bank.csv"):
        with open("./bank.csv", "w", newline="") as csvfile:
            try:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in bank_info:
                    writer.writerow(row)
            except csv.Error as e:
                print(e)

class Bank:
    def __init__(self, name):
        bank_csv = open("bank.csv", "r")
        last_account = bank_csv.readlines()[-1]
        last_account = last_account.split(",")
        last_account_id = int(last_account[0])
        self.name = name
        self.fieldnames = ["account_id","first_name","last_name","password","balance_checking","balance_savings","status","overdraft_count"]
        last_account_id += 1
        self.account_id = str(last_account_id)

    def add_customer(self, customer):
        try:
            with open("bank.csv", "a+", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writerow(customer)
        except csv.Error as e:
            print(e)

    def account(self):
        account = input(" Do you have  an account? Y for yes N for no\n").lower()
        if account == "y":
            log = Customer_Login()
            log.login()
        elif account == "n":
            self.create_account()
        else:
            print("Invalid option. Enter y or n .")

    def create_account(self):
        first_name = input("Enter first name: ").lower()
        last_name = input("Enter last name: ").lower()
        password = input("Enter password: ").lower()
        print("Select the type of account(s):")
        print("1. Checking account")
        print("2. Savings account")
        print("3. Both checking and savings accounts")
        balance_checking = None
        balance_savings = None
        balance = True
        while balance:
            account_type = int(input("Enter the option number: "))
            if account_type == 1:
                balance_checking = float(input("Enter checking balance: "))
                balance = False
            elif account_type == 2:
                balance_savings = float(input("Enter savings balance: "))
                balance = False
            elif account_type == 3:
                balance_checking = float(input("Enter checking balance: "))
                balance_savings = float(input("Enter savings balance: "))
                balance = False
            else:
                print("Invalid option. No account created.")
                balance = True

        new_customer = {
            "account_id": self.account_id,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
            "balance_checking": balance_checking,
            "balance_savings": balance_savings,
            "status": "active",
            "overdraft_count": 0
        }
        self.add_customer(new_customer)
        print(f"Account created successfully! Account ID: {self.account_id}")

class Customer_Login:
    def __init__(self):
        self.logged_in_customer = None

    def login(self):
        idNumber = input("Enter your Account ID: ").lower()
        username = input("Enter your first name: ").lower()
        password = input("Enter your password: ").lower()

        with open("bank.csv", "r") as bank_csv:
            reader = csv.DictReader(bank_csv)
            for customer in reader:
                if ( customer["account_id"] == idNumber and customer["first_name"] == username and customer["password"] == password):
                    print(f"Welcome, {customer['first_name']}! You are now logged in.\n")
                    print("Account details:\n")
                    print( f"{customer['account_id']}, {customer['first_name']}, {customer['last_name']}, {customer['balance_checking']}, {customer['balance_savings']}")
                    self.logged_in_customer = customer
                    self.choose_operation()
                    return customer
            else:
                print("Invalid credentials. Please try again.")

    def choose_operation(self):
        choose = True
        while choose:
            print("\nSelect the type of operation:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Transfer")
            print("4.log out")
            operation = input("Enter the option number: ")

            if operation == "1":
                withdraw = Withdraw(self)
                withdraw.withdraw_money()
            elif operation == "2":
                deposit = Deposit(self)
                deposit.deposit_money()
            elif operation == "3":
                transfer = Transfer(self)
                transfer.transfer_money()
            elif operation == "4":
                print("You have logged out. Have a nice day!")
                choose = False

            else:
                print("Invalid option. Please try again.")


class Withdraw:
    def __init__(self, login_instance):
        self.login_instance = login_instance

    def withdraw_money(self):

        customer = self.login_instance.logged_in_customer

        if customer.get("status", "active") == "deactivated":
            print("Your account is deactivated. Please add funds to reactivate.")
            return

        overdraft_count = int(customer.get("overdraft_count", 0))

        print("Select the type of account to withdraw from:")
        print("1. Checking account")
        print("2. Savings account")
        account_type = int(input("Enter the option number: "))
        if account_type == 1:
            if customer["balance_checking"] is not None and customer["balance_checking"] != "" :
                checking_balance = float(customer["balance_checking"])
                withdrawal_amount = float(input("Enter the amount to withdraw: $"))
                if withdrawal_amount <= 100:
                    if checking_balance > 0:
                        customer["balance_checking"] = (checking_balance - withdrawal_amount)
                        print(f"Withdrawal successful. New checking balance: ${customer['balance_checking']}" )
                        self.update_csv(customer)
                    if withdrawal_amount > checking_balance :
                        customer["balance_checking"] = (checking_balance - withdrawal_amount)
                        customer["balance_checking"] -= 35
                        overdraft_count += 1
                        print(f"Withdrawal successful.and cost for overdraft is \"35\"  New checking balance: ${customer['balance_checking']}")
                        if overdraft_count >= 2:
                            customer["status"] = "deactivated"
                            print("Your account has been deactivated due to excessive overdrafts.")
                        customer["overdraft_count"] = overdraft_count 

                        self.update_csv(customer)
                else:
                    print("You cannot withdraw more than $100 in one transaction.")
            else:
                print("Insufficient balance in checking account.")

        elif account_type == 2:
            if customer["balance_savings"] is not None and customer["balance_savings"] != "":
                savings_balance = float(customer["balance_savings"])
                withdrawal_amount = float(input("Enter the amount to withdraw: $"))
                if withdrawal_amount <= 100:
                    if savings_balance > 0:
                        customer["balance_savings"] = savings_balance - withdrawal_amount
                        print(f"Withdrawal successful. New savings balance: ${customer['balance_savings']}")
                        self.update_csv(customer)
                    else:
                        customer["balance_savings"] = (savings_balance - withdrawal_amount)
                        customer["balance_savings"] -= 35
                        overdraft_count += 1
                        print(f"Withdrawal successful. New savings balance: ${customer['balance_savings']}")
                        if overdraft_count >= 2:
                            customer["status"] = "deactivated"
                            print("Your account has been deactivated due to excessive overdrafts.")
                        customer["overdraft_count"] = overdraft_count       
                        self.update_csv(customer)
                else:
                    print("You cannot withdraw more than $100 in one transaction.")

            else:
                print("Insufficient balance in savings account.")
        else:
            print("Invalid option. Please try again.")

    def update_csv(self, updated_customer):
        updated_customers = []
        with open("bank.csv", "r") as csvfile:
            info_customers = csv.DictReader(csvfile)
            for customer in info_customers:
                if customer["account_id"] == updated_customer["account_id"]:
                    customer["balance_checking"] = updated_customer["balance_checking"]
                    customer["balance_savings"] = updated_customer["balance_savings"]
                    customer["status"] = updated_customer.get("status", "active")
                    customer["overdraft_count"] = updated_customer.get("overdraft_count", 0)
                updated_customers.append(customer)

        with open("bank.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Data.fieldnames)
            writer.writeheader()
            for customer in updated_customers:
                writer.writerow(customer)


class Deposit:
    def __init__(self, login_instance):
        self.login_instance = login_instance

    def deposit_money(self):

        customer = self.login_instance.logged_in_customer

        print("Select the type of account to deposit to:")
        print("1. Checking account")
        print("2. Savings account")
        account_type = int(input("Enter the option number: "))

        if account_type == 1:
            if customer["balance_checking"] is not None and customer["balance_checking"] != "":
                checking_balance = float(customer["balance_checking"])
                deposit_amount = float(input("Enter the amount to deposit : $"))
                customer["balance_checking"] = checking_balance + deposit_amount
                print(f"deposit successful. New checking balance: ${customer['balance_checking']}")
                if (customer["status"] == "deactivated" and customer["balance_checking"] >= 0):
                    customer["overdraft_count"] = 0
                    customer["status"] = "active"
                    print("Your account has been reactivated.")
                self.update_csv(customer)
            else:
                print("Insufficient balance in checking account.")

        elif account_type == 2:
            if customer["balance_savings"] is not None and customer["balance_savings"] != "":
                checking_balance = float(customer["balance_savings"])
                deposit_amount = float(input("Enter the amount to  deposit: $"))
                customer["balance_savings"] = checking_balance + deposit_amount
                print(f" deposit successful. New checking balance: ${customer['balance_savings']}")
                if ( customer["status"] == "deactivated" and customer["balance_checking"] >= 0):
                    customer["overdraft_count"] = 0
                    customer["status"] = "active"
                    print("Your account has been reactivated.")
                self.update_csv(customer)
            else:
                print("Insufficient balance in savings account.")

        else:
            print("Invalid option. Please try again.")

    def update_csv(self, updated_customer):
        updated_customers = []
        with open("bank.csv", "r") as csvfile:
            info_customers = csv.DictReader(csvfile)
            for customer in info_customers:
                if customer["account_id"] == updated_customer["account_id"]:
                    customer["balance_checking"] = updated_customer["balance_checking"]
                    customer["balance_savings"] = updated_customer["balance_savings"]
                    customer["status"] = updated_customer["status"]
                    customer["overdraft_count"] = updated_customer["overdraft_count"]
                updated_customers.append(customer)

        with open("bank.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Data.fieldnames)
            writer.writeheader()
            for customer in updated_customers:
                writer.writerow(customer)


class Transfer :
    def __init__(self, login_instance):
        self.login_instance = login_instance

    def transfer_money(self):
        customer = self.login_instance.logged_in_customer
        if customer.get("status", "active") == "deactivated":
            print("Your account is deactivated. Please add funds to reactivate.")
            return
        print("Select the type of transfer :")
        print("1. Transfer between your accounts")
        print("2. Transfer to another user")
        transfer_type = int(input("Enter the option number: "))
        if  transfer_type == 1:
            if customer["balance_checking"] is not None and customer["balance_checking"] != "" and customer["balance_savings"] is not None and customer["balance_savings"] != "":
                print("Select the type of account to transfer from:")
                print("1. Checking account")
                print("2. Savings account")
                account_type = int(input("Enter the option number: "))
                if account_type == 1:
                    checking_balance = float(customer["balance_checking"])
                    savings_balance = float(customer["balance_savings"])
                    print(f"Checking: ${customer['balance_checking']}\nSavings: ${customer['balance_savings']}")
                    transfer_amount = int(input("Enter the amount to transfer:"))
                    if transfer_amount > checking_balance:
                        print("Insufficient funds in checking account.")
                        return
                    customer["balance_checking"] = checking_balance - transfer_amount
                    customer["balance_savings"] = savings_balance + transfer_amount
                    print(
                        f"Transfer successful! New balances:\nChecking: ${customer['balance_checking']}\nSavings: ${customer['balance_savings']}")
                    self.update_csv(customer)

                if account_type == 2:
                    savings_balance = float(customer["balance_savings"])
                    checking_balance = float(customer["balance_checking"])
                    print(f"Savings: ${customer['balance_savings']}\nChecking: ${customer['balance_checking']}")

                    transfer_amount = int(input("Enter the amount to transfer:"))
                    if transfer_amount > savings_balance:
                        print("Insufficient funds in Savings account.")
                        return
                    customer["balance_savings"] = savings_balance - transfer_amount
                    customer["balance_checking"] = checking_balance + transfer_amount
                    print(f"Transfer successful! New balances:\nSavings: ${customer['balance_savings']}\nChecking: ${customer['balance_checking']}")
                    self.update_csv(customer)

            else :
                print("you have onle one account balance ")
        if transfer_type == 2:
            print("Select the type of account to transfer from:")
            print("1. Checking account")
            print("2. Savings account")
            account_type = int(input("Enter the option number: "))
            if account_type == 1:
                checking_balance = float(customer["balance_checking"])
                print(f"Your checking account balance: ${customer['balance_checking']}")
                transfer_amount = float(input("Enter the amount to transfer:"))
                if transfer_amount > checking_balance:
                    print("Insufficient funds in your checking account.")
                    return
                recipient_account_id = input("Enter the recipient's account ID: ")
                recipient_found = False
                with open("bank.csv", "r") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for recipient in reader:
                        if recipient["account_id"] == recipient_account_id:
                            recipient_found = True
                            recipient_balance = float(recipient["balance_checking"])
                            recipient["balance_checking"] = recipient_balance + transfer_amount
                            print(f"Transfer successful! New balance for recipient's checking account: ${recipient['balance_checking']}")
                            self.update_csv(recipient)
                            break
                if not recipient_found:
                    print("Recipient account not found.")
                    return
            customer["balance_checking"] = checking_balance - transfer_amount
            print(
                f"Your new balance for checking account: ${customer['balance_checking']}"
            )
            self.update_csv(customer)

    def update_csv(self, updated_customer):
        updated_customers = []
        with open("bank.csv", "r") as csvfile:
            info_customers = csv.DictReader(csvfile)
            for customer in info_customers:
                if customer["account_id"] == updated_customer["account_id"]:
                    customer["balance_checking"] = updated_customer["balance_checking"]
                    customer["balance_savings"] = updated_customer["balance_savings"]
                updated_customers.append(customer)
        with open("bank.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Data.fieldnames)
            writer.writeheader()
            for customer in updated_customers:
                writer.writerow(customer)

bank = Bank("Golden Dune Bank")
bank.account()
