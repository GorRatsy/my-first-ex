import numpy as np

def random_predict(number:int=1)-> int:
    """[summary]

    Args:
        number (int, optional): [int]. Defaults to 1.

    Returns:
        int: [description]
    """
    count = 0
    s = 1
    n = 101
    
    while True:
        count += 1
        predict_number = np.random.randint(s, n)
        num_list = []  # list generator
        for i in range(1,101):
            num_list.append(i) 
        
        n1 = num_list[:20]
        n2 = num_list[20 : 40]
        n3 = num_list[40 : 60]
        n4 = num_list[60 : 80]
        n5 = num_list[80 : 99]
        
        
        if number in n1:
            s = num_list[0]
            n = num_list[19]
            
            
        elif number in n2:
            s = num_list[20]
            n = num_list[39]
            
        
        elif number in n3:
            s = num_list[40]
            n = num_list[59]
            
            
        elif number in n4:
            s = num_list[60]
            n = num_list[79]
            
            
        elif number in n5:
            s = num_list[80]
            n = num_list[99]
            
            
        elif number == predict_number:
            break
    
    return count


def score_game(random_predict)-> int:
    
    
    """How much predict

    Args:
        random_predict ([function]): [functiion of predicting numbers]

    Returns:
        int: [middle num of trying]
    """
    
    
    count_is = []  # list of trying
    np.random.seed(1)  # number of finish cases
    r_array = np.random.randint(1, 101, size = (1000)) 
    # list of numbers that computer must to predict
    
    
    for number in r_array:
        count_is.append(random_predict(number))
        
    
    score = int(np.mean(count_is)) # count middle num from array o tryings
    print(f'Middle num of trying is {score}')
    return score


score_game(random_predict)

