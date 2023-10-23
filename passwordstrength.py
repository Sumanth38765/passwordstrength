import re

def check_password_strength(password):
    # Check for length
    if len(password) > 8:
        return "Strong"
    elif 6 <= len(password) <= 8:
        return "Medium"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)

    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
