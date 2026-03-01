import json
import string
import random
from pathlib import Path
import getpass


class Bank:
    database = 'data.json'
    data = []

    def __init__(self):
        
        if not Bank.data:  # Load only once
            try:
                if Path(Bank.database).exists():
                    with open(Bank.database, 'r') as fs:
                        Bank.data = json.loads(fs.read())
                else:
                    print("No such file exists, starting fresh.")
            except Exception as err:
                print(f"An error occurred: {err}")

    @staticmethod
    def __update():
        #Save data to JSON file.

        try:
            with open(Bank.database, "w") as fs:
                json.dump(Bank.data, fs, indent=4)
        except Exception as err:
            print(f"Failed to update database: {err}")

    @classmethod
    def __accountGenerator(cls):
        
        while True:
            num = random.choices(string.digits, k=14)
            random.shuffle(num)
            account_no = "".join(num)
            
            if not any(acc['accountNo.'] == account_no for acc in Bank.data):
                return account_no

    def createAccount(self):
       
        try:
            info = {
                "name": input("Write your name here: ").strip(),
                "father's name": input("Write your father's name here: ").strip(),
                "age": int(input("Write your age here: ").strip()),
                "email": input("Write your email here: ").strip(),
                "pin": int(input("Write your 4-digit PIN here: ").strip()),
                "accountNo.": Bank.__accountGenerator(),
                "balance": 0
            }

            if info['age'] < 18 or len(str(info['pin'])) != 4:
                print("Sorry, you cannot create your account.")
            else:
                print("Your account has been created successfully.")
                for k, v in info.items():
                    print(f"{k} : {v}")
                print("Please note down your account number.")

                Bank.data.append(info)
                Bank.__update()

        except ValueError:
            print("Invalid input. Please enter numbers for age and PIN.")
        except Exception as err:
            print(f"An error occurred: {err}")

    def depositMoney(self):
        
        try:
            accNumber = input("What is your Account Number: ").strip()
            pin = int(getpass.getpass("Enter your PIN: ").strip())

            userdata = [i for i in Bank.data if i['accountNo.'] == accNumber and i['pin'] == pin]
            if not userdata:
                print("Sorry, no data found.")
                return

            amount = int(input("How much do you want to deposit? ").strip())
            if amount > 50000 or amount <= 0:
                print("Deposit amount must be between 1 and 50,000.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"{amount} deposited successfully.")

        except ValueError:
            print("Invalid input. Amount and PIN must be numbers.")
        except Exception as err:
            print(f"An error occurred: {err}")

    def withdrawMoney(self):
       
        try:
            accNumber = input("Please tell your Account Number: ").strip()
            pin = int(getpass.getpass("Please tell your PIN: ").strip())

            userdata = [i for i in Bank.data if i['accountNo.'] == accNumber and i['pin'] == pin]
            if not userdata:
                print("Sorry, no data found.")
                return

            amount = int(input("How much amount do you want to withdraw? ").strip())

            if amount <= 0 or amount > 25000:
                print("Withdrawal amount must be between 1 and 25,000.")
            elif amount > userdata[0]['balance']:
                print(f"Invalid amount! Your current balance is: {userdata[0]['balance']}")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"You withdrew {amount} successfully.")

        except ValueError:
            print("Invalid input. Amount and PIN must be numbers.")
        except Exception as err:
            print(f"An error occurred: {err}")

    def accountDetails(self):

        try:
            username = input("Please tell your name: ").strip()
            fathername = input("Please tell your father's name: ").strip()
            userdetail = [i for i in Bank.data if i['name'] == username and i['father\'s name'] == fathername]

            if not userdetail:
                print("No user found.")
                return

            for k, v in userdetail[0].items():
                print(f"{k} : {v}")

        except Exception as err:
            print(f"An error occurred: {err}")

    def updateDetails(self):
      
        try:
            username = input("Please enter your name: ").strip()
            fathername = input("Please enter your father's name: ").strip()
            userdetail = [i for i in Bank.data if i['name'] == username and i['father\'s name'] == fathername]

            if not userdetail:
                print("No user found!")
                return

            print("press 1 to update your name")
            print("press 2 to update your father's name")
            print("press 3 to update your age")
            print("press 4 to update your email")
            print("press 5 to update your PIN")

            choice = int(input("What do you want to update? ").strip())

            if choice == 1:
                userdetail[0]['name'] = input("Please update your name: ").strip()
            elif choice == 2:
                userdetail[0]['father\'s name'] = input("Please update your father's name: ").strip()
            elif choice == 3:
                userdetail[0]['age'] = int(input("Please update your age: ").strip())
            elif choice == 4:
                userdetail[0]['email'] = input("Please update your email: ").strip()
            elif choice == 5:
                userdetail[0]['pin'] = int(input("Please update your 4-digit PIN: ").strip())
            else:
                print("Invalid choice.")
                return

            Bank.__update()
            print("Details updated successfully.")

        except ValueError:
            print("Invalid input. Age and PIN must be numbers.")
        except Exception as err:
            print(f"An error occurred: {err}")

    def deleteAccount(self):
        
        try:
            username = input("Please enter your name: ").strip()
            fathername = input("Please enter your father's name: ").strip()
            userdetail = [i for i in Bank.data if i['name'] == username and i['father\'s name'] == fathername]

            if not userdetail:
                print("No user found!")
                return
            else:
                check = input("press y if you actually want to delete your account or press n ") 
                if check == "n" or check == "N": 
                    print("Bypassed")
                else:
                    Bank.data.remove(userdetail[0])
                    print("Account deleted successfully.") 
                    Bank.__update()

        except Exception as err:
            print(f"An error occurred: {err}")



print("press 1 to create your account")
print("press 2 to deposit money in your account")
print("press 3 to withdraw money from your account")
print("press 4 to check your account details")
print("press 5 to update your account details")
print("press 6 to delete your account")
print("press 7 to exit")

try:
    check = int(input("Tell your choice: ").strip())
except ValueError:
    check = 0

user = Bank()

if check == 1:
    user.createAccount()
elif check == 2:
    user.depositMoney()
elif check == 3:
    user.withdrawMoney()
elif check == 4:
    user.accountDetails()
elif check == 5:
    user.updateDetails()
elif check == 6:
    user.deleteAccount()
elif check == 7:
    print("Thank you for using our bank system.")
else:
    print("Invalid choice, please choose from 1-7 only.")