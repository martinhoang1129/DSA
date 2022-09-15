# Martin Hoang
# 8/31/22
# CSC 255
# Professor: Kamilla
# LAB 1

# OBJECTIVE: to sort a given array using heapsort/heapify. Once the arr is sorted, we can apply the search algorithm to find the sum of 2 = target in O(n)

import math

def heapsort(arr):
    # create heap 
    n = len(arr)  # number of times to loop for completed tree
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i)

    # swaps root and last element in heap
    for i in range(n-1, 0, -1): # only need n-1 loops because swapping. At n = 1, the arr is sorted
        arr[i], arr[0] = arr[0], arr[i]

        # heapify to sort tree starting from root > creates heap again
        heapify(arr, i, 0)

    return arr

# heapify sorts node and creates heap. Parent node value > child node value
def heapify(arr, n, i):
    max = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[max] < arr[left]:
        arr[i], arr[left] = arr[left], arr[i]
        heapify(arr, n, left) 
    if right < n and arr[max] < arr[right]:
        arr[i], arr[right] = arr[right], arr[i]
        heapify(arr, n, right)


# arr = [1, 4, 10, 8, 7, 3, 15, 100, 33, 9]

# sorted = heapsort(arr)
# print(sorted)

# APPLY 2 POINTER ALGORITHM TO SORTED ARRAY
# 2 pointer algo only works for sorted array 

def twoPointerAlgo(sorted, target): 
    n = len(sorted)
    left = 0 
    right = n - 1  
    p1 = sorted[left] 
    p2 = sorted[right] 
    for i in range(n): 
        if left > right:
            result = 'No'
            return result, p1, p2 
        elif left == right and p1 + p2 == target: 
            result = 'Yes' 
            return result, p1, p2 
        # THERE ARE 2 EDGE CASES. If target is super small or super large 
        elif left == right and p1 + p2 != target: 
            result = 'No'
            return result, p1, p2
        elif p1 + p2 > target: 
            right -= 1
            p2 = sorted[right] 
        elif p1 + p2 < target: 
            left += 1
            p1 = sorted[left] 
        elif p1 + p2 == target:    
            result = 'Yes' 
            return result, p1, p2 
        



for i in range(1,6):
    # reading file and getting unsorted list, target 
    with open('in' + str(i) + '.txt', 'r') as file: 
        line = file.readlines()
        str_list = line[2].rstrip(' \n').split(' ')
        list = [int(i) for i in str_list]
        target = int(line[1].rstrip('\n'))
        with open('out' + str(i) + '.txt', 'w') as f: 
            f.write(str(target)) 
            f.write('\nBefore heap sort')
            f.write('\nSumOfK\n')
            for num in list: 
                f.write(str(num) + ' ')

            # sorted list 
            f.write('\nApplying Heapsort with a time complexity of O(nlog(n))\n')
            sorted = heapsort(list)
            for num in sorted: 
                f.write(str(num) + ' ')
            f.write('\nApplying 2 pointer algorithm with a time complexity of O(n)\n')
            
        # applying 2 pointer algorithm 
            result = twoPointerAlgo(sorted, target)
            # print(result[0], result[1], result[2])
            if result[0] == 'Yes': 
                f.write(result[0] + '\n') 
                f.write('{}+{}={}'.format(result[1], result[2], target))
            else: 
                f.write(result[0])


    

        
