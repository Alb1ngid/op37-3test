

# модули

# 1 встроенные модули
# import random
# print(random.randint(1,99))
#
# import math
# print(math.e)

# from math import pi
# print(pi)
# 2 собвственные модули

import lesson2
from lesson2 import *

a = Hum('beka', 27)
print(a)
# внешние модули
# venv - виртуальное окружение
# зависимости

from art import tprint
import colorama
print(colorama.Back.LIGHTMAGENTA_EX)
print(colorama.Fore.GREEN)
tprint('hello world 1')
