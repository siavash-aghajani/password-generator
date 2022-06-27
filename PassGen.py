import random ,string

def pass_gen():
    up_letters=list(string.ascii_uppercase) #   A-Z
    lo_letters=list(string.ascii_lowercase) #  a-z 
    numbers=['0','1','2','3','4','5','6','7','8','9']   # 0-9
    symbols=['?','!','@','#','$','%','(',')','+','-','*']

    num_uplet=int(input('how many uppercase letters you would like to use? '))
    num_lolet=int(input('how many lownercase letters you would like to use? '))
    num_sym=int(input('how many symbols would you like? '))
    num_int=int(input('how many numbers would you like? '))

    password=[]


    password.extend(list(random.sample(up_letters,num_uplet)))
    password.extend(list(random.sample(lo_letters,num_lolet)))
    password.extend((list((random.sample(numbers,num_int)))))
    password.extend(list(random.sample(symbols,num_sym)))
    random.shuffle(password)
    return ''.join((password))

