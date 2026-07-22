from database import get_connection


def insert_sample_data():

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM train")

    count=cursor.fetchone()[0]

    if count==0:

        trains=[

        (12345,"Rajdhani Express","Kolkata","Delhi","08:00","18:30",150,1500),

        (22331,"Duronto Express","Kolkata","Mumbai","10:00","08:00",120,2200),

        (34567,"Shatabdi Express","Delhi","Lucknow","06:00","12:30",90,900),

        (98765,"Howrah Express","Howrah","Chennai","07:30","10:00",200,1800),

        (11223,"Jan Shatabdi","Kolkata","Durgapur","09:00","11:30",80,350)

        ]

        cursor.executemany("""

        INSERT INTO train
        VALUES(?,?,?,?,?,?,?,?)

        """,trains)

    conn.commit()

    conn.close()


insert_sample_data()