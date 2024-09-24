import re

def password_strength(password):
    """
    Check the strength of a password
    """
    strength = 0

    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1

    # Evaluate password strength
    if strength == 1:
        return "Password is weak. It should have at least two types of characters."
    elif strength == 2:
        return "Password is medium. It should have at least three types of characters."
    elif strength == 3:
        return "Password is strong. It has three types of characters."
    elif strength == 4:
        return "Password is very strong. It has all four types of characters."

# Test the function
password = input("Enter a password: ")
print(password_strength(password))