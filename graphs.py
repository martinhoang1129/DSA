# Martin Hoang 

'''
Graphs DS 
Purpose of this program is to understand graphs DS 

PSEUDOCODE: 
1. 

NOTES: 
- Represent graphs using 2 methods 
    - adj list 
    - matrix 

- How to implement an adj list? 
    - A: B, C, E
    - B: C, E

- How to implement adj matrix? 
    - Adj matrix has from on left column and to as rows 
    - In undirected graph, the diagonal is 0 

- How to represent weighted graph in matrix? 
    - multiply 1*Weight as value 

- Sparse vs dense graph? 
    - sparese = not many nodes connected
    - dense = many connected nodes 

- when to use adj list vs matrix? 
    - adj list better for spares and matrix better for dense graphs 

- How much memory does adj matrix take up? 
    - matrix takes up elements^2 bytes 

'''

class Vertex: 
    '''
    Vertex class has name as a value and neighbor as list 
    '''
    def __init__(self, n): 
        # Vertext has n as a value and a list of potential neighboors 
        self.name = n 
        self.neighbor = [] 

    def add_neighbor(self, vertex):
        if vertex not in self.neighbor: 
            self.neighbor.append(vertex) 
            self.neighbor.sort() 

class Graph: 
    '''
    Graph class initially an empty dict

    Following methods: 
    1. add_vertex
    2. add_neighbor
    3. print_graph 
    '''
    def __init__(self): 
        self.graphdict = {} 

    def add_vertex(self, vertex): 
        # is the vertex the same instance as Vertex class?
        # is vertex in graph.dict? If not then add into graphdict 
        if isinstance(vertex, Vertex) and vertex not in self.graphdict: 
            self.graphdict[vertex.name] = vertex.neighbor      # append to dictionary by adding K:V 
            return True 
        else:
            return False  

    def add_edge(self, u, v): 
        # are u and v vertices within the graphdict? 
        # If vertices, then traverse dictionary > for key = u, add V to neighbor, for key = v, add U as neighbor 
        # u and v are vertex obj so I want to check if the names are in the dict 
        if u.name in self.graphdict and v.name in self.graphdict: 
            for vertex, neighbor in self.graphdict.items(): 
                if vertex == u.name: # how to update dictionary Value and append new vertex neighbor? 
                    neighbor.append(v.name)
                if vertex == v.name: 
                    neighbor.append(u.name)

    def print_graph(self): 
        # loop through dictionary and print K:V pairs. V will be list format 
        for vertex, neighbor in self.graphdict.items(): 
            print(f"Vertex: {vertex}, Neighbor: {neighbor}")


a = Vertex('a') 
# print(a)                # prints it as vertex obj with location in memory 
b = Vertex('b') 
b.add_neighbor('a') 
a.add_neighbor('b') 
c = Vertex('c') 

graph = Graph()
graph.add_vertex(a) 
graph.add_vertex(b) 
graph.print_graph() 
print()
graph.add_vertex(c) 
graph.print_graph()
print() 

graph.add_edge(a, c) 
graph.print_graph() 



'''
QUESTIONS: 
-


LESSONS LEARNED: 
- In order to make a graph need 2 classes: vertex and graph 

- add_vertex: 
    1. check if vertex isinstance Vertex class, the same obj and if the vertex is already in the dict? 
    2. If not then update dictionary with vertex.name and vertex.neighbor 

- add_edge:
    1. check if u.name and v.name is in dictionary.items() 
    2. If yes, loop through dict 
        i. if vertex = u.name > append v.name to list 
        ii. if vertext = v.name > append u.name to list 
- print_graph method: 
    1. iterate through self.graphdict and print K:V 


CODE IMPROVEMENT: 
- 

'''