# Martin Hoang 

'''
TOPIC: Array & hashing 


PSEUDOCODE: 
1. 

BRUTE FORCE: 
1. 
- Time Complexity: 
- Space Complexity: 

OPTIMAL SOLUTION: 
2. Count each char and store in dictionary. Compare dictionaries 
- Time Complexity: O(s+t) > O(n)
- Space Complexity: O(s+t) > O(n) 

3. Can use collection.counter 

4. Can sort the string and compare 

'''
def isAnagram(s: str, t: str) -> bool:
        # solution 1 
        dict1, dict2 = {}, {} 
        for c in s: 
            dict1[c] = dict1.get(c, 0) + 1 
        for c in t: 
            dict2[c] = dict2.get(c, 0) + 1
        
        return dict1 == dict2 

        # solution 2 
        # return counter(s) == counter(t) 

        # solution 3 
        # return sort(s) == sort(t) 


print(isAnagram("anagram", "nagaram"))



'''
QUESTIONS: 
- How does the collection.counter module work? 
    - Can use python counter function to simply > return counter(s) == counter(t)
    - This works the same was as our multiple lines of code because its implemented using a hashmap 
- How to compare 2 strings if we don't want to use more memory? 
    - Can sort the string and then compare 
    - sorting gives Time complexity of O(nlogn), space of O(1) 


NOTES & LESSONS LEARNED: 
- No need to split the string using str.split. Can iterate the string using loop 
- Idea was correct, iterating through each string and count the number of char and updating the value in a dictionary. Then comparing the dictionary 
- DICT1 AND DICT2 HAVE DIFFERENT ORDER > BUT ASKING IF DICT1 == DICT2 COMPARES EACH ELEMENT > by doing this 

CODE IMPROVEMENT: 
- No need for if, dict1 == dict2, else return >>> simplify by using 1 line 
- can declare multiple variables on one line 
- Improve code by checking in beginning if len(s) == len(t) 
'''