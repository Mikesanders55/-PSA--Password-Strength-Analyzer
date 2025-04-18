import re

def check_password_strength(password):
    score = 0
    reasons = []

    # Minimum length check
    if len(password) >= 12:
        score += 1
    else:
        reasons.append("❌ Password should be at least 12 characters long.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        reasons.append("❌ Add at least one lowercase letter.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        reasons.append("❌ Add at least one uppercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        reasons.append("❌ Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        reasons.append("❌ Use at least one special character (e.g., !, @, #).")

    # Final rating
    if score <= 2:
        rating = "Weak 🔴"
    elif score == 3 or score == 4:
        rating = "Moderate 🟡"
    else:
        rating = "Strong 🟢"

    return rating, reasons

# Main program
if __name__ == "__main__":
    pwd = input("🔐 Enter a password to check: ")
    print("🔎 Analyzing...\n")
    
    rating, feedback = check_password_strength(pwd)
    print(f"💬 Password Strength: {rating}\n")

    if feedback:
        print("🧠 Suggestions to improve your password:")
        for f in feedback:
            print(f"   {f}")
    else:
        print("✅ Your password meets all recommended requirements!")

    input("\n🔁 Press Enter to exit...")