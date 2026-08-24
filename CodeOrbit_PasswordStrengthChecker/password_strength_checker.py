
def check_password_strength(password):
    
    length_ok = len(password) >= 8
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

   
    if length_ok and has_upper and has_lower and has_digit and has_special:
        print(" Strong password!")
    else:
        print(" Weak password. Suggestions:")
        if not length_ok:
            print("- Make it at least 8 characters long.")
        if not has_upper:
            print("- Add at least one uppercase letter (A-Z).")
        if not has_lower:
            print("- Add at least one lowercase letter (a-z).")
        if not has_digit:
            print("- Include at least one number (0-9).")
        if not has_special:
            print("- Use at least one special character (!@#$%^&* etc.).")


user_password = input("Enter your password: ")
check_password_strength(user_password)