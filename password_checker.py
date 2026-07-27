import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    print("\nPassword Strength Report")
    print("-" * 30)

    if score == 5:
        print("✅ Strong Password")
    elif score >= 3:
        print("🟡 Moderate Password")
    else:
        print("🔴 Weak Password")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")

password = input("Enter your password: ")
check_password_strength(password)
