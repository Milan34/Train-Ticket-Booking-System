import re

def is_blank(value):
    return value.strip() == ""
def valid_email(email):
    email = email.strip()

    if email == "":
        return False

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email)


def valid_password(password):
    password = password.strip()

    if password == "":
        return False

    # Length should be between 6 and 12
    if len(password) < 6 or len(password) > 12:
        return False

    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # At least one digit
    if not re.search(r"\d", password):
        return False

    # At least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True



def valid_contact(contact):
    contact = contact.strip()

    return contact.isdigit() and len(contact) == 10


def valid_username(username):
    username = username.strip()

    if username == "":
        return False

    return len(username) <= 50


def valid_address(address):
    address = address.strip()

    if address == "":
        return False

    return len(address) <= 100

def valid_train_name(train_name):

    train_name = train_name.strip()

    if train_name == "":
        return False

    return len(train_name) <= 100

def valid_location(location):

    location = location.strip()

    if location == "":
        return False

    return len(location) <= 50

def valid_time(time):

    time = time.strip()

    if time == "":
        return False

    pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'

    return re.match(pattern, time)