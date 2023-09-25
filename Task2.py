import json
import os
from datetime import datetime

# Define global variables
TRANSACTIONS_FILE = "transactions.json"

# Check if the transactions file exists; if not, create an empty file
if not os.path.isfile(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump([], file)


# Function to load transactions from the transactions file
def load_transactions():
    with open(TRANSACTIONS_FILE, "r") as file:
        return json.load(file)


# Function to save transactions to the transactions file
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


# Function to add a new transaction (income or expense)
def add_transaction(transactions):
    transaction_type = input("Enter transaction type (income/expense): ").lower()
    if transaction_type not in ["income", "expense"]:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")
        return

    category = input("Enter category: ")
    amount = float(input("Enter amount: $"))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_transaction = {
        "type": transaction_type,
        "category": category,
        "amount": amount,
        "date": date,
    }

    transactions.append(new_transaction)
    save_transactions(transactions)
    print(f"{transaction_type.capitalize()} added successfully!")


# Function to calculate the remaining budget
def calculate_budget(transactions):
    income = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "income")
    expenses = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "expense")
    remaining_budget = income - expenses
    return remaining_budget


# Function to analyze expenses by category
def analyze_expenses(transactions):
    expense_categories = set(
        transaction["category"] for transaction in transactions if transaction["type"] == "expense")

    print("\nExpense Analysis:")
    for category in expense_categories:
        category_expenses = [transaction["amount"] for transaction in transactions if
                             transaction["category"] == category]
        total_expense = sum(category_expenses)
        print(f"{category}:${total_expense:.2f}")


# Function to display the budget summary
def display_budget_summary(transactions):
    remaining_budget = calculate_budget(transactions)
    print("\nBudget Summary:")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    analyze_expenses(transactions)


# Main function
def main():
    transactions = load_transactions()

    while True:
        print("==Personal Budget Tracker==")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget Summary")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            add_transaction(transactions)
        elif choice == "3":
            display_budget_summary(transactions)
        elif choice == "4":
            save_transactions(transactions)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
