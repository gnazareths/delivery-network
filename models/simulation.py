import numpy as np
from models.truck import Truck
from helpers import *

class Simulation():

    def __init__(self,
                 cities,
                 time_table,
                 next_cities_table,
                 truck_capacity,
                 n_trucks,
                 #n_iter,
                 timesteps,
                 parcels_per_city):

        self.truck_capacity = truck_capacity
        self.n_trucks = n_trucks
        self.cities = cities
        self.time_table = time_table
        self.next_cities_table = next_cities_table
        #self.n_iter = n_iter
        self.timesteps = timesteps
        self.parcels_per_city = parcels_per_city

    def run(self):

        ## store values
        trucks = []
        waiting_times = {city:[] for city in self.cities.keys()}
        cities_parcels = {city:[] for city in self.cities.keys()}
        cities_complete_trips = {city:[] for city in self.cities.keys()}
        cities_complete_waiting_times = {city:[] for city in self.cities.keys()}
        cities_incomplete_waiting_times = {city:[] for city in self.cities.keys()}

        ## create the trucks
        ## can be refactored
        for _ in range(n_trucks):
            key = np.random.choice(self.cities.keys())
            city = self.cities[key]
            truck = Truck(city)
            trucks.append(truck)

        ## iterate timesteps
        t = 0
        while t < self.timesteps:
            t += 1

            for key in self.cities.keys():
                ## generate parcels originating from every city
                generate_parcels(parcels_per_city[key], cities, cities[key])

            for truck in trucks:
                ## decide which way the truck is going
                ## based on the mode of the next_directions
                current_city = truck.city

                ## if a city has no parcels, the truck should stay there
                if len(current_city.parcels) == 0:
                    continue

                next_directions = [parcel.next for parcel in current_city.parcels]
                counts = Counter(next_directions)
                mode = counts.most_common(1)[0][0]
                ## change route of truck
                truck.add_route(mode)

                ## add parcels to the truck
                parcels_added = 0
                n_parcels = 0
                while n_parcels < len(current_city.parcels):
                    parcel = current_city.parcels[n_parcels]
                    if parcel.next == truck.route:
                        truck.parcels.append(parcel)
                        parcel.update_current_city()
                        parcels_added += 1
                    else:
                        n_parcels += 1
                    ## break if/when capacity is exceeded
                    if parcels_added >= self.truck_capacity:
                         break

                ## do what has to be done...
                truck.follow_route()

            ## update total duration for every parcel that's not complete
            for key in self.cities.keys():
                city = self.cities[key]
                all_parcels = np.concatenate((city.parcels, city.incoming_parcels))
                for parcel in all_parcels:
                    parcel.update_time() ## idea adding from incoming_parcels to completed to update time only of recently completed

                ## after updating duration, merge incoming with parcels
                city.parcels = list(all_parcels)
                city.incoming_parcels = []

                ## store values
                if t % self.timesteps == 0:

                    ## store parcels
                    cities_parcels[key].append(len(city.parcels))
                    cities_complete_trips[key].append(len(city.complete_trips))

                    ## compute and store waiting times
                    all_complete_trips = [i.duration for i in city.complete_trips]
                    all_incomplete_trips = np.concatenate(([i.duration for i in city.parcels],
                                                       [i.duration for i in city.incoming_parcels]))
                    mean_complete_waiting_times = np.mean(all_complete_trips)
                    mean_incomplete_waiting_times = np.mean(all_incomplete_trips)
                    cities_complete_waiting_times[key].append(mean_complete_waiting_times)
                    cities_incomplete_waiting_times[key].append(mean_incomplete_waiting_times)

        return (cities_parcels,
                    cities_complete_trips,
                    cities_complete_waiting_times,
                    cities_incomplete_waiting_times)
