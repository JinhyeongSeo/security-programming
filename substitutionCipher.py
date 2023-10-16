import string
import random

all_letters = string.ascii_letters
shuffled_all_letters = ''.join(random.sample(all_letters,len(all_letters)))

dict1 = {}

for i in