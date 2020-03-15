def init():
    ilist=[2,1,5,0,8,4,10,0,20,10]
    return ilist

#ilist=[1, 2, 5, 0, 8, 4]

def calc_cost(state):
    cost=0
    l=len(state)
    for i in range(l):
        for j in range(i+1,l):
            if(state[i]>state[j]):
                cost+=1

    
    return cost
def State_generation(current_state,current_state_cost, ind):
    
    prev_state=current_state
    prev_state_cost = current_state_cost
    current_state = []

    current_state.append(prev_state[ind])

    for j in range(len(prev_state)):
        if j is not ind:
             current_state.append(prev_state[j])   
    current_state_cost = calc_cost(current_state)

    if(current_state_cost < prev_state_cost):
        return current_state, current_state_cost
    else:
        return prev_state, None





def goal_test(state):
    if calc_cost(state) == 0:
        return True
    else:
        return False

def main():
    state = init()
    cost=0
    ind = 1
    #cost=calc_cost(state)
    while(goal_test(state)!=True and ind < len(state)):
        state, cost = State_generation(state, calc_cost(state), ind)
        ind+=1
        if cost is None:
            print(state) 
            break
            
    print(state)  # Steepest Ascent
    

if __name__ == '__main__':
    main()    


#calc_cost(ilist)