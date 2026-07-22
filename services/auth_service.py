from database import get_connection
from utils.validation import *
from utils.helper import generate_user_id


class AuthService:

    @staticmethod
    def register():

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== USER REGISTRATION ==========\n")

        username = input("Enter Username : ")

        if not valid_username(username):
            print("Username should be less than 50 characters.")
            conn.close()
            return

        email = input("Enter Email : ")

        if not valid_email(email):
            print("Invalid Email.")
            conn.close()
            return

        # Check whether email already exists
        cursor.execute(
            "SELECT * FROM customer WHERE email=?",
            (email,)
        )

        if cursor.fetchone():
            print("Email already registered.")
            conn.close()
            return

        password = input("Enter Password (6-12 chars): ")

        if not valid_password(password):
            print("Password must be between 6 and 12 characters.")
            conn.close()
            return

        address = input("Enter Address : ")

        if not valid_address(address):
            print("Address too long.")
            conn.close()
            return

        contact = input("Enter Contact Number : ")

        if not valid_contact(contact):
            print("Contact must be 10 digits.")
            conn.close()
            return

        user_id = generate_user_id()

        # Ensure generated user_id is unique
        while True:
            cursor.execute(
                "SELECT 1 FROM customer WHERE user_id=?",
                (user_id,)
            )
            if cursor.fetchone():
                user_id = generate_user_id()
            else:
                break

        cursor.execute("""
        INSERT INTO customer
        VALUES(?,?,?,?,?,?)
        """,
        (
            user_id,
            username,
            email,
            password,
            address,
            contact
        ))

        conn.commit()
        conn.close()

        print("\nRegistration Successful!")
        print("Your User ID :", user_id)

    @staticmethod
    def login():

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== LOGIN ==========\n")

        email = input("Email : ")
        password = input("Password : ")

        cursor.execute("""
        SELECT *
        FROM customer
        WHERE email=? AND password=?
        """,
        (email, password))

        user = cursor.fetchone()

        conn.close()

        if user:
            print("\nLogin Successful.\n")
            return user[0]      # Return User ID

        print("Invalid Email or Password.")
        return None