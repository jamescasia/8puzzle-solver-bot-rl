import random as rand
import numpy as np
 
class SlidingPuzzleEngine:
    def __init__(self, states_val_dict, states_num_dict, trans_matrix, goal_state):
        self.TOPS = [0,1,2]
        self.RIGHTS = [2,5, 8]
        self.LEFTS = [0, 3, 6]
        self.BOTTOMS = [6, 7, 8]
        self.moves = ["Up", "Down", "Left", "Right"]
        self.states_val_dict = states_val_dict
        self.states_num_dict = states_num_dict
        self.trans_matrix = trans_matrix
        self.goal_state = goal_state
    
    def _swap(self, arr, in1, in2):
        temp = arr[in2]
        arr[in2] = arr[in1]
        arr[in1] = temp
         
    def move(self,stateNum, m):
        stateValue = (list(self.states_num_dict[stateNum]))
        nextStateValue = stateValue
        
        if m == 1 or m == "Up":
            if not stateValue.index(0) in self.TOPS:
                self._swap(stateValue, stateValue.index(0), stateValue.index(0)-3) 
            else:
                nextStateValue = stateValue
                
        
        elif m == 2 or m == "Down":
            if not stateValue.index(0) in self.BOTTOMS:
                self._swap(stateValue, stateValue.index(0), stateValue.index(0)+3) 
            else:
                nextStateValue = stateValue 
        
        elif m == 3 or m == "Left":
            if not stateValue.index(0) in self.LEFTS:
                self._swap(stateValue, stateValue.index(0), stateValue.index(0)-1) 
            else:
                nextStateValue = stateValue
            pass
        
        else:
            if not stateValue.index(0) in self.RIGHTS:
                self._swap(stateValue, stateValue.index(0), stateValue.index(0)+1) 
            else:
                nextStateValue = stateValue
            pass
        
        nextState = self.states_val_dict[(tuple(nextStateValue))]
        return (nextStateValue), nextState
    
    def display(self, stateNum):
        stateVal = (self.states_num_dict[stateNum] )
        print(stateVal)
        
        print("-------------")
        print("|" ,stateVal[0] , "|", stateVal[1], "|", stateVal[2], "|")
        print("-------------")
        print("|" ,stateVal[3] , "|", stateVal[4], "|", stateVal[5], "|")
        print("-------------")
        print("|" ,stateVal[6] , "|", stateVal[7], "|", stateVal[8], "|") 
        print("-------------")
        
    def distance(self, stateValue):
        goalState = [0,1,2,3,4,5,6,7,8]
        return sum([abs(stateValue.index(a) - a) for a in stateValue ])
    
    def stateScore(self, stateNum):
        stateValue = self.states_num_dict[stateNum]
        return sum([ (stateValue[i])**(1+i) for i in range(9)])
    
    
    def getAllowedActions(self, state):
        allowedActions = np.asarray(self.trans_matrix[state, 1:5] != state)*[1,2,3,4]
        allowedActions = allowedActions[allowedActions >0]-1 
        
        return allowedActions
        
    
    def shuffle(self):
        stateVal = [0,1,2,3,4,5,6,7,8]
        state = self.goal_state  
        moves = rand.randint(1,70) 
        for i in range(moves):
            stateVal, state = self.move(state, self.moves[rand.sample(list(self.getAllowedActions(state)), 1)[0]] )
            
            
        return stateVal,  state
    
