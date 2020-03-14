from queue import PriorityQueue
class Node:
    def __init__(self,prev,node_key,cost,total_cost):
        self.prev=prev
        self.node_key=node_key
        self.cost=cost
        self.total_cost=total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def path_print(node):
    print("Cost")
    print(node.cost)
    #path=node
    path_list=''
    c = graph[node.node_key]
    path_list+=c
    while node.prev != -1:
        node=node.prev
        c=graph[node.node_key]
        path_list+=c
    print("Path is :",path_list[::-1] )        

graph={0:'S',1:'A',2:'B',3:'C',4:'D'}

adjacency_list=[  [-1,1,4,-1,-1],
                  [-1,-1,2,5,12],
                  [-1,-1,-1,2,-1],
                  [-1,-1,-1,-1,3],
                  [-1,-1,-1,-1,-1]]

l=adjacency_list[0]
#print(l)

H=[7,6,2,1,0]

n = Node(-1,0,0,0)
q = PriorityQueue()
q.put(n)

    
while not q.empty():
    current = q.get()
   # print(current.prev, current.node_key)
    if current.node_key  == 4:
        path_print(current)
        break
    u = current.node_key
    adj_list = adjacency_list[u]
    i=0
    #print(adj_list)
    for src in adj_list:
        
        if src == -1:
            i+=1
            continue
        Nob=Node(0,0,0,0)
        Nob.prev=current
        #print(i,src)
        Nob.node_key=i
        Nob.cost=current.cost+src
        Nob.total_cost=Nob.cost+H[i]
        q.put(Nob)
        i+=1

        

