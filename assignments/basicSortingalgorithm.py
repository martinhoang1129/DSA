# Martin Hoang 
# CSC 252 - 8C1 
# Lab 5: Searching and Sorting with Time Complexity 
# Professor: Ivan 

import time 
import math 

# main function calling all other functions and calculates runtime 
def main(): 

    # convert all values and search input to str. So no error of str != int 
    # will assume int. if I want to sort char or number then I need another function or condition that checks if number or char 
    # split the input. Split returns list of strings. I need to apply list comprehension to convert to int 
    list = [int(x) for x in input('\nPlease enter numbers: ').split()]
    print(list) 

    # user selects sorting or search algorithm 
    SelectRoutine(list)
    

# menu selector
select = 0

def DisplayMenu() :
    print ("\nenter your choice")
    print ("1 for a Linear Search")
    print ("2 for a Binary Search")
    print ("3 for a Bubble Sort")
    print ("4 for a Selection Sort")
    print ("5 for a Insertion Sort")



def SelectRoutine(arr) :
    global select

    DisplayMenu()
    select = int(input())
    if (select == 1):
        print ("\nCall the Linear Search Routine")
        linearSearch(arr)
    elif (select == 2):
        print ("\nCall the Binary Search Routine")
        binarySearch(arr) 
    elif (select == 3): 
        print('\nCall for Bubble Sort') 
        bubbleSort(arr)
    elif (select == 4): 
        print('\nCall for Selection Sort') 
        selectionSort(arr)
    elif (select == 5): 
        print('\nCall for Insertion Sort') 
        insertionSort(arr)
    else :
        print("\ninvalid selection")



def linearSearch(arr): 
    x = int(input('Enter a number to search: ')) 

    found = False 

    for i in range(len(arr)): 
        if x == arr[i]: 
            found = True 
            print('{} is found in {} position'.format(x, i))
            exit 
        if found == False and i == len(arr)-1:  
            print('{} is not found'.format(x)) 



def binarySearch(arr): 
    search = int(input('Enter a number to search: '))

    sorted = int(input('Is the list sorted? (1 for True, 2 for False): '))

    if sorted == 2: 
        print('Cannot perform binarySearch on unsorted list! Please sort the list first then perform binarySearch!')
        exit() 
    
    left = 0 
    right = len(arr) - 1 

    # cut right half 
    while left <= right: 
        mid = (left + right) // 2
        if search == arr[mid]: 
            print('{} is found at {}'.format(search, mid))
            exit() 
        elif search < arr[mid]: 
            right = mid - 1
        else: # search > middle number 
            left = mid + 1
    
        # binary search whole list and number not found 
    print('{} is not found within the list '.format(search)) 



def selectionSort(arr):
    # traverse list and compare 1st number to next numbers > 2 loops 
    # Assume first number is min. If found newMin > get index 
    # swap at the end 

    
    for i in range(len(arr)-1): 
        iMin = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[iMin]:
                iMin = j 
        arr[i], arr[iMin] = arr[iMin], arr[i] 

    print(arr) 

    # i is already incrementing. No need to do i++ 
    # iMin goes betwen the loop. We are assuming iMin is the smallest one at the start of outer loop. iMin isn't 0 on the outside 


def insertionSort(arr): 
    # left arr is sorted, right side unsorted > compare current item to item on the left 
    # traverse list. Take current index and compare to left index, the one before 
    # swaps when current number is less than previous number before
    # _ _ _ _ 

    for i in range(len(arr)-1):  # outer loop stops at len(arr)-1 because inner loop looks at the next number and decrements 
        for j in range(i+1,0,-1): 
            if arr[j] < arr[j-1]:   # if current number is smalller than previous number, switch 
                arr[j-1], arr[j] = arr[j], arr[j-1]
    
    print(arr) 

    



def bubbleSort(arr): 
    # right side are sorted  
    # traverse list and compares 2 numbers at a time. It keeps swapping the 2 numbers. Both index moves at the same time 
    
    # 5 3 2 1   i = 0
    # 3 5 2 1 
    # 3 2 5 1 
    # 3 2 1 5 

    # 2 3 1 5   i = 1
    # 2 1 3 5 

    for i in range(len(arr)): 
        # last i element in place on first pass 
        for j in range(len(arr)-i-1): # each time i increments, that's the number of sorted variables we have  
            # need to subtract 1 as well. If we do not subtract 1 on the first pass when i = 0, there's an indexing error 
            if arr[j] > arr[j+1]: 
                arr[j+1], arr[j] = arr[j], arr[j+1] 

    print(arr) 

main() 