from database import get_connection
from utils.helper import generate_booking_id, generate_seat
from datetime import datetime
from utils.date_validation import valid_date




class BookingService:

    @staticmethod
    def book_ticket(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== BOOK TICKET ==========\n")

        try:
            train_number = int(input("Enter Train Number : "))
        except ValueError:
            print("Invalid Train Number.")
            conn.close()
            return
        journey_date = input("Enter Journey Date (DD-MM-YYYY or DD/MM/YYYY or DD,MM,YYYY): ")

        if not valid_date(journey_date):
            print("Invalid Date!")
            print("Accepted formats:")
            print("DD-MM-YYYY")
            print("DD/MM/YYYY")
            print("DD,MM,YYYY")
            print("DD.MM.YYYY")
            conn.close()
            return
        cursor.execute("""
        SELECT *
        FROM train
        WHERE train_number=?
        """,
        (train_number,))

        train = cursor.fetchone()

        if train is None:

            print("Train Not Found.")

            conn.close()
            return

        if train[6] <= 0:

            print("No Seats Available.")

            conn.close()
            return

        booking_id = generate_booking_id()
        seat_number = generate_seat()
        fare = train[7]

        cursor.execute("""
        INSERT INTO booking
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            booking_id,
            user_id,
            train_number,
            journey_date,
            seat_number,
            fare,
            "BOOKED"
        ))

        cursor.execute("""
        UPDATE train
        SET seats = seats - 1
        WHERE train_number=?
        """,
        (train_number,))

        conn.commit()
        conn.close()

        print("\n==============================")
        print("Ticket Booked Successfully")
        print("==============================")

        print("Booking ID :", booking_id)
        print("Train :", train[1])
        print("Seat :", seat_number)
        print("Fare :", fare)

    @staticmethod
    def cancel_ticket(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            booking_id = int(input("Enter Booking ID : "))
        except ValueError:
            print("Invalid Booking ID.")
            conn.close()
            return

        cursor.execute("""
                       SELECT *
                       FROM booking
                       WHERE booking_id = ?
                         AND user_id = ?
                       """, (booking_id, user_id))

        booking = cursor.fetchone()

        if booking is None:
            print("Booking Not Found.")

            conn.close()
            return

        if booking[6] == "CANCELLED":
            print("Ticket Already Cancelled.")

            conn.close()
            return

        cursor.execute("""
                       UPDATE booking
                       SET status='CANCELLED'
                       WHERE booking_id = ?
                       """,
                       (booking_id,))

        cursor.execute("""
                       UPDATE train
                       SET seats = seats + 1
                       WHERE train_number = ?
                       """,
                       (booking[2],))

        conn.commit()
        conn.close()

        print("\nTicket Cancelled Successfully.")

    @staticmethod
    def booking_history(user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT booking.booking_id,
                              train.train_name,
                              booking.journey_date,
                              booking.seat_number,
                              booking.fare,
                              booking.status

                       FROM booking

                                JOIN train
                                     ON booking.train_number = train.train_number

                       WHERE booking.user_id = ?
                       """,
                       (user_id,))

        bookings = cursor.fetchall()

        conn.close()

        if len(bookings) == 0:
            print("No Bookings Found.")
            return

        print("\n==============================")

        print("{:<12}{:<20}{:<15}{:<10}{:<8}{:<12}".format(
            "BookingID",
            "Train",
            "Journey",
            "Seat",
            "Fare",
            "Status"
        ))

        print("-" * 90)

        for booking in bookings:
            print("{:<12}{:<20}{:<15}{:<10}{:<8}{:<12}".format(
                booking[0],
                booking[1],
                booking[2],
                booking[3],
                booking[4],
                booking[5]
            ))
