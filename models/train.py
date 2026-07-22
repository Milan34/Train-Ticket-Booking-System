class Train:

    def __init__(self,
                 train_number,
                 train_name,
                 origin,
                 destination,
                 departure_time,
                 arrival_time,
                 seats,
                 fare):

        self.train_number = train_number
        self.train_name = train_name
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats
        self.fare = fare