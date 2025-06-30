def is_valid_email(email):

    if email.count('@') != 1:
        return False

    username, domain = email.split('@')

    if '.' not in domain:
        return False

    return True

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
