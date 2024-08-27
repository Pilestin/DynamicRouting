from xml.etree import ElementTree as ET
import numpy as np
# from Objects.ChargeStation import ChargeStation 
from Objects.Customer import Customer
from Objects.Target import Target
import random

def print_route(route: list[Target]) -> None:
    """ 
    rota yazdırmak için kullanılan fonksiyon 
    
    args:
        route: list[Target] -> Rota listesi
    return:
        None
    
    """
    print("Route: ", end=" ")
    try:
        for target in route:
            print(target, end=", ")
        
    except TypeError:
        print(route, end=", ")
    finally:
        print("\n")
    
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

def calculate_distance(route: list[Target]) -> float:
    """ 
    Rota üzerindeki toplam mesafeyi hesaplar.
    args:
        route: list[Target] -> Rota listesi
    return:
        total_distance: float -> Rota üzerindeki toplam mesafe
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += route[i].distance_to(route[i+1])
    return total_distance

def calculate_cost(route: list[Target]) -> float:
    """ 
    Rota üzerindeki toplam maliyeti hesaplar.
    args:
        route: list[Target] -> Rota listesi
    return:
        total_cost: float -> Rota üzerindeki toplam maliyet
    """
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += route[i].cost_to(route[i+1])
    return total_cost

def acceptance_criteria(cost: int, new_cost: int, temperature) -> bool:
    return random.random() < np.exp((cost - new_cost) / temperature)

def neighborhood_search(route: list[Target]) -> list[Target]:
    idx1, idx2 = random.sample(range(1, len(route) - 1), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def dynamic_routing(route: list[Target], n: int = 10, unserved_customers : list = []) -> list[Target]:
    """ 
    Bu fonksiyon ile iterasyonlar yaparak rota üzerinde değişiklikler yapılır.
    %50 ihtimal ile yeni bir rota oluşturulurken %50 ihtimal ile rota dinamik olarak yapılandırılacaktır.
    
    Problem : Şu an yeni bir unserved talep geldiğinde rotanın distance'ı değişeceği için kabul kriterinin tekrar ele alınması gerekmektedir. 
    
    Bunun için yeni müşteri eklendiğinde cost yeniden hesaplanıp orjinal cost bu yapılabilir.  
    """
    max_iter = 100
    temperature = 1000
    cooling_rate = 0.95
    
    # rota kopyalanır ve cost'u alınır.
    current_route = route[:]
    iteration_route = route[:]
    # best_route = route[:]
    
    current_cost = calculate_distance(current_route)

    for i in range(max_iter):
        print("[{i}] current route: ", current_route, " cost: ", current_cost)
        if random.random() > 0.7:
            # rotaya yeni bir customer noktası eklenir.
            random_unserviced_customer = random.choice(unserved_customers)
            # yeni customer noktası rota üzerine sondan eklenir.
            current_route.insert(-1, random_unserviced_customer) # ! Deponun sağına koymamalı dikkat et test edilmedi 
            current_cost = calculate_distance(current_route) 
            print("dynamic customer adding : ", random_unserviced_customer)
            
        else:
            # Rota üzerindeki customer noktaları arasında iki tane rastgele customer seçilir.
            # yeni rota amaç fonksiyonu bakımından incelenir. 
            iteration_route = neighborhood_search(iteration_route)
            iteration_cost = calculate_distance(iteration_route)

            # greedy acceptance / açgözlü kabul
            if iteration_cost < current_cost:
                print("Accept new neighbor solution") 
                current_route = iteration_route[:]
                current_cost = iteration_cost

            # simulated annealing acceptance
            # if new_cost < cost or acceptance_criteria(cost, new_cost, temperature):
            #     route = new_route[:]
        _cost = calculate_distance(current_route)
        print("[{i}] current route: ", current_route, " cost: ", _cost)

        input("devam etmek için bir tuşa basınız")
        
    return current_route
    
def main():
    # verinin/problemin 3 farklı bileşen ile alınması 
    depot, customers, initial_route = get_data()

    print("Customers : ",customers)    
    unserved_customers = None
    route = None
    
    route, unserved_customers = divide_route(initial_route[:])
    print("----------------------------------------------------------------")
    print("Initial Route: ", route)
    print("Unserved Customers: ", unserved_customers)
    print("----------------------------------------------------------------")
    
    input("devam etmek için bir tuşa basınız")
    
    result = dynamic_routing(route[:], 10, unserved_customers=unserved_customers)
    print(result)
    


if __name__ == "__main__":
    main()
    