
import gym
import math 
import random as rand 
import numpy as np
class SlidingPuzzleEnv(gym.Env):
    
    def __init__(self, engine, qtable, states_val_dict, trans_matrix, goal_state):
        self.trans_matrix = trans_matrix
        self.states_val_dict = states_val_dict
        self.actions = ["Up","Down","Left", "Right"]
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Discrete(9)
        self.engine = engine
        self.stateVal,_ = self.engine.shuffle()
        self.state = self.states_val_dict[tuple(self.stateVal)]
        self.moves = 0
        self.qtable = qtable
        self.goal_state = goal_state
        
    def step(self,action, max_steps): 
        self.moves+=1
        prevState = self.state
        prevStateScore = self.trans_matrix[prevState, 5]
        self.stateVal, self.state = self.engine.move(self.state,action)  
        stateScore = self.trans_matrix[self.state, 5]
        reward = stateScore - prevStateScore - self.moves
        done = self.state == self.goal_state 
        if done:
            reward += 1000000000
        elif self.moves == max_steps:
            reward += -10000000000
            
        
        return self.state, reward, done , {}
    
    
    def getAllowedActions(self, state): 
        return self.engine.getAllowedActions(state)
        
    
    
    def reset(self):
        self.stateVal, self.state = self.engine.shuffle() 
        return self.state 
    
    def given(self):
        self.state = self.states_val_dict[(7,2,4,5,0,6,8,3,1)]
        return self.state
    
    def getBestAction(self, state):
        allowedActions = self.getAllowedActions(state)

        bestActionIndex = 0
        bestScore = -math.inf
        for al in allowedActions:
            score = self.qtable[state,al] 
            if score > bestScore:
                bestScore = score
                bestActionIndex = al
        return bestActionIndex
    
    def getBestScore(self, state):
        allowedActions = self.getAllowedActions(state)
  
        bestScore = -math.inf
        for al in allowedActions:
            score = self.qtable[state,al] 
            if score > bestScore:
                bestScore = score 
        return bestScore
    
    def getRandomAction(self, state):
        
        allowedActions = self.getAllowedActions(state)
        return rand.sample(list(allowedActions), 1)[0]
        
    
    
    
    

        
    