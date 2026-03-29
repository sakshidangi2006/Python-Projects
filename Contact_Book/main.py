import json
from pathlib import Path
import shutil

DATABASE = 'data.json'
contacts = {}

def load_data():
    """Loads data from JSON into the contacts dictionary."""
    global contacts
    db_path = Path(DATABASE)
    if db_path.exists():
        try:
            with open(db_path, 'r') as f:
                # Convert list back to dict for faster access
                data_list = json.load(f)
                contacts = {c['name'].lower(): c for c in data_list}
        except (json.JSONDecodeError, IOError):
            print("Database corrupted. Starting fresh.")
    else:
        print("Starting with a new database.")

def save_data():
    """Backs up and saves the current contacts."""
    try:
        if Path(DATABASE).exists():
            shutil.copy(DATABASE, f"{DATABASE}.bak")
        
        with open(DATABASE, "w") as f:
            # Save as a list for a cleaner JSON format
            json.dump(list(contacts.values()), f, indent=4)
    except Exception as e:
        print(f"Save failed: {e}")

def add_contact():
    name = input("Enter name: ").strip()
    if not name: return print("Name required.")
    
    if name.lower() in contacts:
        return print("Contact already exists!")

    number = input("Enter 10-digit number: ").strip()
    if not (number.isdigit() and len(number) == 10):
        return print("Invalid number.")

    contacts[name.lower()] = {"name": name, "number": number}
    save_data()
    print("Contact saved!")

def view_contacts():
    if not contacts:
        return print("No contacts found.")
    
    print(f"\n{'Name':<20} | {'Number':<15}")
    print("-" * 38)
    # Sorting by the original name
    for c in sorted(contacts.values(), key=lambda x: x['name'].lower()):
        print(f"{c['name']:<20} | {c['number']:<15}")

def search_contact():
    query = input("Search name: ").strip().lower()
    # Partial matching using list comprehension
    results = [c for name_key, c in contacts.items() if query in name_key]
    
    if not results:
        return print("No matches.")
    
    for c in results:
        print(f"Found: {c['name']} - {c['number']}")

def update_contact():
    old_name = input("Name to update: ").strip().lower()
    if old_name not in contacts:
        return print("Not found.")

    target = contacts[old_name]
    new_name = input(f"New name (leave blank for {target['name']}): ").strip()
    new_number = input(f"New number (leave blank for {target['number']}): ").strip()

    if new_name:
        # Remove old key and add new one
        new_name_key = new_name.lower()
        if new_name_key in contacts and new_name_key != old_name:
            return print("New name already exists.")
        del contacts[old_name]
        target['name'] = new_name
        contacts[new_name_key] = target
    
    if new_number:
        if new_number.isdigit() and len(new_number) == 10:
            target['number'] = new_number
        else:
            print("Invalid number. Keeping old one.")

    save_data()
    print("Updated!")

def delete_contact():
    name = input("Name to delete: ").strip().lower()
    if contacts.pop(name, None):
        save_data()
        print("Deleted.")
    else:
        print("Not found.")

def main():
    load_data()
    menu = {
        "1": add_contact, "2": view_contacts, "3": search_contact,
        "4": update_contact, "5": delete_contact
    }
    
    while True:
        print("\n1. Add | 2. View | 3. Search | 4. Update | 5. Delete | 6. Exit")
        choice = input("Choice: ").strip()
        
        if choice == "6":
            print("Goodbye!"); break
        
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()