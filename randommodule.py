import random
import myrandommodule

#random_int = random.randint(1,10)
#print(random_int)

#print(myrandommodule.my_number)
#random_number_0_to_1 = random.random() 
#print(random_number_0_to_1)

#random_float = random.uniform(1,10)
#print(random_float)

random_head_or_tail = random.randint(0,1)
if random_head_or_tail == 0:
    print("Head")
else:
    print("Tail")