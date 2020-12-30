import string 
import random 
import pandas as pd

def random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N)) 
    return res

df = pd.read_csv('name_1k.csv')
name = list(df['Name'])
def user_name():
    user = random.choice(name)
    subs = random_string(7)
    user_name = user + '_' + subs
    return user_name


