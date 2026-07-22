import random
import sqlite3


def generate_booking_id():

    conn = sqlite3.connect("railway.db")

    cursor = conn.cursor()

    while True:

        booking_id = random.randint(100000,999999)

        cursor.execute("""
        SELECT *
        FROM booking
        WHERE booking_id=?
        """,(booking_id,))

        if cursor.fetchone() is None:
            conn.close()
            return booking_id


def generate_user_id():

    conn = sqlite3.connect("railway.db")

    cursor = conn.cursor()

    while True:

        user_id=random.randint(10000,99999)

        cursor.execute("""
        SELECT *
        FROM customer
        WHERE user_id=?
        """,(user_id,))

        if cursor.fetchone() is None:
            conn.close()
            return user_id


def generate_seat():

    coach=random.choice(["S1","S2","S3"])

    seat=random.randint(1,72)

    return f"{coach}-{seat}"