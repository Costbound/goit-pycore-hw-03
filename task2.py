def get_numbers_ticket(min: int, max: int, quantity: int):
    min = int(min)
    max = int(max)
    quantity = int(quantity)
    print(type(min))
    if min >= max:
        print('"min" value must be less than "max" value')
        return
    if quantity > (max - min):
        print ('"quantity" must be less or equal max - min')
        return
    print(min is int)
    result = generate_numbers_list(min, max)
    return result
    
    
def generate_numbers_list(min: int, max: int):
    result_list = []
    
    while min <= max:
        result_list.push(min)
        min += 1
    
    return result_list
    
get_numbers_ticket(1, 1000, 50)
