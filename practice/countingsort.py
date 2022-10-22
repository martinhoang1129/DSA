# Martin Hoang 

'''
Counting Sort 
The purpose of this program is applying counting sort to an unsorted list. Counting sort has a time complexity of O(n), similar to bucket sort or radix sort

PSUEDOCODE: 
1. Find range by finding maximum and minimum number. Get size of array too 
2. Create count array and find the total count of each element 
3. Create sumCount array (index) 
4. Create output array by using the sumCount and original arr 


NOTES: 
- The tricky part is making the output array because of the indexing
'''

list = [6, 5, 10, 3, 2, 5]

def countingSort(list): 
    '''
    input: unsorted list 
    rtype: sorted list 
    '''

    maximum = max(list) 
    minimum = min(list) 
    size = len(list) 
    range_num = maximum - minimum + 1 # range is inclusive of both ends of number 

    # count array 
    # arr originally 0, then add 1 at the correct location number
    # To add at correct index, subtract by minimum. 2 is at index 0 and 10 is at index 8 
    count_arr = [0] * range_num 
    for num in list: 
        index = num - minimum 
        count_arr[index] += 1 

    # sumCount array 
    # summinimumg the count_arr to give the index for each number count 
    sum_arr = [0] * range_num
    sum = 0
    for i in range(len(count_arr)): 
        sum += count_arr[i] 
        sum_arr[i] = sum 

    # sorted list 
    # trick: list > sum_arr > sorted
    # To move from lit > sum, subtract minimum and then -1 because I added 1 to the range   
    # decrement sum_arr whenever placed in output . If we do not decrease the sum_arr, then there will be a collision 
    sorted_list = [0]*size 
    for i in range(len(list)-1, -1, -1): 
        sorted_list[sum_arr[list[i] - minimum] -1] = list[i] 
        sum_arr[list[i] - minimum] -= 1 
    
    return sorted_list

print(countingSort(list))


'''
QUESTIONS: 
- why does sum_arr decrease by 1 after placing element in sorted_list?
    - Must decrease element by 1 or else there will be a collision. In this case there are 2 fives in the list. If we do not decrement by 1, there will only be 1 5 in the sorted list 
      because one 5 will replace the other at the same output index 
- What is the trick to building the sorted array, step 3? 
    - It uses a combination of list, sum_arr, and minimum
    - sorted_list[sum_arr[list[i]-min]-1] = list[i]  

LESSONS LEARNED:
- countingSort has 4 steps
    - find min, max, size, range 
    - count_arr: count occurrences of each element. Count_arr is size range b/c representing all range of numbers 
    - sum_arr: Sums each previous value to calculate the index for sorted_list
    - sorted_list: uses list, sum_arr, min, -1 to make the sorted list 

CODE IMPROVEMENT:
-

'''