import csv
import os
class Data:
# 1.0 Import the csv and os packages:
# 1.1 Seed Data to CSV
 bank_info = [
    { 'account_id':'10001', 'first_name':'suresh', 'last_name':'sigera', 'password':'juagw362' ,   'balance_checking' :1000 ,  'balance_savings' :10000},
    { 'account_id':'10002', 'first_name':'james',  'last_name':'taylor', 'password':'idh36%@#FGd', 'balance_checking' :10000,  'balance_savings' :10000}, 
    { 'account_id':'10003', 'first_name':'melvin', 'last_name':'gordon', 'password':'uYWE732g4ga1','balance_checking' :2000 ,  'balance_savings' :20000}, 
    { 'account_id':'10004', 'first_name':'stacey', 'last_name':'abrams', 'password':'DEU8_qw3y72$','balance_checking' :2000,   'balance_savings' :20000}, 
    { 'account_id':'10005', 'first_name':'jake',   'last_name':'paul',   'password':'d^dg23g)@',   'balance_checking' :100000, 'balance_savings' :100000}
]
# 2.0 Set fieldnames once:
 fieldnames = ["account_id", "first_name", "last_name","password","balance_checking","balance_savings"]
# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
 if not os.path.exists("./bank.csv"):
    with open("./bank.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in bank_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile / Rows:
#  try: 
#     with open("bank.csv", "r") as file:
#         contents = csv.DictReader(file)
#         for row in contents:
#             print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
#             for prop in fieldnames:
#                 print(row[prop]) # will print the value of each individual property
#  except csv.Error as e:
#     print(e)

class Bank:
    def __init__(self, name):
        bank_csv = open("bank.csv", "r")
        last_account = bank_csv.readlines()[-1]
        last_account = last_account.split(',')
        last_account_id = int(last_account[0])
        self.name=name
        self.fieldnames = ["account_id", "first_name", "last_name","password","balance_checking","balance_savings"]
        #find the current highest account number in the csv
        last_account_id += 1
        self.account_id = str(last_account_id)

    def add_customer(self, customer):
        try:
           with open("bank.csv", "a+",newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(customer)
        except csv.Error as e:
               print(e)

    def create_account(self):
      create_account = input(" Do you want create an account? y for yes n for no\n").lower()
      if create_account == "y" :
         first_name = input("Enter first name: ")
         last_name = input("Enter last name: ")
         password = input("Enter password: ")
         print("Select the type of account(s):")
         print("1. Checking account")
         print("2. Savings account")
         print("3. Both checking and savings accounts")
         balance_checking = None
         balance_savings = None
         balance= True
         while balance :
          account_type = int(input("Enter the option number: "))
          if account_type == 1 :
            balance_checking = float(input("Enter checking balance: "))
            balance=False
          elif account_type == 2 :
            balance_savings = float(input("Enter savings balance: "))
            balance=False
          elif account_type == 3 :
            balance_checking = float(input("Enter checking balance: "))
            balance_savings = float(input("Enter savings balance: "))
            balance=False
          else :
            print("Invalid option. No account created.")
            balance=True
            
         new_customer = {
        'account_id': self.account_id,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'balance_checking': balance_checking,
        'balance_savings': balance_savings
         }
         self.add_customer(new_customer)
         print(f"Account created successfully! Account ID: {self.account_id}")
      else:
         print("have nice day")

class Customer_Login_Logout :
    def __init__(self):
      self.logged_in_customer = None
 
    def login(self):
        idNumber = input ("Enter your Account ID: ")
        username = input("Enter your first name: ")
        password = input("Enter your password: ")
        with open("bank.csv", "r") as bank_csv:
            reader = csv.DictReader(bank_csv)
            for customer in reader:
                if customer["account_id"] == idNumber and customer["first_name"] == username and customer["password"] == password:
                        print(f"Welcome, {customer['first_name']}! You are now logged in.\n")
                        print("Account details:\n")
                        print(f"{customer['account_id']}, {customer['first_name']}, {customer['last_name']}, {customer['balance_checking']}, {customer['balance_savings']}")
                        self.logged_in_customer = customer
                        return customer
            else:
             print("Invalid credentials. Please try again.")

    def logout(self):
         if self.logged_in_customer:
            logout_account = input("Do you want to logout? y for yes n for no\n").lower()
            if logout_account == "y":
                print("You have logged out. Have a nice day!")
                self.logged_in_customer = None
            else:
                print("You are still logged in.")
         else:
           print("No user logged in.")
          
class Withdraw :
   def __init__(self, login_instance):
        self.login_instance = login_instance
        self.overdraft_count = {}

   
   def withdraw_money (self) :
       if not self.login_instance.logged_in_customer:
            print("You need to log in first.")
            return
        
       customer = self.login_instance.logged_in_customer
       account_id = customer["account_id"]
       
       if account_id not in self.overdraft_count:
        self.overdraft_count[account_id] = 0 

       print("Select the type of account to withdraw from:")
       print("1. Checking account")
       print("2. Savings account")
      

       
       account_type = int(input("Enter the option number: "))
       if account_type == 1:
         if customer["balance_checking"] is not None and customer["balance_checking"] != '':
               checking_balance = float(customer["balance_checking"])
               withdrawal_amount = float(input("Enter the amount to withdraw: $"))
               
               if checking_balance >= withdrawal_amount:
                  customer["balance_checking"] = checking_balance - withdrawal_amount
                  print(f"Withdrawal successful. New checking balance: ${customer['balance_checking']}")

          
         else:
            print("Insufficient balance in checking account.")

       elif account_type == 2:
         if customer["balance_savings"] is not None and customer["balance_savings"] != '':
                savings_balance = float(customer["balance_savings"])
                withdrawal_amount = float(input("Enter the amount to withdraw: $"))

                if savings_balance >= withdrawal_amount:
                    customer["balance_savings"] = savings_balance - withdrawal_amount
                    print(f"Withdrawal successful. New savings balance: ${customer['balance_savings']}")
         else:
            print("Insufficient balance in savings account.")
         
      
class Deposit :
     def __init__(self, login_instance):
        self.login_instance = login_instance
        

    
 	

 	







# bank = Bank("Golden Dune Bank")
# bank.create_account()
log=Customer_Login_Logout()
log.login()
# log.logout()
withdraw = Withdraw(log)
withdraw.withdraw_money()












    