email = input("Enter your Email: ")
k, d = 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue 
                    else:
                        d = 1

                if k == 1:
                    print("Email cannot contain spaces")
                elif d == 1:
                    print("Email contains invalid special characters")
                else:
                    print("Valid Email ✅")
            else:
                print("There should be a dot (.) at position -3 or -4")
        else:
            print("Email must have exactly one @ symbol")
    else:
        print("First letter should be an alphabet")
else:
    print("Length must be at least 6 characters")