# 🏧 ATM System  

Welcome to the **ATM System**! This Python-based project simulates the core functionalities of an ATM machine, allowing users to check their balance, withdraw, and deposit money. This system is built using **Object-Oriented Programming (OOP)** concepts and makes use of **abstract base classes (ABC)** for creating an ATM interface. 💳💰

---

## ✨ Features  

- **💵 Check Balance:** View the current balance available in your account after verifying the pin.
- **💸 Withdraw Money:** Withdraw funds from your account after a successful pin verification, ensuring you have sufficient balance.
- **💰 Deposit Money:** Deposit money into your account after entering the correct pin, with updates to the balance.

The system is secure, and multiple attempts are allowed to enter the correct pin before being locked out. 🔒

---

## 🛠️ Prerequisites  

Before running the program, ensure you have the following installed:  

- **Python 3.x**

---

## 🚀 How to Run the Program  

1. **Clone the Repository:**  
   Use the following command to clone the repository:  
   ```bash  
   git clone https://github.com/Rajdeep-006/ATM-management-system.git  
   ```  
   *(Replace `USERNAME` and `REPOSITORY_NAME` with your actual GitHub username and repository name.)*

2. **Navigate to the Project Folder:**  
   Move into the project directory:  
   ```bash  
   cd REPOSITORY_NAME  
   ```

3. **Run the Program:**  
   Start the program by running:  
   ```bash  
   python atm_system.py  
   ```

4. **Interact with the System:**  
   - Choose an option to check your balance, withdraw, or deposit funds.
   - Enter the correct pin for each transaction.
   - The system ensures the user is given multiple attempts for entering the correct pin.

---

## 📘 About the System  

The system uses an **abstract base class** `ATM` that defines the basic operations (`check_bal`, `withdrawl`, `deposit`) that any ATM machine should have. The **New_ATM** class inherits from `ATM` and implements these operations with the following functionality:  
- **Pin verification**: Ensures the user enters the correct pin for performing any transaction.
- **Balance management**: Allows for withdrawals and deposits while keeping track of the available balance.

---

## 🎯 Project Purpose  

This project was created to:
- 🧑‍💻 Demonstrate the use of **abstract base classes** (ABC) and **inheritance** in Python.
- 💳 Simulate core ATM functionalities in a Python program.
- 🔒 Implement basic security through pin-based authentication for transactions.
- 🌟 Provide an introductory level example for beginners to understand OOP concepts in action.

---

## 🤝 Contribution  

Contributions are welcome! If you'd like to contribute, feel free to:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request for review.

---

## 📜 License  

This project is licensed under the **MIT License**, so feel free to use and modify it for your own needs.  

---

Get started now and experience the ATM system in action! 💳🌟

---

This is formatted and ready for direct copy-pasting into your README file. Let me know if you need any further modifications! 😊
