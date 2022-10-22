# Martin Hoang 

'''
2 pointer Algorithm
The purpose of this program is applying the 2 pointer algo to a sorted array to find the 2 numbers summing the target 

PSUEDOCODE 
1. list must be sorted 
2. Create a while loop that breaks when number is found or not found 
    i. once the left pointer passes the right pointer then there is no solution 
3. Move pointers by comparing sum to target: 
    i. if sum > target: move right pointer left 
    ii. if sum < target: move left pointer right 
    iii. left and right can fall on the same number, so need to check this case 
    iv. edge cases: 
        a. target equals smallest number or smaller than left number 
        b. target equals largest number or larger than right most number 
'''

def two_pointer(list, target): 
    # can check if sorted by creating a function def is_sorted(list)
    # if not sorted, then can apply sorting algorithm beforehand
    size = len(list) 
    i = 0 
    j = size - 1 
    left = list[i] 
    right = list[j]

    while i < j:
        sum = left + right 
        # exits when sum == target
        if sum == target: 
            print('index: {},{}. numbers {}, {}'.format(i, j, list[i], list[j]))
            return True
        # moves right pointer left 
        elif sum > target: 
            j -= 1 
            right = list[j]
        # moves left pointer right 
        else: 
            i += 1 
            left = list[i]
    print('no solution') 
    return False 


list1 = [5, 12, 8, 11, 7, 4, 3, 5, 5, 3, 2, 1] 
list1.sort() 
two_pointer(list1, 14) 

list2 = [5, 12, 16, 10, 11, 7, 4, 3, 5, 5, 3, 1, 2, 1]
list2.sort()
two_pointer(list2, 18)

list3 = [5, 12, 8, 10, 7, 4, 3, 5, 5, 3, 2, 1]
list3.sort()
two_pointer(list3, 11)

list4 = [5, 12, 8, 10, 7, 4, 3, 5, 5, 3, 2, 1]
list4.sort() 
two_pointer(list4, 1) 


'''
LESSONS LEARNED: 
- 2 pointer algorithm only works on sorted list 
- Algo works by having a while loop and then moving the left and right pointers based on conditions 
- Can improve this program by checking if the list is sorted at the beginning of two_pointer function 


CODE IMPROVEMENT: 
- program can be improved while setting while i < j. When i == j, it still runs and doesn't break. Moment i > j, there's no solution 
- Only need to check if sum == target. 
'''