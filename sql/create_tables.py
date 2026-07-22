from database import get_connection


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS admin
                   (

                       admin_id
                       INTEGER
                       PRIMARY
                       KEY,
                       username
                       TEXT
                       UNIQUE
                       NOT
                       NULL,
                       password
                       TEXT
                       NOT
                       NULL

                   )
                   """)

    cursor.execute("""
                   SELECT *
                   FROM admin
                   WHERE username = ?
                   """, ("admin",))

    admin = cursor.fetchone()

    if admin is None:
        cursor.execute("""
                       INSERT INTO admin
                       VALUES (?, ?, ?)
                       """,
                       (
                           1001,
                           "admin",
                           "admin123"
                       ))
        

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer(

        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        address TEXT,
        contact TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS train(

        train_number INTEGER PRIMARY KEY,
        train_name TEXT,
        origin TEXT,
        destination TEXT,
        departure_time TEXT,
        arrival_time TEXT,
        seats INTEGER,
        fare REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS booking(

        booking_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        train_number INTEGER,
        journey_date TEXT,
        seat_number TEXT,
        fare REAL,
        status TEXT,

        FOREIGN KEY(user_id) REFERENCES customer(user_id),
        FOREIGN KEY(train_number) REFERENCES train(train_number)

    )
    """)

    conn.commit()
    conn.close()


create_tables()