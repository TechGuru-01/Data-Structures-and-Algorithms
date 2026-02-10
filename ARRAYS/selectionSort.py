'''
What is Selection Sort?
- Selection Sort is a comparison-based sorting algorithm. 
- It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

How it works?
- Identify the minimum value in the array and exchange it with the element at the first index, placing it in its correct position.
- Next, locate the smallest element from the remaining unsorted portion and swap it with the element at the second index.
- This process is repeated, reducing the unsorted section each time, until all elements are arranged in their proper order.
'''

def selectionSort(arr):
    for i in range(len(arr)):# Iterate over each position in the array
        min = i# Assume the current index holds the smallest value
        for j in range(i+1,len(arr)):# Search the remaining unsorted elements
            if arr[j] > arr[min]:
                min = j# Update index of the smallest value found
        arr[i],arr[min] = arr[min],arr[i]#Swap
        count =i+1
        print(f"PASS {count}: {arr} ")
            

arr = [5,4,3,2,1]
selectionSort(arr)


