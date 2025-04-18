import re

def check_password_strength(password):
    score = 0

    # New minimum length requirement: 12
    if len(password) >= 12:
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score == 3 or score == 4:
        return "Moderate 🟡"
    else:
        return "Strong 🟢"

if __name__ == "__main__":
    pwd = input("🔐 Enter a password to check: ")
    print("🔎 Analyzing...")
    result = check_password_strength(pwd)
    print(f"💬 Password Strength: {result}")
