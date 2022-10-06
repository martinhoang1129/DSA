# Martin Hoang 

'''
Heapsort 
Applying heapsort to a list of unsorted integers 

PSEUDOCODE: 
1. create 2 functions: one is heapsort, the other is heapify 
    i. heapsort function: takes the heap and switches it with the last node. Need to sort multiple nodes because it has not been sorted yet. sorts from 2nd to last row, which is size//2-1. 
       creates heap from bottom up approach 
    ii. heapify function: recursively creates a heap. Takes in size and i. size decreases each heapsort because each iteration moves the root node to the end of the array  
2. Call heapsort to build a max heap in the beginning 
3. create a loop that switches the root node and last node, then calls heapsort 

NOTES: 
- heapsort sorts the array with a time complexity of O(nlogn) 
- a heap is a tree representation of an array. The nodes are represented using l = 2*i + 1, r = 2*i + 2 
'''

unsorted_list = [1, 100, 3, 9, 5, 33, 13]

def heapsort(list): 
    size = len(list) # 7 
    # first create the heap 
    # create heap starting from 2nd to last row from the bottom 
    for i in range(size//2 - 1, -1, -1): # i = 1,0 
        heapify(list, size, i)      

    # switch root node and last node, then decrement by 1 
    for i in range(size-1, 0, -1): 
        list[0], list[i] = list[i], list[0]
        heapify(list, i, 0)  # only need to heapify the root node because all other numbers are in order. The root node is currently unsorted 

    return list 

def heapify(list, size, i):
    cur = i 
    left = 2*i + 1 
    right = 2*i + 2   

    # if value is less, then switch values 
    # only choosing nodes where the index < current size of heap (size) 
    if left < size and list[cur] < list[left]:
        list[cur], list[left] = list[left], list[cur]
        heapify(list, size, left)           # need to heapify starting from swapped node to see if it's in place. The top node/cur is in place already bc of the swap 
    if right < size and list[cur] < list[right]:
        list[cur], list[right] = list[right], list[cur] 
        heapify(list, size, right)

print(heapsort(unsorted_list))

''' 
LESSONS LEARNED: 
- heapsort has 3 steps
    1. heapify all nodes 
    2. swap the root node w the last node and heapify the new root node (only 1 node) 
    3. heapify function takes size & i (current node) as input. heapify is a recrusive function so there's heapify within heapify 
- a heap is a tree representation of an array. We create the heap using max = i, left = 2*i + 1, right = 2*i + 2
- The first step in heapsort is to create the heap. Creating the heap means calling heapify multiple times because there are multiple unsorted nodes. Heapify starts soring from 2nd to bot row 
- Within the root node swap w the last node, heapify is called again because the root node isn't max. Here heapify is called but the index i = 0, size = i because the size of the heap decreased by 1 
- 
'''