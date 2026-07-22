class Booking:

    def __init__(self,
                 booking_id,
                 user_id,
                 train_number,
                 journey_date,
                 seat_number,
                 fare,
                 status):

        self.booking_id = booking_id
        self.user_id = user_id
        self.train_number = train_number
        self.journey_date = journey_date
        self.seat_number = seat_number
        self.fare = fare
        self.status = status