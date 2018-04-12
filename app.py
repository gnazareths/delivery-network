from helpers import *
from models import City, Parcel, Truck

## generate cities and next_cities table
cities = generate_cities()
next_cities = generate_next_cities(cities)
time_table = generate_time_table()
trucks = []

## one truck per city
for key in cities.keys():
    new_truck = Truck(cities[key])
    trucks.append(new_truck)

## iterate 100 times
t = 0
while t < 10:
    t += 1

    ## loop through cities in the network
    for key in cities.keys():

        ## generate new delivery items in that city
        city = cities[key]
        generate_parcels(10, cities, city)

    ## loop trough trucks
    for truck in trucks:

        ## compute the next direction
        city = truck.city
        next_directions = [parcel.next for parcel in city.parcels]
        counts = Counter(next_directions)
        mode = counts.most_common(1)[0][0]
        truck.add_route(mode)

        ## add parcels to the truck
        truck.add_parcels(city.parcels)
        truck.follow_route()

        #print len(truck.parcels)
