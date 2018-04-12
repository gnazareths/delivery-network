class Truck():

    def __init__(self, city, route=None):
        self.city = city
        self.route = route
        self.parcels = []

    def add_parcels(self, parcels):
        for i in parcels:
            if i.next == self.route:
                self.parcels.append(i)

    def add_route(self, route): ## needed?
        self.route = route

    def follow_route(self):
        self.update_time()
        self.drop_off()
        self.update_parcels()
        self.city = self.route

    def update_time(self):
        for i in self.parcels:
            i.update_time()

    def drop_off(self):
        i = 0
        while i < len(self.parcels):
            parcel = self.parcels[i]
            if parcel.destination == parcel.next:
                self.parcels.remove(parcel)
                self.city.parcels.remove(parcel)
                self.route.complete_trips.append(parcel)
                parcel.complete()
            else:
                i += 1

    def update_parcels(self):
        city = self.city
        for parcel in self.parcels:
            parcel.update_current_city()
        self.parcels = []

    def __repr__(self):

        return "Truck in {}".format(self.city)
