# Martin Hoang 

'''
TOPIC: Array & Hashing 


PSEUDOCODE: 
1. 

BRUTE FORCE: 
1. Brute force method would be to have a nested loop to compare 2 numbers 
- Time Complexity: O(n^2) 
- Space Complexity: O(1) 

OPTIMAL SOLUTION:
2. Can sort the list and then compare the numbers next to each other 
- Time Complexity: 
- Space Complexity: 

3. Use a set, which is essentially a special type of hashmap. add each value to the set. If another value appears, then return false. Only need to traverse list once  
- Time Complexity: O(n). Traverse list to see if there are duplicates 
- Space Complexity: O(n). Making a new variable while traversing list 

'''
nums = [1,2,3,1]

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set() 
        for number in nums: 
            if number not in distinct: 
                distinct.add(number)
            else:
                return False 
        return True  


'''
QUESTIONS: 
- What is the time complexity of sorting and then searching for the sub-optimal solution? Sorting using quicksort/mergesort takes O(nlogn) and then searching by 
  iterating through the array is needed which is O(n) 


NOTES & LESSONS LEARNED: 
- A set is implemented using a hashmap, similar to a dictionary 
- sets have O(1) insertion and deletion 


CODE IMPROVEMENT: 
- 

'''