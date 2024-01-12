import string
import random
P=1
N = 16
while P==1: 
    print(str(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N))))
