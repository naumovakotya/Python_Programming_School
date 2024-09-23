# imports
import csv
import inspect
import sys
from itertools import permutations

# functions
def read_csv_file(filename='map.csv'):
    with open(filename) as input_file:
        reader = csv.reader(input_file)
        lst_str = [row for row in reader] 
        return lst_str 
    
def get_classes_and_their_id(name_module ='cars'):
    try:
        return {cls_obj().id : cls_obj for cls_name, cls_obj in inspect.getmembers(sys.modules[name_module]) if inspect.isclass(cls_obj)}
    except:
        print("This class doesn't exist")
        return None

def enter_type_of_transport():
    dic_transport = get_classes_and_their_id()
    # I know that isn't the best varient to use len_dic, 
    # but while we have so simple and ordinal id of cars it's possible
    len_dic = len(dic_transport)
    print("The following types of transport are currently available:")
    for n in range(1, len_dic+1):
        print(f"{n}. {dic_transport[n].__name__}")
    try:
        selected_number = int(input(f"To select the type of transport, enter a number from 1 to {len_dic} here: "))
        return dic_transport[selected_number]()
    except:
        print("Invalid input. Please enter a valid number.")

def enter_points_for_visiting(uniq_name_cities):
    msg = (
        f"Please enter the city where the route starts, "
        f"the middle (if necessary) and the final route points separated by comma here: "
        )
    try:
        points = str(input(msg)).split(",")
        points_cities = []
        for point in points:
            cleaned_point = point.strip()
            if cleaned_point in uniq_name_cities:
                points_cities.append(cleaned_point)
            else:
                return print("Invalid input. Please enter a valid points.")
        start_p, *middle_ps, end_p = points_cities
        return start_p, middle_ps, end_p
    except:
        print("Invalid input. Please enter a valid points.")

def generate_route_variations(start, end, middle_points):
    # Генерируем все возможные перестановки для middle_points
    middle_permutations = permutations(middle_points)

    # Создаем фиксированный список всех точек (начальная, промежуточные, конечная)
    all_points = [start] + list(middle_points) + [end]

    # Генерируем все возможные маршруты с учетом перестановок для middle_points
    route_variations = [
        [start] + list(permutation) + [end]
        for permutation in middle_permutations
    ]

    return route_variations

def cal_optimal_way(cl_map, lst_ways):
    calculated_ways = {}
    lst_complexities = []
    for way in lst_ways:
        local_complexity = 0
        local_way = []
        for i in range(1, len(way)):
            start_p_name = way[i-1]
            end_p_name = way[i]
            if not (start_p_name + '-' + end_p_name) in calculated_ways:
                t_res = cl_map.dijkstra_algorithm(start_p_name, end_p_name)
                if not t_res[0]: return [[end_p_name]], False
                calculated_ways[start_p_name + '-' + end_p_name] = t_res
                calculated_ways[end_p_name + '-' + start_p_name] = [t_res[0][::-1],t_res[1]] #inverted route for inverted pair
            local_way = local_way + [calculated_ways[start_p_name + '-' + end_p_name][0]]
            local_complexity += calculated_ways[start_p_name + '-' + end_p_name][1]
        lst_complexities.append([way, local_complexity, local_way])
    return sorted(lst_complexities, key=lambda x: x[1]), True

def print_res(lts_optimal_way, status, car_obj):
    if status:
        print(f'The most fuel-efficient route is {lts_optimal_way[0]}')
        print(f'Details of the route is {lts_optimal_way[2]}, which uses {round(lts_optimal_way[1]*car_obj.passability, 2)} liters of gasoline')
    else:
        print(f'Unable to reach the point {lts_optimal_way[0]}')


