import random

def banner():
    print('''
 ____  _            ____  _                 _       _             
|  _ \(_) ___ ___  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
| | | | |/ __/ _ \ \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |_| | | (_|  __/  ___) | | | | | | | |_| | | (_| | || (_) | |   
|____/|_|\___\___| |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   

Creator : amirhoseinsohrabi
Gmail : amirhoseinsohrabi.official@gmail.com
                                                                  
    ''')
def dice(input_):
        input_ = int(input_)
        test = random.randint(1,6)
        for i in range(input_):
            test
            i+=1
            if i == input_:
                print(test)

