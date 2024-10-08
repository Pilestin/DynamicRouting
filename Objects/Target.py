
#from readProblemInstances import readProblemInstances, readESOGUProblemInstances



class Target:
    """
    Bu sınıf Schneider veri setlerindeki her bir satır veriyi temsil eder.
    Bu veri setindeki StringID, Type, x, y, demand, ReadyTime, DueDate, ServiceTime sütunlarını sınıf özellikleri olarak içerir.
    Ek olarak konum bilgisini döndüren bir fonksiyon ve nesnenin özelliklerini döndüren bir fonksiyon içerir.
    Aynı zamanda iki hedef arasındaki mesafeyi hesaplayan bir 'distance_to' fonksiyonu da içerir.
    """
    def __init__(self, id, idx, x, y, ready_time, due_date, service_time, distance_matrix):
        self.id = id
        self.idx = idx
        self.x = x
        self.y = y
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time
        self.distance_matrix = distance_matrix

    def distance_to(self, compared_target):
        return self.distance_matrix[self.idx - 1, compared_target.idx - 1]
    
    def distance_to_avg_of_two(self, compared_target1, compared_target2, distance_matrix):
        avg_distance = (distance_matrix[self.idx - 1,compared_target1.idx - 1] + distance_matrix[self.idx - 1,compared_target2.idx - 1])
        return avg_distance

    def get_coordinates(self):
        return self.x, self.y

    def __str__(self):
        # return "type: {0}, id: {1}, idx: {2} x: {3}, y: {4}".format(type(self), self.id, self.idx, self.x, self.y)
        return f"{self.id}"

    def __repr__(self):
        return self.__str__()