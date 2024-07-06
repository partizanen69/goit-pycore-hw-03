import random

def get_numbers_ticket(min: int, max: int, quantity: int):
  if min < 1:
    print("min must be greater than 0")
    return []
  
  if max > 1000:
    print("max must be less than or equal 1000")
    return []
  
  if quantity > max or quantity < min:
    print("quantity must be betwen min and max")
    return []
  
  set_of_numbers = set()

  while len(set_of_numbers) < quantity:
    random_number = random.randint(min, max)
    set_of_numbers.add(random_number)

  list_of_numbers = list(set_of_numbers)
  list_of_numbers.sort() 

  return list_of_numbers

numbers = get_numbers_ticket(1, 1000, 10)
print(numbers)

