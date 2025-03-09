# 1.0 Import the csv and os packages:
import csv
import os

# 1.1 Seed Data to CSV
bank_info = [
    { 'account_id':'1001', 'frst_name':'suresh', 'last_name':'sigera', 'password':'juagw362' ,   'balance_checking' :1000 ,  'balance_savings' :10000},
    { 'account_id':'1002', 'frst_name':'james',  'last_name':'taylor', 'password':'idh36%@#FGd', 'balance_checking' :10000,  'balance_savings' :10000}, 
    { 'account_id':'1003', 'frst_name':'melvin', 'last_name':'gordon', 'password':'uYWE732g4ga1','balance_checking' :2000 ,  'balance_savings' :20000}, 
    { 'account_id':'1004', 'frst_name':'stacey', 'last_name':'abrams', 'password':'DEU8_qw3y72$','balance_checking' :2000,   'balance_savings' :20000}, 
    { 'account_id':'1005', 'frst_name':'jake',   'last_name':'paul',   'password':'d^dg23g)@',   'balance_checking' :100000, 'balance_savings' :100000}
]

# 2.0 Set fieldnames once:
fieldnames = ["account_id", "frst_name", "last_name","password","balance_checking","balance_savings"]

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
try: 
    with open("bank.csv", "r") as file:
        contents = csv.DictReader(file)
        for row in contents:
            print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
            for prop in fieldnames:
                print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)


# 5.0 Add Individual Row => "a+" option will allow reading and APPENDING to file
try:
    new_row = {'account_id':'1006', 'frst_name':'shahd', 'last_name':'sh', 'password':'juagw33362' ,   'balance_checking' :10000000 ,  'balance_savings' :100000000}
    with open("bank.csv", "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)
except csv.Error as e:
    print(e)


# 6.0 Updating A row
# --- There is no no way to directly update one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to update an individual item and rewrite the entire file.
# --- we will walk through this process in class.



# 7.0 Deleting A Row
# --- There is no no way to directly delete one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to delete an individual item and rewrite the entire file.
# --- we will walk through this process in class.