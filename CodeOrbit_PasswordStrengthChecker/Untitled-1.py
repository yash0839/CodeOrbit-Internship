def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Display result
    if score == 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)


# Main program

print("   PASSWORD STRENGTH CHECKER")
password = input("Enter your password: ")
check_password_strength(password)




# anyother code 


print("     PASSWORD STRENGTH CHECKER")

max_attempts = 3

for attempt in range(1, max_attempts + 1):

    print(f"\nAttempt {attempt} of {max_attempts}")

    password = input("Enter your password: ")

    # Conditions
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    # Check each character
    for char in password:

        if char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

        elif char.isdigit():
            has_number = True

        else:
            has_special = True

    # Check length
    has_length = len(password) >= 8

    # Calculate score
    score = 0

    if has_length:
        score += 1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_number:
        score += 1

    if has_special:
        score += 1

    print("\n========== RESULT ==========")

    # Strong password
    if score == 5:
        print("Password Strength: STRONG")
        print("Your password meets all security requirements.")
        print("Password accepted!")
        break

    # Medium password
    elif score >= 3:
        print("Password Strength: MEDIUM")
        print("Your password can be improved.")

    # Weak password
    else:
        print("Password Strength: WEAK")

    # Suggestions
    print("\nHow to improve your password:")

    if not has_length:
        print("- Use at least 8 characters.")

    if not has_uppercase:
        print("- Add at least one uppercase letter.")

    if not has_lowercase:
        print("- Add at least one lowercase letter.")

    if not has_number:
        print("- Add at least one number.")

    if not has_special:
        print("- Add at least one special character.")

    # Attempts remaining
    if attempt < max_attempts:
        print(f"\nTry again. Attempts remaining: {max_attempts - attempt}")

    else:
        print("\nMaximum 3 attempts reached.")
        print("Password was not accepted.")


print("PROGRAM ENDED")
