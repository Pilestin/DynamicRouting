from xml.etree import ElementTree as ET

from Objects.Customer import Customer
from Objects.Target import Target
import random
import numpy as np

def get_data() -> tuple[Target, list[Customer], list[Target]]:
    """ 
        Bu fonksiyon belirtilen talep noktaları içeren xml problemini okur ve ilgili Sınıflar aracılığı ile rota haline getirir.
        args:
            None
        return:
            depot: Target -> Depo noktası
            customers: list[Customer] -> Müşteri noktaları
            route: list[Target]
    """
    
    tree = ET.parse('data/newesogu-c20-ds1.xml')
    root = tree.getroot()
    customers = []
    depot = None 
    
    distance_matrix_tag = 'DijkstraMatrix'
    distance_matrix_data = root.find(distance_matrix_tag).text
    matrix_lines = distance_matrix_data.splitlines()
    distance_matrix = np.array([[float(x) for x in line.split()] for line in matrix_lines])
    
    for point in root.findall('Points/Point'):
        id = point.get('Name')
        idx = int(point.get('No'))  # Assuming idx is the same as No
        x = float(point.get('X'))
        y = float(point.get('Y'))
        request_element = point.find('Requests/Request')
        if request_element is not None:
            demand = int(request_element.get('TotalWeight', '0'))
            ready_time = int(request_element.get('ReadyTime', '0'))
            due_date = int(request_element.get('DueDate', '0'))
            service_time = int(request_element.get('ServiceTime', '0'))
        else:
            demand = 0  # Requests/Request öğesi bulunmuyorsa, varsayılan olarak 0 kullanılıyor
            ready_time = 0
            due_date = 0
            service_time = 0

        if point.get('Type') == 'DepoCharging':
            depot = Target(id, idx, x, y, ready_time, due_date, service_time, distance_matrix)
        # elif point.get('Type') == 'Charging' or point.get('Type') == 'DepoCharging':
        #     new_target = ChargeStation(id, idx, x, y, ready_time, due_date, service_time, distance_matrix)
        #     fuel_stations.append(new_target)
 
        elif point.get('Type') == 'Delivery':
            new_target = Customer(id, idx, x, y, demand, ready_time, due_date, service_time, distance_matrix)
            customers.append(new_target)
            
    # Rota başlangıcı ve sonu depo olmalıdır, bu yüzden depo ve müşterileri birleştirerek bir rota oluşturuyoruz
    route = [depot] + customers + [depot]
    return depot, customers, route
     
def divide_route(route: list[Target], n: int = 10) -> list[Target]:    
    """ 
    İlk aşamada alınan (get_data()) rota listesinin içerisinden n adet customer noktası alarak yeni bir rota oluşturur. 
    Diğer müşterileri ise unserved_customer listesine ekler.
    args:
        route: list[Target] -> Rota listesi
        n: int -> Alınacak customer sayısı
    return:
        new_route: list[Target] -> Yeni rota
        unserved_customers: list[Target] -> Servis edilmemiş müşteriler
    """
    new_route = []
    unserved_customers = []
    depot = route[0]
    route_size = len(route)
    n = route_size // 2 
    
    choosen_customers = random.sample(route[1:-1], n)
    unserved_customers = [customer for customer in route[1:-1] if customer not in choosen_customers]
    new_route = [depot] + choosen_customers + [depot]

    return new_route, unserved_customers
