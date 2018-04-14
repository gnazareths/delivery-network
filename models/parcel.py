class Parcel():

    def __init__(self, start, destination):

        self.start = start
        self.current = start
        self.destination = destination
        self.next = next_cities[self.destination.name][self.current.name] ## avoid global var
        self.trip_time = None
        self.duration = 0
        self.completed = False

    def info(self):

        if self.completed:
            completed = "Completed"
        else:
            completed = "Pending"
        return (self.start.name, self.destination.name, completed)

    def complete(self):

        self.completed = True

    def update_time(self):

        if self.trip_time:
            if self.trip_time <= 14 and self.current == self.destination:
                self.duration += 14
            elif self.trip_time > 14 and self.current == self.destination:
                self.duration += 38
            elif self.trip_time <= 24 and self.current != self.destination:
                self.duration += 24
            elif self.trip_time > 24 and self.current != self.destination:
                self.duration += 24
        else:
            self.duration += 24

        self.trip_time = None

    def update_current_city(self): ## do parcels get added to the new city though?

        self.current.parcels.remove(self)
        self.current = self.next
        self.next = next_cities[self.destination.name][self.current.name] ## avoid global var

    def __repr__(self):

        if self.completed:
            status = "Complete"
        else:
            status = "Pending"
        string = "{} to {} – {}".format(self.start,
                                        self.destination,
                                        status)
        return string
