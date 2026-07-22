from database import get_connection
from utils.validation import (
    valid_train_name,
    valid_location,
    valid_time
)

class TrainService:

    @staticmethod
    def add_train():

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== ADD TRAIN ==========\n")

        train_number = int(input("Train Number : "))
        train_name = input("Train Name : ").strip()
        origin = input("Origin : ").strip()
        destination = input("Destination : ").strip()
        # departure = input("Departure : ").strip()
        departure = input("Departure Time : ").strip()
        arrival = input("Arrival Time : ").strip()
        seats = int(input("Available Seats : "))
        fare = float(input("Fare : "))

        if not valid_train_name(train_name):
            print("Invalid Train Name.")
            conn.close()
            return

        if not valid_location(origin):
            print("Invalid Origin.")
            conn.close()
            return

        if not valid_location(destination):
            print("Invalid Destination.")
            conn.close()
            return

        if not valid_time(departure):
            print("Departure time should be in HH:MM format.")
            conn.close()
            return

        if not valid_time(arrival):
            print("Arrival time should be in HH:MM format.")
            conn.close()
            return

        cursor.execute("""
        SELECT *
        FROM train
        WHERE train_number=?
        """,
        (train_number,))

        if cursor.fetchone():

            print("Train Number already exists.")

            conn.close()
            return

        cursor.execute("""
        INSERT INTO train
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            train_number,
            train_name,
            origin,
            destination,
            departure,
            arrival,
            seats,
            fare
        ))

        conn.commit()
        conn.close()

        print("\nTrain Added Successfully.")

    @staticmethod
    def view_trains():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM train
        """)

        trains = cursor.fetchall()

        conn.close()

        if not trains:

            print("\nNo Trains Found.")
            return

        print("\n==============================")

        print("{:<10}{:<20}{:<15}{:<15}{:<12}{:<12}{:<8}{:<8}".format(
            "Number",
            "Name",
            "Origin",
            "Destination",
            "Departure",
            "Arrival",
            "Seats",
            "Fare"
        ))

        print("-"*100)

        for train in trains:

            print("{:<10}{:<20}{:<15}{:<15}{:<12}{:<12}{:<8}{:<8}".format(
                train[0],
                train[1],
                train[2],
                train[3],
                train[4],
                train[5],
                train[6],
                train[7]
            ))

    @staticmethod
    def update_train():

        conn = get_connection()
        cursor = conn.cursor()

        train_number = int(input("Enter Train Number : "))

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

        train_name = input("New Train Name : ")
        origin = input("Origin : ")
        destination = input("Destination : ")
        departure = input("Departure : ")
        arrival = input("Arrival : ")
        seats = int(input("Seats : "))
        fare = float(input("Fare : "))

        cursor.execute("""
        UPDATE train
        SET train_name=?,
            origin=?,
            destination=?,
            departure_time=?,
            arrival_time=?,
            seats=?,
            fare=?
        WHERE train_number=?
        """,
        (
            train_name,
            origin,
            destination,
            departure,
            arrival,
            seats,
            fare,
            train_number
        ))

        conn.commit()
        conn.close()

        print("\nTrain Updated Successfully.")


    @staticmethod
    def delete_train():

        conn = get_connection()
        cursor = conn.cursor()

        train_number = int(input("Enter Train Number : "))

        cursor.execute("""
        SELECT *
        FROM train
        WHERE train_number=?
        """,
        (train_number,))

        if cursor.fetchone() is None:

            print("Train Not Found.")

            conn.close()
            return

        cursor.execute("""
        DELETE FROM train
        WHERE train_number=?
        """,
        (train_number,))

        conn.commit()
        conn.close()

        print("\nTrain Deleted Successfully.")

    @staticmethod
    def search_train():

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== SEARCH TRAIN ==========\n")

        origin = input("Enter Origin : ")
        destination = input("Enter Destination : ")

        cursor.execute("""
                       SELECT *
                       FROM train
                       WHERE LOWER(origin) = LOWER(?)
                         AND LOWER(destination) = LOWER(?)
                       """,
                       (origin, destination))

        trains = cursor.fetchall()

        conn.close()

        if len(trains) == 0:
            print("\nNo Train Found.")
            return

        print("\nAvailable Trains\n")

        print("{:<10}{:<20}{:<15}{:<15}{:<10}{:<10}{:<8}{:<8}".format(
            "Number",
            "Name",
            "Origin",
            "Destination",
            "Dept",
            "Arrival",
            "Seats",
            "Fare"
        ))

        print("-" * 100)

        for train in trains:
            print("{:<10}{:<20}{:<15}{:<15}{:<10}{:<10}{:<8}{:<8}".format(
                train[0],
                train[1],
                train[2],
                train[3],
                train[4],
                train[5],
                train[6],
                train[7]
            ))

    @staticmethod
    def view_all_trains():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT *
                       FROM train
                       WHERE seats > 0
                       ORDER BY train_number
                       """)

        trains = cursor.fetchall()

        conn.close()

        if not trains:
            print("\nNo trains available.")
            return

        print("\n================ AVAILABLE TRAINS ================\n")

        print("{:<12} {:<25} {:<15} {:<15} {:<12} {:<12} {:<8} {:<8}".format(
            "Train No",
            "Train Name",
            "Origin",
            "Destination",
            "Departure",
            "Arrival",
            "Seats",
            "Fare"
        ))

        print("-" * 115)

        for train in trains:
            print("{:<12} {:<25} {:<15} {:<15} {:<12} {:<12} {:<8} ₹{:<8}".format(
                train[0],
                train[1],
                train[2],
                train[3],
                train[4],
                train[5],
                train[6],
                train[7]
            ))