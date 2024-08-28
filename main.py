from Objects.Customer import Customer
from Objects.Target import Target
from Routing.routing import calculate_distance, neighborhood_search, static_routing, dynamic_routing
from RouteVisualization.DynamicVisualization import visualize_on_sumo
from data.data_handler import get_data, divide_route
import numpy as np
import random

from RouteVisualization.DynamicVisualization import *


def main():
    # verinin/problemin 3 farklı bileşen ile alınması 
    depot, customers, initial_route = get_data()
    
    print("Customers : ",customers)    
    unserved_customers = None
    route = None
    
    route, unserved_customers = divide_route(initial_route[:])
    
    print("----------------------------------------------------------------")
    print("Initial Route      : \t", route , "\t cost: ", calculate_distance(route))
    print("Unserved Customers : \t", unserved_customers)
    print("----------------------------------------------------------------")
    
    input("devam etmek için bir tuşa basınız")
    
    static_route = static_routing(route[:], 10, unserved_customers)
    visualize_on_sumo(static_route)
    
    dynamic_route = dynamic_routing(static_route[:], 10, unserved_customers=unserved_customers)
    visualize_on_sumo(dynamic_route)
    
    print(dynamic_route)
    


if __name__ == "__main__":
    main()
    