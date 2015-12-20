# Modify Exercise 3-1 to extract all program logic in a separate module.

import random
import string
from Lesson03.Exercise3_1_modified import string_sorter

rand_str = ''.join(random.choice(string.lowercase) for _ in range(100))

string_sorter(rand_str)
