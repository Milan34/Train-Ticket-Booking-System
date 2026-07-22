# from services.auth_service import AuthService
# from services.profile_service import ProfileService
# from services.booking_service import BookingService
# from services.train_service import TrainService
from services.auth_service import AuthService
from services.profile_service import ProfileService
from services.admin_service import AdminService
from services.booking_service import BookingService
from services.train_service import TrainService


logged_in_user = None


def user_menu():

    global logged_in_user

    while True:



        print("\n========== USER MENU ==========")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. View All Trains")
        print("4. Search Train")
        print("5. Book Ticket")
        print("6. Cancel Ticket")
        print("7. Booking History")
        print("8. Logout")

        choice = input("Enter Choice : ")

        if choice == "1":

            ProfileService.view_profile(logged_in_user)

        elif choice == "2":

            ProfileService.update_profile(logged_in_user)

        elif choice == "3":

            TrainService.view_all_trains()

        elif choice == "4":

            TrainService.search_train()

        elif choice == "5":

            BookingService.book_ticket(logged_in_user)

        elif choice == "6":

            BookingService.cancel_ticket(logged_in_user)

        elif choice == "7":

            BookingService.booking_history(logged_in_user)

        elif choice == "8":

            print("Logout Successful.")
            break

        else:

            print("Invalid Choice")

def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Train")
        print("2. View Trains")
        print("3. Update Train")
        print("4. Delete Train")
        print("5. View all users")
        print("6. Logout")

        choice = input("Enter Choice : ")

        if choice == "1":
            TrainService.add_train()

        elif choice == "2":
            TrainService.view_trains()

        elif choice == "3":
            TrainService.update_train()

        elif choice == "4":
            TrainService.delete_train()
        elif choice == "5":
            AdminService.view_all_users()

        elif choice == "6":
            print("Admin Logged Out.")
            break

        else:
            print("Invalid Choice.")
def main_menu():

    global logged_in_user

    while True:

        print("\n==============================")
        print("TRAIN TICKET BOOKING SYSTEM")
        print("==============================")

        print("1. User Registration")
        print("2. User Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            AuthService.register()

        elif choice == "2":
            logged_in_user = AuthService.login()

            if logged_in_user:
                user_menu()


        elif choice == "3":

            if AdminService.admin_login():
                admin_menu()


        elif choice == "4":

            break