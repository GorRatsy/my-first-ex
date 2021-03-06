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
            
        
        if number > predict_number:
            s = predict_number
            n = 101
            predict_number = np.random.randint(s, n)
            count += 1
            
            
            if number > predict_number:
                 s = predict_number
                 n = 101
                 predict_number = np.random.randint(s, n)
                 count += 1
                 
                 
                 if number > predict_number:
                     s = predict_number
                     n = 101
                     
                     
                 elif number < predict_number:
                     n = predict_number
                     
                 
                 elif number == predict_number:
                     break
            
            
            elif number < predict_number:
                n = predict_number
                predict_number = np.random.randint(s, n)
                count += 1
                
                
                if number < predict_number:
                    n = predict_number
                    
                
                elif number > predict_number:
                    s = predict_number
                 
                                       
                
            elif number == predict_number:
                break
             
           
            
        elif number < predict_number:
            s = 1
            n = predict_number
            count += 1
            predict_number = np.random.randint(s, n)
        
        
            if number < predict_number:
                n = predict_number
                count += 1
                predict_number = np.random.randint(s, n)
                
                
                if number < predict_number:
                    n = predict_number
                    
                    
                elif number > predict_number:
                    s = predict_number
                    
                
                elif number == predict_number:
                    break
                
                
            elif number > predict_number:
                s = predict_number
                
            
            elif number == predict_number:
                break
        
        elif number == predict_number:
            break  # exit from cycle
        
        
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

