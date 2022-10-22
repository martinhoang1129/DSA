# Martin Hoang 

'''
Binary Search 
The purpose of this program is to perform binary search on a sorted list. Binary search has a time complexity of O(log n), essentially a dictionary split. 

PSEUDOCODE: 
1. Define target, size, left, right 
2. apply while loop when l < r: (base case for recursion). Loop will break and return not Found if l = r (one element left) 
3. 3 conditions, else not found: 
    i. tar < mid: 
    ii. tar > mid: 
    iii. tar = mid 

NOTES: 
- Binary search only works on sorted list. It leverages the power of the sort to do a dictionary split 
- Time complexity of O(log n) means that after every split, the list is halved. This is extremely powerful because even with ~4billion elements, it'll take only 32 splits to reach 1 

'''
# list = [1, 3, 10, 11, 13]

def binary_search(list, target): 
    # using indexes to define left, right, mid 
    size = len(list)
    left = 0
    right = size-1
    mid = int((left + right) / 2)
 
    if left <= right: 
        if target == list[mid]: 
            return list[mid] 
        elif target < list[mid]: 
            list = list[0:mid]  # new list includes middle number now 
            return binary_search(list, target) # TO USE RECURSION, NEED TO PUT RETURN AND THEN CALL FUNCTION!!!!! 
        else: # target > mid: 
            list = list[mid+1:]
            return binary_search(list, target)
    return False 


list = [1, 3, 10, 11, 13, 30, 50, 100, 1000, 130593]
print(binary_search(list, 100))


'''
QUESTIONS: 
- 


LESSONS LEARNED: 
- To have recursion call, must return (RECURSIVE FUNCTION) 
- list is redefined in the conditions. size, left, right, mid are recalculated at the beginning of binary_search function 
- NEED TO RETURN IN BINARY_SEARCH BECAUSE WE WANT THE OUTPUT OF EACH CALL TO BE IN THE INPUT OF THE NEXT 


CODE IMPROVEMENT: 
- Rather than having a while True loop, have whenever left <= right, binary search happens only if the left index is less than the right or equal. Once it becomes 1 element
  there it returns False 
- 

'''
