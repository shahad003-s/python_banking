# Golden Dune Bank - Python Banking System

![Golden Dune Bank](./Golden%20Dune%20Bank%20(3).png)


## Project Description

Welcome to the Golden Dune Bank Python Banking System! This project simulates a banking environment where customers can have checking and savings accounts, withdraw and deposit money, transfer funds, and more. The system also implements overdraft protection and ensures that customers can only access their own information. It uses Python classes, file handling, and the CSV module to manage data.

The goal of this project is to showcase how to build a simple, but functional banking application using Python and the CSV format to store account data.

---

## Technologies Used
- **Python 3.x**  
- **CSV module** (for reading and writing account data)

---

## App Functionality / User Stories
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

## Challenges / Key Takeaways
- No challenges yet! If any challenges arise during the development process, I will update this section accordingly. Stay tuned!


---
### To Run the Project:

1. `bank.csv`: Contains account information. It is used to persist data.
2. `banking.py`: Contains all the Python code for handling user interactions. It also manages account creation and overdraft protection.
3. `bank_csv.py`: Used to create and populate the `bank.csv` file with some initial data if it's missing.

---

### To Run the Project:

1. If the `bank.csv` file doesn't already exist, run `bank_csv.py` to generate initial data.
2. Run `banking.py` to start the banking application.
3. Follow the prompts to interact with the system.
---
**Enjoy coding and happy banking! 💸**
