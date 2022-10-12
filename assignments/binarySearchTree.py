class node: 
    # constructor making node DS 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

class BST: 
    # constructor creating root node 
    def __init__(self): 
        self.root = None # either node or none 
    

    def insert(self, data): 
        # creating new node 
        root = self.root 
        new_node = node(data) 

        # root node 
        # creates root node if there's no root node yet 
        if root == None: 
            return root == new_node

        # left tree 
        # if new node is less than root, insert new node left of root 
        elif new_node < root: 
            root.left = self.insert(new_node)
        
        # right tree 
        # if new node is > root, insert right 
        else: 
            root.right = self.insert(new_node) 

    # print in order 
    def inorder(self): 
        root = self.root 
        
        if root.data != None:
            self.inorder(root.left)
            print(root.data) 
            self.inorder(root.right) 
    


a = BST() 
a.insert(5)
a.insert(3)
a.insert(10) 
a.inorder() 
