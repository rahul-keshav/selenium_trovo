import string 
import random 

def random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N)) 
    return res

