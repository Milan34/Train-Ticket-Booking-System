import re


def valid_email(email):

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email)


def valid_password(password):

    return 6 <= len(password) <= 12


def valid_contact(contact):

    return contact.isdigit() and len(contact) == 10


def valid_username(username):

    return len(username) <= 50


def valid_address(address):

    return len(address) <= 100