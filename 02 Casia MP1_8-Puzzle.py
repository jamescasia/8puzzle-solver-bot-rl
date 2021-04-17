

import pickle
import random as rand
import random
import gym
import pandas as pd
import math
import numpy as np
from SlidingPuzzleEngine import SlidingPuzzleEngine
from SlidingPuzzleEnv import SlidingPuzzleEnv

def strToArray(s):
    return [int(a) for a in s[1:-1].split(',')]


num_configs = math.factorial(9)
GOAL_STATE_VAL = (0,1,2,3,4,5,6,7,8)
GOAL_STATE = 322560 
trans_matrix = np.load("trans_matrix.npy")
states_df = pd.read_csv("states.csv")   
qtable = np.load('qtable2.npy')
max_steps = 50
with open('states_val_dict.p', 'rb') as s1:
    states_val_dict = pickle.load(s1)

with open('states_num_dict.p', 'rb') as s2:
    states_num_dict = pickle.load(s2)
    

    

sEngine = SlidingPuzzleEngine(states_val_dict, states_num_dict, trans_matrix, GOAL_STATE)
env = SlidingPuzzleEnv(sEngine, qtable, states_val_dict, trans_matrix,GOAL_STATE)
    
def solveRandomPuzzle():
    state = env.reset()
    step = 0
    done = False
    for step in range(max_steps): 
        action = env.getBestAction(state)

        new_state, reward, done, info = env.step(env.actions[action], max_steps)
        if step == 0 or step == max_steps-1 or True :
            sEngine.display( state )
            print("step:", step) 
        if done:
            sEngine.display(new_state)
            print("Number of steps", step)
            if new_state == GOAL_STATE:
                print("Puzzle solved!🏆")
            else:
                print("You failed ☠️")


            break
        state = new_state 
        
def solveGivenPuzzle(): 
    state = env.given()
    step = 0
    done = False
    for step in range(max_steps): 
        action = env.getBestAction(state)

        new_state, reward, done, info = env.step(env.actions[action], max_steps)
        if step == 0 or step == max_steps-1 or True :
            sEngine.display( state )
            print("step:", step) 
        if done:
            sEngine.display(new_state)
            print("Number of steps", step)
            if new_state == GOAL_STATE:
                print("Puzzle solved!🏆")
            else:
                print("You failed ☠️")


            break
        state = new_state 
        
        
print("This program attempts to solve the 8 sliding puzzle using Qlearning. P.S. This bot can't solve every configuration, but it can solve most of them.\n")
i = str(input("Would you like it to solve a random puzzle or the given? Press 'R' for random puzzle. Press 'G' for given\n"))

if i.strip()  in ( "R" , 'r'):
    solveRandomPuzzle()
elif i.strip() in  ("G" ,  'g'):
    solveGivenPuzzle()
else:
    print("Thank you!") 