# Golden Dune Bank - Python Banking System

![Golden Dune Bank](./Golden%20Dune%20Bank%20(3).png)


## Project Description

Welcome to the Golden Dune Bank Python Banking System! This project simulates a banking environment where customers can have checking and savings accounts, withdraw and deposit money, transfer funds, and more. The system also implements overdraft protection and ensures that customers can only access their own information. It uses Python classes, file handling, and the CSV module to manage data.

The goal of this project is to showcase how to build a simple, but functional banking application using Python and the CSV format to store account data.

---

## Technologies Used
- **Python** :A powerful and flexible programming language used to implement the project's.
- **CSV module** :for reading and writing account data
- **GitHub**: A version control and collaboration platform that helps manage code efficiently, track changes. 

---

## App Functionality / User Stories 🏦
| Feature                          | Description |
|-----------------------------------|-------------|
| **Add New Customer**              | Add a new customer with checking and/or savings account |
| **Withdraw Money**                | Customers can withdraw from checking or savings accounts (requires login) |
| **Deposit Money**                 | Customers can deposit into checking or savings accounts |
| **Transfer Money Between Accounts** | Transfer between checking and savings or to another customer |
| **Overdraft Protection**          | Prevent overdraft beyond $100 and apply a $35 fee on overdrafts |
| **Deactivate Account**            | Deactivate an account after 2 overdrafts |
| **Reactivate Account**            | Reactivate account once overdraft fees and balance are cleared |
| **Customer Login/Logout**         | Customers can login and logout, and access only their own information |
| **Account Withdraw Restrictions** | Customers cannot withdraw more than $100 if account balance is negative |
| **Account Withdraw Limits**       | Customers cannot withdraw more than $100 in a single transaction |


---

## Challenges / Key Takeaways ⚠️
- Printing the Last Line of a File Read in with CSV in Python 
  - By using Python’s csv module, you can read the file into a list of lines using the readlines() method. 
  - After reading the file, the last line can be accessed using negative indexing (lines[-1]). 

  - Initially, I didn’t have a background on how to do this efficiently, but after some research, I learned how to handle it.

- Challenges of Implementing Multiple Withdrawal Conditions
  - condition must be checked in sequence, making sure that conditions (e.g., withdrawal limits, overdraft fees, account deactivation) are applied correctly without interfering with one another.
- Updating Information in a CSV File

  - The main difficulty was updating a specific column in the CSV file without altering other data. Since CSV files don’t support direct modifications like databases, I had to read all the data, modify only the necessary field (such as balance), and then rewrite the entire file while preserving its structure.

---
### IceBox Features 🧊
- Index all transactions for a customer account.

- If a customer has only a savings account and does not have a checking account, they can open a checking account to have both types of accounts.

- Account suspension applies to a single account only, meaning if the overdraft limit is exceeded on a checking account, only that account is deactivated, while the savings account remains active (and vice versa).


---

### Refernces :
- Print Last Line of File Read In with Python 
(https://stackoverflow.com/questions/37227909/print-last-line-of-file-read-in-with-python)
`f1 = open(inputFile, "r")
last_line = f1.readlines()[-1]
f1.close()`


---
** 💃 💃money money! 💸 🏆 **

![gif](https://media.giphy.com/media/ADgfsbHcS62Jy/giphy.gif)