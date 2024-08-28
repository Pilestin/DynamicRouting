from Objects.Target import Target

def print_route(route: list[Target], now: int) -> None:
    """ 
    rota yazdırmak için kullanılan fonksiyon 
    
    args:
        route: list[Target] -> Rota listesi
    return:
        None
    
    """
    print("Route: ", end=" ")
    try:
        print("->", end=" ")
        for index, node in enumerate(route):
            if index == now:
                print("|", end=" ")
                print(node, "|",  end=" === ")
            else:
                
                if index == len(route) - 1:
                    print(node, end="")
                else: 
                    print(node, end=" === ")
        print()            

    except TypeError:
        print(route, end=", ")
    finally:
        print("\n")