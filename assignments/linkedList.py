# Martin Hoang
# Lab 11 
# Professor: Ivan T. 
# 7/15/22 

# Appliication of linkedlist - insertion, deletion, updating, searching 

# subclass of linkedlist 
class node:     
    # creating building block of linked list, a node and pointer slot 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None        # allocate memory but it doesn't point to anything here 

class linkedList: 
    # Starting creating a linkedList. Initially LL is empty 
    def __init__(self): 
        self.head = node() 
    
    # append method 
    # adding node at end 
    def append(self, data): 
        new_node = node(data) 
        cur = self.head 
        # Need to traverse through LL and look for last node where cur.next == None, then append there 
        # cur only moves when next is linked, or isn't None 
        while cur.next != None: 
            cur = cur.next 

        # After traversing LL, we are at the last node now
        # append new_node 
        cur.next = new_node 

        # steps to append
        # 1. Create new_node 
        # 2. Create cur = head 
        # 3. Look for last node in LL by traversing > while cur.next != None, cur = cur.next 
        # 4. cur.next = new_node > this appends to latest node 

    # length method 
    def length(self): 
        length = 1 
        cur = self.head 
        # get length by adding 1 everytime we traverse LL 
        while cur.next != None: 
            cur = cur.next 
            length += 1 
        return length 

    # display method 
    # take value, store in var and display in list 
    def display(self): 
        list = [] 
        cur = self.head 
        while cur.next != None: 
            cur = cur.next  # want to move to current element then append node data 
            list.append(cur.data)
        print(list) 



    # deletion method 
    # delete at certain index 
    # if count == index, take previous node and link to next one 
    # must have a temp variable storing last node > last_node 
    def delete(self, index): 
        cur = self.head 
        count = 0  

        while True: 
            last_node = cur
            cur = cur.next 
            if count == index: 
                last_node.next = cur.next 
                return 
            count += 1 
                
    # searching method 
    # search of value within LL and return True/False
    def search(self, value): 
        cur = self.head 
        while cur.next != None: 
            cur = cur.next 
            if cur.data == value: 
                return print('{} is within the linked list'.format(value)) 
        return print('{} is not within the linked list'.format(value))  

    # updating method 
    # update value at user defined index 
    def update(self, index, value): 
        cur = self.head
        count = -1
        while True:   
            if count == index: 
                cur.data = value  
                return 
            cur = cur.next
            count += 1 

    # there is 1 empty node, thats why count starts from -1, else usually starts from 0 




