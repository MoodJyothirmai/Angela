import random
import my_module #To use value of other python files in same directory by importing
# By importing the python file
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_module)