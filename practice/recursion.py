# Martin Hoang 

'''
Recursion
The objective of this program is to understand recursion, which is defined as defining something in terms of itself. Examples are fibonacci number, calculating combinations/permutations


PSEUDOCODE: 
1. 

NOTES: 
- 

'''

# RECURSION TO COUNT NUMBER OF ELEMENTS IN A NESTED LIST? 
NAMES = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann', 'Martin', 'Brandon', 'JP']
COUNT = 0
def count_ele_list(list_names): 
    ''' 
    Using isinstance() method to tell if element is a list 
    '''
    global COUNT 
    for item in list_names: 
        if isinstance(item, list):      # if item is a list > 
            count_ele_list(item) 
        else:                           # base case when item isn't a list 
            COUNT += 1 
    return COUNT
print('COUNT ELEMENTS IN NESTED LIST')
print(count_ele_list(NAMES))

# FIBONACCI NUMBER 
def fibonacci(index): 
    '''
    input: int(index of fibo number) 
    rtype: int(fibo number at index) 
    fibo: defined as the current number is the sum of the previous 2 numbers before it 
    '''

    # recursive method 
    # base case: fibo(0), fibo(1), fibo(2) 
    if index == 0: 
        return 0 
    elif index == 1 or index == 2: 
        return 1 
    else: 
        return fibonacci(index-1) + fibonacci(index-2)  # defining this as fibo(i). No need to set fibo(i) = .... > same as returning (a + b) as C 
                                                        # using return because need the previous results to be stored in the stack to be called. If want fibo(5), it saves fibo(4), fibo(3) + etc.. 

print('FIBONACCI')                                           
print(fibonacci(5))
print(fibonacci(30))
print(fibonacci(1))


# FACTORIAL 
def fact(num): 
    if num == 1: 
        return 1
    else: 
        return num * fact(num-1) 
print('FACTORIAL')
print(fact(4))



'''
QUESTIONS: 
- When to use return or not with a method/function? 
    - use return and the method when we want the method B to return a value to method A
    - in this case we want to update the global var, COUNT. If we were to return count_ele_list(item), count would be overriden
    - HERE NO NEED TO USE RETURN (METHOD) BECAUSE WE DO NOT NEED TO RETURN ANY VALUE. GLOBAL VAR COUNT NEEDS TO BE UPDATED BUT NOT RETURNED EVERYTIME 

- For fibonacci, if I want to return a list, overall, what needs to be returned in each fibo recursive call? 
    - define base cases: fibo(0), fibo(1), fibo(2) 
    - define returned recursive call: fibo(i) = fibo(i-1) + fibo(i-2) 
    
LESSONS LEARNED: 
- Only use global var if needed throughout program because it wastes memory. its stored in the beginning of the stack and doesn't delete until power is off 


CODE IMPROVEMENT: 
- 

'''