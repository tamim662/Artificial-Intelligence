import random
import main
import math
import sys

def exp_schedule(k=4, alpha=1, limit=10):
    return  t: ((k-1) * (alpha * t) if t < limit else 0)

def heuristic(current_state,ind):
    prev_state=current_state
    prev_state_cost = calc_cost(current_state)
    current_state = []
    
    for j in range(len(prev_state)):
        if j is not ind:
            current_state.append(prev_state[j])   
    current_state_cost = calc_cost(current_state)

    if(current_state_cost < prev_state_cost):
        return current_state_cost
    else:
        return prev_state_cost
    




def simulated_annealing(state, schedule=exp_schedule()):
    current = init()
    ind=1
    current_h = heuristic(current,ind)
    for t in xrange(sys.maxsize):
        T = schedule(t)

        ind+=1
        if T == 0 or problem.goal_test(current):
            return current
        neighbour = heuristic(current_h,ind)
        if not neighbour:
            return current
        
        new_h = heuristic(neighbour)
        delta_e = new_h - current_h
        
        if delta_e > 0 or math.exp(delta_e / T) > random.uniform(0.0, 1.0):
            current = neighbour
            current_h = new_h