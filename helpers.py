import numpy as np
from models.city import City
from models.parcel import Parcel

def generate_parcels(n, cities, start):

    n_parcels = int(np.random.normal(n, n/10))
    for _ in range(n_parcels):
        keys = cities.keys()
        keys.remove(start.name)
        destination = np.random.choice(keys)
        destination = cities[destination]
        parcel = Parcel(start, destination)
        cities[start.name].add_parcel(parcel)

def generate_next_cities(cities):

    matrix = np.matrix([[None, cities["Curitiba"], cities["Curitiba"], cities["Curitiba"]],
                        [cities["Porto Alegre"], None, cities["Sao Paulo"], cities["Rio de Janeiro"]],
                        [cities["Curitiba"], cities["Curitiba"], None, cities["Rio de Janeiro"]],
                        [cities["Curitiba"], cities["Curitiba"], cities["Sao Paulo"], None]])
    df = pd.DataFrame(matrix)
    cities_list = cities.keys()
    df.columns = cities_list
    df.index = cities_list

    return df

def generate_time_table():

    times = {"Porto Alegre": {"Curitiba": 10},
             "Curitiba": {"Porto Alegre": 10, "Sao Paulo": 7, "Rio de Janeiro": 9},
             "Sao Paulo": {"Curitiba": 6, "Rio de Janeiro": 7},
             "Rio de Janeiro": {"Curitiba": 8, "Sao Paulo": 7}}

    return times

def generate_cities():

    A = City("Porto Alegre")
    B = City("Curitiba")
    C = City("Sao Paulo")
    D = City("Rio de Janeiro")
    cities = {"Porto Alegre": A, "Curitiba": B, "Sao Paulo": C, "Rio de Janeiro": D}

    return cities
