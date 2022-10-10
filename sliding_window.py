# Martin Hoang 

'''
Sliding Window 
Purpose of this programing is learning how to implement the sliding window algorithm. Sliding window speeds up time complexity by reducing loops. Sliding window algo 
has a time complexity of O(n), one single loop  

PSEUDOCODE: 
1. define size, k (window size) 
2. size > k, else error because arr is too small 
3. create a loop in range (size - k) to prevent index exceed error. End of window must stop K elements before it 

NOTES: 
- 

'''
# list = [3, 5, 7, 1, 6] 
def sliding_window(list, k): 
    '''
    k = consecutive numbers within list 
    rtype = int(maxsSum) for k 
    '''

    size = len(list) 

    if k > size: 
        print('Error: window is larger than list size')

    # define initial window & sum 
    window = list[0:k]  
    max = sum(window) 

    for i in range(size - k + 1):  # k will be 2 in this example            i = 0, 1, 2, 3, 4  
        window = list[i:k+i]    # window shifting right by 1 
        sum_window = sum(window) 
        if sum_window > max: 
            max = sum_window    

    return max 

list = [3, 5, 7, 1, 6, 100, 33] 
print(sliding_window(list, 2)) 



'''
QUESTIONS: 
-


LESSONS LEARNED: 
- sliding window has faster time complexity than Brute Force approach by reducing number of loops 
- Sliding window is similar to a bus window and kids analogy 


CODE IMPROVEMENT: 
- Improved the program by moving the initial window and sum outside of the for loop. The for loop didn't need to recalculate window_0 everytime. Program only needs to calculate 
  window as i increments  

'''