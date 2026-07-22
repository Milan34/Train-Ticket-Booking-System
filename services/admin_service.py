from database import get_connection


class AdminService:

    @staticmethod
    def admin_login():

        conn = get_connection()
        cursor = conn.cursor()

        print("\n========== ADMIN LOGIN ==========\n")

        username = input("Username : ")
        password = input("Password : ")

        cursor.execute("""
        SELECT *
        FROM admin
        WHERE username=? AND password=?
        """,
        (username, password))

        admin = cursor.fetchone()

        conn.close()

        if admin:
            print("\nAdmin Login Successful.")
            return True

        print("Invalid Username or Password.")
        return False

    @staticmethod
    def view_all_users():

        conn = get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                           SELECT user_id,
                                  username,
                                  email,
                                  address,
                                  contact
                                  
                           FROM customer
                           ORDER BY user_id
                           """)

            users = cursor.fetchall()

            if len(users) == 0:
                print("\nNo Users Found.")
                return

            print("\n========================= REGISTERED USERS =========================\n")

            print("{:<10} {:<20} {:<30} {:<25} {:<15}".format(
                "User ID",
                "Username",
                "Email",
                "Address",
                "Contact"
            ))

            print("-" * 150)

            for user in users:
                print("{:<10} {:<20} {:<30} {:<25} {:<15}".format(
                    user[0],
                    user[1],
                    user[2],
                    user[3],
                    user[4]
                ))

        except Exception as e:

            print("Error:", e)

        finally:

            conn.close()