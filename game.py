import numpy as np

number = np.random.randint(0,101) #make a number
count = 0

while True:
    count+=1
    predict_number = int(np.random.randint(0,101))
    
    if predict_number > number:
        print('Number mist be smaller')
    
    elif predict_number < number:
        print ('Number must be bigger')
        
    else:
        print(f'Thats right! That was number {number}, for {count} tryings')
        break