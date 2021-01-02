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

dict1 ={
    'test':[1]
}
clmn = ['email','username','password']

dict2 = {
        "email":[],
        "username":[],
        "password":[]
        }

def save_cred(email,username,password):
    try:
        df2 = pd.read_csv('username_password.csv')
    except:
        df2 = pd.DataFrame(dict2)
    
    df0 = pd.DataFrame([[email, username, password]], columns=clmn)
    df = df2.append(df0,ignore_index=True)    
    df.to_csv('username_password.csv',index=False)













        

