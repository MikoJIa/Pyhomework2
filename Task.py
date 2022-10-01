# Реализуйте алгоритм перемешивания списка.
import random
   
list1 = [1, 2, 3, 4, 5, 6] 
print (f'Список до перемешивания: {list1}')

list2 = random.sample(list1, len(list1))
  
print(f'Список после перемешивания: {list2}')



