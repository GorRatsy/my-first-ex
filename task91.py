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
        
        
        if number in list(int(range(1, 51))):
            
            
            if number in list(int(range(1,26))):
                
                
                if number in list(int(range(1,21))):
                    s = 1
                    n = 20
                        
                
                elif number in list(int(range(21, 26))):
                    s = 21
                    n = 26
            
            
        if number in range(51, 101):
            
            
            if number in list(int(range(51, 76))):
                
                if number in list(int(range(51, 71))):
                    s = 51if number in list(int(range(51, 71))):
                    s = 51
                    n = 70
                    
                    
                elif number in list(int(range(71,76))):
                     s = 71
                     n = 75
                    n = 70
                    
                    
                elif number in list(int(range(71,76))):
                     s = 71
                     n = 75
            
            
            elif  number in list(int(range(76, 101))):
                
                
                if number in list(int(range(76,91))):
                    s = 76
                    n = 90
                    
                    
                elif number in list(int(range(91, 101))):
                     s = 91
                     n = 75
                
                
         
        if number == predict_number:
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

