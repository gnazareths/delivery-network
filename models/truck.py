class Truck():

    def __init__(self, city, route=None):

        self.city = city
        self.route = route
        self.parcels = []

    def get_trip_time(self):

        exp_trip_time = time_table[self.city.name][self.route.name]
        time = np.random.normal(exp_trip_time, exp_trip_time/10)

        return time

    def add_parcels(self, parcels):

        for i in parcels:
            if i.next == self.route:
                self.parcels.append(i)

    def add_route(self, route): ## needed?

        self.route = route

    def follow_route(self):

        trip_time = self.get_trip_time()
        for i in self.parcels:
            i.trip_time = trip_time
        self.drop_off()
        self.parcels = []
        self.city = self.route

    def drop_off(self):

        i = 0
        while i < len(self.parcels):
            parcel = self.parcels[i]
            if parcel.destination == parcel.current:
                self.parcels.remove(parcel)
                self.route.complete_trips.append(parcel)
                parcel.complete()
            else:
                self.route.incoming_parcels.append(parcel)
                i += 1

    def __repr__(self):

        return "Truck in {}".format(self.city)
