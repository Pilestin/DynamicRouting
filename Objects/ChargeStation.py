from Objects.Target import Target


class ChargeStation(Target):
    """ 
    Bu sınıf veri setinde StringID değerleri "S" olan verileri içermektedir. Bunlar istasyonları temsil eder.
    """
    def __init__(self, id, idx, x, y, ready_time, due_date, service_time,distance_matrix):
        super(ChargeStation, self).__init__(id, idx, x, y, ready_time, due_date, service_time, distance_matrix)