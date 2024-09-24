import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Validation
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except ValueError:
        print('"min", "max" and "quantity" must be a number')
    if (min < 1) or (min > 999):
        print('"min" must be more than 0 and less than 1000')
        return
    if (max < 2) or (max > 1000):
        print('"max" must be more than 1 and less or equal 1000')
        return
    if min >= max:
        print('"min" value must be less than "max" value')
        return
    if quantity > ((max - min) + 1):
        print ('"quantity" must be less or equal max - min')
        return


    result = random.sample(generate_numbers_list(min, max), quantity)
    result.sort()
    return result
    
    
def generate_numbers_list(min: int, max: int):
    result_list = []

    while min <= max:
        result_list.append(min)
        min += 1
    
    return result_list
    
result = get_numbers_ticket(2, 500, 6)
print(result)
