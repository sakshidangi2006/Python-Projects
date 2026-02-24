from pathlib import Path
import os

def readFilesOrFolders():
    path = Path('')
    items = list(path.glob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def createFiles():
    try: 
        readFilesOrFolders()
        name = input("please enter you file name: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file: ")
                fs.write(data)

    except Exception as err:
        print(f"error occured as {err}")
               
    print("FILE CREATED SUCCESSFULLY")
        

def readFiles():
    try:
        readFilesOrFolders()
        name = input("which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("READED FILE SUCCESSFULLY")

        else:
            print(f"{name} FILE DOES NOT EXISTS")
    except Exception as err:
        print(f"error occured as {err}")

def updateFiles():
    try:
        readFilesOrFolders()
        name = input("which file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file: ")
            print("press 2 for overwriting the data of your file: ")
            print("press 3 for appending some content in your file: ")

            res = int(input("tell your response: "))

            if res == 1:
                name2 = input("tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,"w") as fs:
                    data = input("tell what you want to write int this overwrites the data: ")
                    fs.write(data)

            if res == 3:
                with open(p,"a") as fs:
                    data = input("what you want to append: ")
                    fs.write(data)
                
            print("FILE UPDATED SUCCESSFULLY")
        else:
            print(f"{name} FILE DOES NOT EXISTS")
        
    except Exception as err:
        print(f"error occured as {err}")

def deleteFiles():
    try: 
        readFilesOrFolders()
        name = input("which file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("FILE DELETED SUCCESSFULLY")
           
        else:
            print(f"{name} FILE DOES NOT EXISTS")
    except Exception as err:
        print(f"error occured as {err}")

print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File")

check = int(input("please tell your response: "))

if check == 1:
    createFiles()

if check == 2:
    readFiles()
 

if check == 3:
    updateFiles()

if check == 4:
    deleteFiles()