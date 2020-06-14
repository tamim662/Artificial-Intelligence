# Steepest Ascent psuedocode


  fucntion Hill_climbing(problem)
  return a state that is local maximamum


```
    current <-- Make_Node(problrm.Intial_state)
    loop do :
    meighbour <--- a highest_valued successor of current
    if neighbour.Value <= current.Value then return current.State
    current <--- neighbour
```

# First Choice

**Take the first generated state having cost < Current.State**

>Problem: Sorting the list in ascending order