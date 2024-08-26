import math as m
from Objects.Target import Target


class Customer(Target):
    """ 
    Bu sınıf veri setinde StringID değerleri "C" olan verileri içermektedir. Bunlar müşteri düğümlerini temsil eder.
    Target Sınıfından farklı olarak müşterilerin talep ettikleri yük miktarını (demand) de sınıf özelliği olarak içerir.
    """

    def __init__(self, id, idx, x, y, demand, ready_time, due_date, service_time, distance_matrix):
        super(Customer, self).__init__(id, idx, x, y, ready_time, due_date, service_time, distance_matrix)
        self.demand = demand
        self.closest_charge_station = ""
        
    # def __str__(self):
    #     return super().__str__()
    
    def getCustomer(self):
        return self

    
