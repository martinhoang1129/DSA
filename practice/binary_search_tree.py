# Martin Hoang 

'''
Binary Search Tree 
Purpose of this code is to learn how to make a BST 

PSEUDOCODE: 
1. create node class with value, left and right as constructors 
2. create BST class with root node as constructor. Not applying inheritance in BST class but will be using node class within BST 
3. Make add, find, print functions 
4. add and find function works similarly. Traverse tree starting from root node and use recursion to move. 
    i. if root = NONE > return False (base case) 
    ii. if root = target > return target 

NOTES: 
- 

'''
class node(): 
    def __init__(self, value): 
        ''' 
        defining each node with value and having 2 child nodes
        New node must have a value = data 
        It has left and right node attribute, but for now they are None until set within BST 
        '''
        self.value = value
        self.left = None 
        self.right = None 

# 5, 3, 10 
class BST(): 
    def __init__(self): 
        '''initially BST root is None'''
        self.root = None      

    def insert(self, value): 
        '''Insert parent function takes in a value. _insert is the recursive child function'''
        # if root has no value, then the first node is the root 
        if self.root == None:
            self.root = node(value) 
        
        # want to have a seperate function called by insert. _insert will be recursive. code is more clean rather than having insert w/ all conditions  
        else: 
            self._insert(value, self.root)   # recursive function will start with root node. _insert will compare data to root.value 
    
    def _insert(self, value, cur_node): 
        '''recursive child function'''
        if value < cur_node.value: 
            if cur_node.left == None:                   # first left node 
                cur_node.left = node(value) 
            else: 
                self._insert(value, cur_node.left)      # if 2nd left node, then insert and compare value w cur_node.left 
        elif value > cur_node.value: 
            if cur_node.right == None: 
                cur_node.right = node(value) 
            else: 
                self._insert(value, cur_node.right)
        else: 
            print(f'Value already exist: {value}')

    def search(self, value): 
        # check tree exist 
        if self.root == None: 
            print('There is no tree')
        else: 
            self._search(value, self.root) 
    
    def _search(self, value, cur_node): 
        if cur_node == None: 
            print(f'{value} is not found within the BST')
        elif value == cur_node.value: 
            print(f'{value} is found within the BST')
        elif value < cur_node.value:        
            self._search(value, cur_node.left)  
        elif value > cur_node.value: 
            self._search(value, cur_node.right)  
            
    def print_tree(self): 
        '''Printing BST inorder sequence'''
        if self.root != None: 
            self._print_tree(self.root) 
        else: 
            print('Tree has no value')
    
    def _print_tree(self, cur_node): 
        '''Recrusive private print tree function. Splitting print into 2 functions'''
        # Similar to a Linked list, traversing a BST by setting if cur_node != None, then traverse
        if cur_node != None: 
            self._print_tree(cur_node.left)
            print(cur_node.value) 
            self._print_tree(cur_node.right) 

    def sum_tree(self):
        '''sums all int within the BST. Takes root node as input'''
         # Can traverse tree inorder and then sum all int 
        if self.root != None: 
            return self._sum_tree(self.root)
        else: 
            print('Cannot sum because no tree')
        
    def _sum_tree(self, cur_node): 
        '''private function. This is a child function of sum_tree, the parent'''
        if cur_node == None: 
            return 0 
        sum = cur_node.value + self._sum_tree(cur_node.left) + self._sum_tree(cur_node.right)      # sum = cur_node.value + left.value + right.value, 
        return sum 



b = BST()
b.insert(5)
b.insert(3)
b.insert(1) 
b.insert(10)
b.insert(10)
b.insert(4)  
b.print_tree()
sum = b.sum_tree()
print(sum)
b.search(200)



'''
QUESTIONS: 
- How exactly to call add to traverse the tree using recursion? 
- How to find recursive function? 
    - draw out the pattern, write in terms of math, and then translate to code 
- Why use private functions? 
    - private function can seperate recursive part from the non recursive part. This makes it easier to understand/code 
- 


LESSONS LEARNED: 
- sum_tree: 
    - 2 functions: 1 passing in starting root node. 2nd function takes cur_node and traverses tree returning sum 
    - recursive function: sum = cur_node + sum(cur_node.L) + sum(cur_node.R) 
- print_tree: 
    - check if root node has a value. If not then return no Tree 
    - If there is value, call child print_function(cur_node) 
    - if cur_node has value, traverse left
        i. _print_tree(cur_node.left) 
        ii. print(cur_node.value) 
        iii. print(cur_node.right) 
- insert(value): 
    1. first see if self.root has value. If not then set root to node 
    2. else, call private _insert function(value, cur_node): 
        i. if value < cur_node.value: traverse left
            a. if cur_node.left == None: 
                cur_node.left = value 
            b. else: keep traversing 
                _insert(value, cur_node.left) 
        ii. if value > cur_node.value: traverse right
        iii. else: Already have value within tree 

CODE IMPROVEMENT: 
- 

'''