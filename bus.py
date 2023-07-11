class Bus:
    def __init__ (self, route_number, destination, passengers, drive):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        self.drive = drive

    def num_of_passengers (self):
        return len(self.passengers)
    
    def pick_up (self, name):
        [self.passenger].append(name)
    
    
