import random

random.randint(1,5)     # 1 and 5 are inclusive --- set [1,5]

random.randrange(1,5)   # returns a integer the belongs to the set [1,5)

random.random()         # set (0,1)

random.randrange(1,10,2) # range [1,10) 1 to 10 all the odd num only
random.randrange(2,11,2) # range [2,11) even

random.choice([1,2,3,4])