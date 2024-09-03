from Objects.Customer import Customer
from Objects.Target import Target
from RouteVisualization.print_route import print_route
import random 
import numpy as np

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

def acceptance_criteria(cost: int, new_cost: int, temperature: int) -> bool:
    return random.random() < np.exp((cost - new_cost) / temperature)

def neighborhood_search(route: list[Target]) -> list[Target]:
    idx1, idx2 = random.sample(range(1, len(route) - 1), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route



def static_routing(route: list[Target],  n: int = 10, unserved_customers : list = [] ) -> list[Target]:
    """
    Rotalama yapmak için komşulukları keşfeder ve eğer iyi bir distance elde edildiyse rotayı tutar.

    Args:
        route (list[Target]): _description_

    Returns:
        list[Target]: _description_
    """
    
    
    max_iter = 100
    temperature = 1000
    cooling_rate = 0.95
    
    # rota kopyalanır ve cost'u alınır.
    current_route = route[:]
    iteration_route = route[:]
    # best_route = route[:]
    
    current_cost = calculate_distance(current_route)

    for i in range(0,max_iter+1):
        
        iteration_route = neighborhood_search(iteration_route)
        new_cost = calculate_distance(iteration_route)
        
        if new_cost < current_cost:
            current_route = iteration_route[:]
            current_cost = new_cost

        if i%10 == 0:
            print(f"Iteration: {i}\t Cost: {current_cost} \t Route: {current_route}")
            input("devam . . . ")
        
    return current_route

def dynamic_routing(route: list[Target], n: int = 10, unserved_customers : list = []) -> list[Target]:
    """ 
    Öncelikle statik rotalama yapan fonksiyon çağırılır ve kesin rota elde edilir.
    Ardından bu rota üzerinde araç ilerlediği (for döngüsü) varsayılarak başlanır.
    Her aşamada %x olasılık ile yeni talep gelip gelmeyeceği belirlenir ve talep geldiğinde en yakın noktaya ekleme yapılır. 
    args:
        route: list[Target] -> Rota listesi
        n: int -> Alınacak customer sayısı

    """
    # route = static_routing(route[:], n, unserved_customers)
    
    for index, node in enumerate(route):
        print("----------------------------------------------------------------")
        print_route(route, index)
        print(f"Şu an : [{index}] {node}")
        # bir olasılık değeri (0-1) 
        if unserved_customers == []:
            print("Tüm müşteriler servis edildi.")
            continue

        probablity = random.random()
        if probablity > 0.5:
            
            # yeni bir rastgele müşteri gelir. birden fazla olması durumunda sample kullanılabilir.
            new_customer = random.choice(unserved_customers)
            # en yakın noktaya ekleme yapılır
            input(f"{str(probablity)} olasılığı geldi. Yeni müşteri id: {new_customer} eklenecek.")
           
            cost_list = []
            for next_node in route[index:-1]:
                # burada rotaya ekleme yapıp min olan nokta da bulunabilir. lambda fonksiyonu ile.
                # ben her henüz gidilmemiş nokta için inceleyip en yakın olanı buldum
                distance_to_node = next_node.distance_to(new_customer)
                cost_list.append((distance_to_node, next_node))
            
            # print(cost_list)
            best_ = min(cost_list, key=lambda cost: cost[0])
            best_node = best_[1]
            print(f"Müşteri id {new_customer} için rotadaki en yakın yer ve uzaklık : ", best_)
            input(f"Müşteri id {new_customer} rotaya dahil ediliyor . . . ")
            where = route.index(best_node)
            route.insert(where+1, new_customer)
            unserved_customers.remove(new_customer)
        else : 
            # print("No new customer")
            input(f"{str(probablity)} olasılığı geldi. devam ediliyor.")
            continue

    return route
    