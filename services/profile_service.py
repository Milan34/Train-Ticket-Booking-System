from database import get_connection
from utils.validation import *


class ProfileService:

    @staticmethod
    def view_profile(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM customer
        WHERE user_id=?
        """,
        (user_id,))

        user = cursor.fetchone()

        conn.close()

        if user:

            print("\n========== PROFILE ==========")

            print("User ID :", user[0])
            print("Username :", user[1])
            print("Email :", user[2])
            print("Address :", user[4])
            print("Contact :", user[5])

        else:
            print("Profile not found.")

    @staticmethod
    def update_profile(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== UPDATE PROFILE ==========\n")

        username = input("New Username : ")

        if not valid_username(username):
            print("Invalid Username")
            conn.close()
            return

        address = input("New Address : ")

        if not valid_address(address):
            print("Invalid Address")
            conn.close()
            return

        contact = input("New Contact : ")

        if not valid_contact(contact):
            print("Invalid Contact")
            conn.close()
            return

        cursor.execute("""
        UPDATE customer
        SET username=?,
            address=?,
            contact=?
        WHERE user_id=?
        """,
        (
            username,
            address,
            contact,
            user_id
        ))

        conn.commit()
        conn.close()

        print("\nProfile Updated Successfully.")