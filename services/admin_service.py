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