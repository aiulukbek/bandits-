import numpy as np 
from typing import List  

class StochasticBandit: 
    def __init__(self, action_probabilities: List): 
        self.probs = action_probabilities 
        self.K = len(self.probs)

    def run_arm(self, index: int) -> int: 
        '''
            this is simple MDP : there is no states and thus we are not returning next state 
            we are selecting only action and obtain the corresponding reward 
        '''
        if  index > self.K: 
            raise IndexError("Index is greater than the number of arms.")
        if np.random.random() < self.probs[index]: 
            return 1 
        else: 
            return 0
        

        
