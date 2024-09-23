import cars as c
import functions as f
import map as m
import os

# one  str for me (not for task)
os.system('cls' if os.name == 'nt' else 'clear')

car_obj = f.enter_type_of_transport()
# car_obj = c.PassengerCar()

# downlow map (the file with roads)
file_map = f.read_csv_file(filename='example.csv')
cl_map = m.Map()
cl_map.creating_cities_and_roads(file_map, car_obj)
print('')
start_p, middle_ps, end_p = f.enter_points_for_visiting(cl_map.uniq_name_cities)
# start_p, middle_ps, end_p = ['A', ['C', 'D', 'J', 'K', 'W', 'E', 'M', 'G'], 'F']

lst_ways = f.generate_route_variations(start_p, end_p, middle_ps)
optimal_ways_par, status = f.cal_optimal_way(cl_map, lst_ways)
# f.print_res(way, status, car_obj) for way in optimal_ways_par]
print('')
f.print_res(optimal_ways_par[0], status, car_obj)
