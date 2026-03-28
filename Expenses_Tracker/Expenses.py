import csv
from pathlib import Path

FILE_NAME = "expenses.txt"

def get_valid_int(prompt):
    """Helper to ensure we get a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def add_expense():
    amount = get_valid_int("Enter your amount: ")
    category = input("Enter category: ").strip()
    name = input("Enter name: ").strip()
    
    # Using CSV writer handles formatting and special characters automatically
    with open(FILE_NAME, "a", newline="") as fs:
        writer = csv.writer(fs)
        writer.writerow([name, category, amount])
    
    print(f"Successfully added {name} (${amount}) to {category}.")

def view_expenses():
    if not Path(FILE_NAME).exists():
        print("\nNo expenses found yet.")
        return

    print(f"\n{'Name':<15} | {'Category':<15} | {'Amount':<10}")
    print("-" * 45)
    
    with open(FILE_NAME, "r") as fs:
        reader = csv.reader(fs)
        for row in reader:
            if row:
                name, cat, amt = row
                print(f"{name:<15} | {cat:<15} | ${amt:<10}")

def calculate_total():
    if not Path(FILE_NAME).exists():
        print("\nNo expenses to calculate.")
        return

    total = 0
    with open(FILE_NAME, "r") as fs:
        reader = csv.reader(fs)
        for row in reader:
            if row:
                total += int(row[2])
    
    print(f"\n>>> Total Expenses: ${total}")

def delete_all():
    confirm = input("Are you sure you want to clear all data? (y/n): ").lower()
    if confirm == 'y':
        open(FILE_NAME, "w").close()
        print("All records cleared.")

def main():
    menu = {
        "1": ("Add Expense", add_expense),
        "2": ("View Expenses", view_expenses),
        "3": ("Calculate Total", calculate_total),
        "4": ("Delete All Records", delete_all),
        "5": ("Exit", exit)
    }

    while True:
        print("\n--- EXPENSE TRACKER ---")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")
        
        choice = input("Select an option: ")
        
        if choice in menu:
            if choice == "5":
                print("Goodbye!")
                break
            menu[choice][1]()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()