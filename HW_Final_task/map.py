import queue

# Classes for cities (nodes) and for distance between them (edges)
mes_errow = f"The discrepancy between the types of input variables and the expected types of variables"

class City():
    # nodes
    def __init__(self, name):
        if isinstance(name, (int, str)):
            self.name = name
            self.edges = []
            self.is_visited = False
            self.was_in_queue = False
            self.best_way = []
            self.best_way_complexity = float("inf")

    def add_edges(self, edge):
        if isinstance(edge, Road):
            self.edges.append(edge)
        else:
            return mes_errow + " in class City"
        
    def __str__(self):
        return (f"Class {self.__class__.__name__}, name = {self.name}. "
                f"Number of roads = {len(self.edges)}, which includes "
                f"{[road.name for road in self.edges]}.")
    
    def refresh_city(self):
        self.is_visited = False
        self.was_in_queue = False
        self.best_way = []
        self.best_way_complexity = float("inf")

class Road():
    # edges
    def __init__(self, start_p_obj:City, end_p_obj:City, name:str, 
                 distance:(int|float), difficulty:(int|float),
                 prohibited_cars):
        if (isinstance(start_p_obj, City) 
            and isinstance(end_p_obj, City)
            and isinstance(name, str)):
            self.start_p_obj = start_p_obj
            self.end_p_obj = end_p_obj
            self.name = name
            self.distance = float(distance)
            self.difficulty = float(difficulty)
            self.prohibited_cars = [int(car) for car in prohibited_cars if car] if not prohibited_cars[0]=='' else []
            self.complexity = self.distance * self.difficulty
            # add road to cities
            self.start_p_obj.add_edges(self)
            self.end_p_obj.add_edges(self)

    def cheking_is_c_belong_to_r(self, city:City):
        if isinstance(city, City):
            return city.name == self.start_p_obj.name or city.name == self.end_p_obj.name

    def get_another_point(self, city_par:City):
        if isinstance(city_par, City) and self.cheking_is_c_belong_to_r(city_par):
            if city_par == self.start_p_obj:
                return self.end_p_obj
            elif city_par == self.end_p_obj:
                return self.start_p_obj
            
    def __str__(self):
        return (f"Class {self.__class__.__name__}, start_p = {self.start_p_obj.name}, end_p = {self.end_p_obj.name}, "
                f"distance = {self.distance}, difficulty = {self.difficulty}, "
                f"prohibited_cars = {self.prohibited_cars}, complexity = {self.complexity}.") 
    
    def get_start_end_points(self):
        return self.start_p, self.end_p
    
class Map:
    def __init__(self, name = 'map'):
        self.uniq_name_cities = []
        self.cities_obj = {}
        self.roads_obj = {}
        self.name = name

    def creating_cities_and_roads(self, prepared_file, entered_car):
        # creating objs using info from file
        for road in prepared_file:
            start_p, end_p, distance, difficulty, lst_proh_cars_str = road
            lst_proh_cars = lst_proh_cars_str.split(' ')
            # create city
            for name in [start_p, end_p]:
                if name not in self.uniq_name_cities:
                    city = City(name)
                    self.cities_obj[name] = city
                    self.uniq_name_cities.append(name)
            # create road
            if str(entered_car.id) not in lst_proh_cars:
                road = Road(self.cities_obj[start_p], self.cities_obj[end_p], f"{start_p}-{end_p}",
                            distance, difficulty, lst_proh_cars)
                self.roads_obj[road.name] = road
    
    def __str__(self):
        return f"Class {self.__class__.__name__} includes {len(self.cities_obj)} cities and {len(self.roads_obj)} roads"
    
    def find_city_by_name(self, city_name: str):
        return self.cities_obj[city_name]
    
    def put_city_and_change_status(self, q, point):
        if not point.is_visited:
            q.put(point)
            point.was_in_queue = True

    def refresh_cities(self):
        [self.cities_obj[city_name].refresh_city() for city_name in self.uniq_name_cities]
    
    def dijkstra_algorithm(self, start_p_name, end_p_name):
        self.refresh_cities()       
        q = queue.LifoQueue()
        start = self.find_city_by_name(start_p_name)
        end = self.find_city_by_name(end_p_name)
        self.put_city_and_change_status(q, start)
        start.best_way.append(start_p_name)
        start.best_way_complexity = 0
        while not q.empty():
            point = q.get()
            if point.name == end_p_name:
                continue 
            next_points_arr = []
            for road in point.edges:
                next_point = road.get_another_point(point)
                if (point.best_way_complexity + road.complexity < next_point.best_way_complexity):
                    next_point.best_way_complexity = point.best_way_complexity + road.complexity
                    next_point.best_way = point.best_way + [next_point.name]
                if not next_point.is_visited and not next_point.was_in_queue:
                    next_points_arr.append(next_point)
            if next_points_arr:
                next_points_arr = sorted(next_points_arr, key=lambda x: x.best_way_complexity, reverse = True)
            point.is_visited = True
            [self.put_city_and_change_status(q, point_ar) for point_ar in next_points_arr if point_ar]
        return (end.best_way, end.best_way_complexity)
            