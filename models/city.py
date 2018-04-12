class City():

    def __init__(self, name):
        self.name = name
        self.parcels = []
        self.incoming_parcels = []
        self.complete_trips = []

    def __repr__(self):

        return self.name

    def add_parcel(self, parcel):
        self.parcels.append(parcel)

    ## function to remove parcels
