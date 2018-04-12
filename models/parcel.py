class Parcel():

    def __init__(self, start, destination):
        self.start = start
        self.current = start
        self.destination = destination
        self.next = next_cities[self.destination.name][self.current.name] ## avoid global var
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
        time = time_table[self.current.name][self.next.name]
        self.duration += time

    def update_current_city(self):
        self.current.parcels.remove(self)
        self.next.incoming_parcels.append(self)
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
