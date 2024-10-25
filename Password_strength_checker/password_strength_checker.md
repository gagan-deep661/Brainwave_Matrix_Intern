import re

# Define a list of common passwords
common_passwords = ['123456', 'password', '12345678', 'qwerty', 'abc123']

def check_password_strength(password):
    score = 0

    # Check if the password is in the common passwords list
    if password in common_passwords:
        return "Very Weak - Common Password"

    # Length Check
    if len(password) >= 8:
        score += 1

    # Complexity Checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    # Feedback based on the score
    if score < 3:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong"

# Main block to test the function
if __name__ == "__main__":
    test_password = input("Enter a password to check its strength: ")
    print(f"Password strength: {check_password_strength(test_password)}")
