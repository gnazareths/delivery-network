cities = generate_cities()
next_cities = generate_next_cities(cities)
time_table = generate_time_table()
truck_capacity = 100
n_trucks = 6
timesteps = 20
parcels_per_city = {"Porto Alegre": 100, "Curitiba": 100, "Sao Paulo": 100, "Rio de Janeiro": 100}

porto_alegre_parcels = []
porto_alegre_complete_trips = []
porto_alegre_incomplete_waiting_times = []
porto_alegre_complete_waiting_times = []

curitiba_parcels = []
curitiba_complete_trips = []
curitiba_incomplete_waiting_times = []
curitiba_complete_waiting_times = []

sao_paulo_parcels = []
sao_paulo_complete_trips = []
sao_paulo_incomplete_waiting_times = []
sao_paulo_complete_waiting_times = []

rio_parcels = []
rio_complete_trips = []
rio_incomplete_waiting_times = []
rio_complete_waiting_times = []

for i in range(100):

    sim = Simulation(cities, time_table, next_cities, truck_capacity, n_trucks, timesteps, parcels_per_city)
    parcels, complete_trips, complete_waiting_times, incomplete_waiting_times  = sim.run()

    porto_alegre_parcels.append(parcels["Porto Alegre"][-1])
    porto_alegre_complete_trips.append(complete_trips["Porto Alegre"][-1])
    porto_alegre_incomplete_waiting_times.append(incomplete_waiting_times["Porto Alegre"][-1])
    porto_alegre_complete_waiting_times.append(complete_waiting_times["Porto Alegre"][-1])

    curitiba_parcels.append(parcels["Curitiba"][-1])
    curitiba_complete_trips.append(complete_trips["Curitiba"][-1])
    curitiba_incomplete_waiting_times.append(incomplete_waiting_times["Curitiba"][-1])
    curitiba_complete_waiting_times.append(complete_waiting_times["Curitiba"][-1])

    sao_paulo_parcels.append(parcels["Sao Paulo"][-1])
    sao_paulo_complete_trips.append(complete_trips["Sao Paulo"][-1])
    sao_paulo_incomplete_waiting_times.append(incomplete_waiting_times["Sao Paulo"][-1])
    sao_paulo_complete_waiting_times.append(complete_waiting_times["Sao Paulo"][-1])

    rio_parcels.append(parcels["Rio de Janeiro"][-1])
    rio_complete_trips.append(complete_trips["Rio de Janeiro"][-1])
    rio_incomplete_waiting_times.append(incomplete_waiting_times["Rio de Janeiro"][-1])
    rio_complete_waiting_times.append(complete_waiting_times["Rio de Janeiro"][-1])
