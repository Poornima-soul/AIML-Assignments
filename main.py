def check_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password! Authentication Successful.")
    else:
        print("Password is weak. It must contain:")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one number")
        print("- At least one special character")


# User input
password = input("Enter your password: ")
check_password(password)