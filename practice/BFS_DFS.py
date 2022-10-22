# Martin Hoang 

'''
Graph Traversal: DFS & BFS 


PSEUDOCODE: 
BFS
1. create visited set and queue 
2. add first vertex into visited and queue
3. Create a while loop that continues as long as the queue has values 
    i. print each popped value 
    ii. Check neighbors, if vertex isn't in graph, add to visited & queue 

DFS: 
1. create visited set and add current starting vertex 
2. print current vertex value 
3. check if neighboring node is in visited. If not apply recursion taking in the next node

NOTES: 
- A graph can be implemented using a dictionary.
- Another way of implementing a graph is using a matrix 

'''
graph = {
    '5': ['3', '7'],
    '3': ['2' ,'4'], 
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [] 
    }


def bfs(graph, vertex): 
    '''Implemented using a queue'''
    visited = set() 
    queue = [] 

    # how to add first vertex of the graph to the set and queue? I want 5 to be added in this case 
    visited.add(vertex) 
    queue.append(vertex)

    # loop through queue and print each element that's popped
    while queue != []:
        v = queue.pop(0) 
        print(v, end = ' ') 

        # for each element, check neighbors. If not visited then add to queue 
        for neighbors in graph[v]: 
            if neighbors not in visited: 
                visited.add(neighbors)
                queue.append(neighbors) 


bfs(graph, '5') 

print() 

visited = set()  
def dfs(graph, visited, vertex): 
    '''Implemented using recursion'''
    # create visited set and add current vertex 
    visited.add(vertex)
    print(vertex, end = ' ') 
    # how to move to next node? 
    for neighbors in graph[vertex]: 
        if neighbors not in visited:
            dfs(graph, visited, neighbors)

dfs(graph, visited, '5')

     
'''
QUESTIONS: 
- Can the global visited vertex be moved inside the DFS function? 


LESSONS LEARNED: 
BFS: 
- BFS implemented using a queue 
- Need to make 2 tracking variables: 
    1. visited, a set 
    2. queue = [] 
- For each vertex, loop through it's neighbors and append to queue if the vertex isn't within visited set 


DFS: 
- takes in visited, graph, and vertex 
- append starting vertex to visited set and print it 
- visited set is a global var 
- loop through dictionary and pass in the value of each current vertex inside the recursive function > do this only if vertex isn't part of visited set 


CODE IMPROVEMENT: 
- It's better to have the program take in a starting node for bfs because it's not always a tree with a root node at the beginning 

'''