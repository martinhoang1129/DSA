# Martin Hoang 

'''
Hashtable 
The objective of this program is the implementation of a hashtable using a list. It's important understanding hashtables because that's how a dictionary is implemented. With a hashtable
There is constant time insertion, deletion, searching 

PSEUDOCODE: 
1. create class hashtable and it's constructor (size, empty list) 
2. create hash function to return a hash value. The hash value is the index of the hash table 
3. insert function: stores key_value pair at the index of the hash table 
4. delete function: calculates hash and then finds the key_value at the hash value 
5. search function: calculates hash using key and returns key_value at hash value 
6. print function

NOTES: 
- insertion, deletion, search all uses hash value
- A dictionary is a black box that calculates the hash value and then stores K:V pairs. A hash table dymistifies the black box by showing the hash function and collisions 
'''

class hashmap(): 
    def __init__(self): 
        self.size = 13 
        self.hashmap = [None]*self.size 

    def get_hash(self, key): 
        '''
        hash function takes a key and returns the hash value
        Division hash function using hash table that's a prime number
        '''
        hash = key % self.size 
        return hash 

    def insert(self, key): 
        hash = self.get_hash(key) 
        self.hashmap[hash] = key 

    def delete(self, key): 
        hash = self.get_hash(key) 
        self.hashmap[hash] = None  

    def search(self, key): 
        hash = self.get_hash(key)
        return self.hashmap[hash]  

    def print(self): 
        for i, ele in enumerate(self.hashmap): 
            print(f'{i}: {ele}') 


class hashmap_chaining(): 
    def __init__(self): 
        # For chaining, implementing a nested list 
        self.size = 13 
        self.hashmap = [[] for i in range(self.size)] 

    def get_hash(self, key): 
        '''
        hash function takes a key and returns the hash value
        Division hash function using hash table that's a prime number
        '''
        hash = key % self.size 
        return hash 

    def insert(self, key): 
        # first check if previous key exist. If so then add to end. If not then update [] 
        hash = self.get_hash(key)
        self.hashmap[hash].append(key) 

    def delete(self, key): 
        hash = self.get_hash(key) 
        for i in range(len(self.hashmap[hash])): 
            if self.hashmap[hash][i] == key: 
                self.hashmap[hash].remove(key) 
                return 

    def search(self, key): 
        hash = self.get_hash(key)
        found = False 
        for i in range(len(self.hashmap[hash])): 
            if self.hashmap[hash][i] == key: 
                found = True 
                return found 
        return found

    def print(self): 
        for i, ele in enumerate(self.hashmap): 
            print(f'{i}: {ele}') 


h = hashmap()
h.insert(10) 
h.insert(9)
h.insert(5) 
h.insert(15)
h.insert(100)   # there is a collision at index 9. The original 9 got replaced with 100 and it's gone. Should implement chaining 
h.print()

print('\nImplementing chaining using nested list') 
h2 = hashmap_chaining()
h2.insert(9)
h2.print()
h2.insert(100) 
h2.print()
for i in range(50): 
    h2.insert(i) 
h2.print()
h2.delete(12)
h2.print()
print(h2.search(103))


print([None]*5)  
print([[]]*5)
print([[] for i in range(5)])   # correct way of having a list within a list 

'''
QUESTIONS: 
- When to use a hashmap over a dictionary? 
    - A dictionary is implemented using a hashmap. They both have constant time insertion, deletion, accessing
- What's the difference btwn a dictionary and a hashmap? 
    - a dictionary is a generic implementation of a hashmap while a hashmap is a specific method using a specific hash function 


LESSONS LEARNED: 
- In a hash table, the data is not sorted. This is similar to a dictionary 
- When accessing [] within hash table, it's a [[]]. There is nothing inside that list. So it skips the line when setting if ele == []. It's essentially blank 
- To implement chaining just make [[]] > Need to explicitly loop to make the multiple empty list within the list 


CODE IMPROVEMENT: 
- 
'''