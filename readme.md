# 8-Puzzle Solver With Reinforcement Learning
This project is all about creating a bot that is able to solve different configurations of the 3x3 sliding tiles puzzle. Reinforcement learning, specifically Q-learning, was used to create this bot. The bot was trained for about 12 hours and 30 million episodes. Currently, the bot is able to solve most given configurations but fails sometimes(this however, can be fixed with more training). 

## Methods
###  Engine Design
An engine was created that simulates the game itself. A transition matrix was created wherein for each state, the possible new states were detailed given each action. The engine is found in SlidingPuzzleEngine.py

### Environment Design
The environment inherits from OpenAi gym's Environment class. This is further detailed in SlidingPuzzleEnv.py

### Reward Design
A score per state was assigned based on the sum of powers of each of the numbers. Reward per move was calculated as:
$$reward = \delta stateScore - num_of_moves$$
This was done in order to penalize more moves and reward shorter number of moves. If the puzzle is solved, a reward of 10e10 was given, and if it wasn't able to solve within 50 moves, a reward of -10e11 was given

### Training
Here are the training parameters
* learning rate = 0.1
* max epsilon = 1.0
* min epsilon = 0.01
* epsilon decay = 0.0005
* gamma = 0.95
Training took about 12 hours and 30 million episodes. 

### Evaluation
Only preliminary evaluation has been done since this is a WIP, but the agent can solve most configurations so far.


## References
Much of this work is patterned from this [repository](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/FrozenLake/Q%20Learning%20with%20FrozenLake.ipynb)