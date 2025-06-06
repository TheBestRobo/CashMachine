# ATM GUI Application

A basic ATM (Automated Teller Machine) simulation built with Python's `tkinter` library. Users can log in using a simple password prompt and perform standard ATM operations: deposit money, withdraw funds, check balance, or exit the application. The GUI is fully interactive and updates dynamically based on user actions.

## Features

- **Login Screen**: Simple password prompt before accessing the ATM interface.
- **Deposit Funds**: Enter any amount to add to your balance.
- **Withdraw Funds**: Enter an amount to subtract from your balance.
- **Check Balance**: Displays the current account balance.
- **User Interface**:
  - Built using `tkinter` grid layout
  - Buttons, entry fields, and labels used throughout
  - View dynamically changes with user interaction

## Screenshots

*Add screenshots here if available*

## Prerequisites

- Python 3.x
- `tkinter` (included with standard Python installations)

## How It Works

1. **Startup**: Launch the app and enter the password (`1`) to log in.
2. **Main Menu**:
   - **Deposit**: Input a value and click "OK" to add to the balance.
   - **Withdraw**: Input a value and click "OK" to deduct from the balance.
   - **Balance**: Displays the current amount in your account.
   - **Exit**: Returns to the main menu or closes the app.
3. **Account Balance**: Starts at `$1000` by default.
