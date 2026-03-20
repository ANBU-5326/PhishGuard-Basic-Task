# ==========================================
# PhishGuard Basic Prototype
# Simple Phishing Detection Tool
# ==========================================


# -------------------------------
# Task 1: Email Risk Checker
# -------------------------------

def check_email_risk(email_text):

    # List of risky phishing keywords
    risky_words = ["urgent", "verify", "password", "bank", "click"]

    email_text = email_text.lower()

    for word in risky_words:
        if word in email_text:
            return "Warning: This email may be risky"

    return "This email looks safe"


# -------------------------------
# Task 2: Domain Similarity Check
# -------------------------------

def normalize_domain(domain):
    """
    Replace common phishing character tricks
    Example:
    g00gle.com → google.com
    """

    domain = domain.lower()

    replacements = {
        "0": "o",
        "1": "l",
        "3": "e",
        "@": "a"
    }

    for key in replacements:
        domain = domain.replace(key, replacements[key])

    return domain


def check_domain(domain1, domain2):

    d1 = normalize_domain(domain1)
    d2 = normalize_domain(domain2)

    if d1 == d2:
        return "Suspicious domain"

    # Check if main part of domain is similar
    if d1.split(".")[0] == d2.split(".")[0]:
        return "Suspicious domain"

    return "Domain looks safe"


# -------------------------------
# Main Program
# -------------------------------

def main():

    print("=================================")
    print(" PhishGuard Basic Security Tool")
    print("=================================")

    # Task 1
    print("\nTask 1: Email Risk Detection")

    email_text = input("Enter email text: ")

    result = check_email_risk(email_text)

    print(result)


    # Task 2
    print("\nTask 2: Domain Similarity Check")

    domain1 = input("Enter first domain: ")
    domain2 = input("Enter second domain: ")

    result2 = check_domain(domain1, domain2)

    print(result2)


# Run program
if __name__ == "__main__":
    main()