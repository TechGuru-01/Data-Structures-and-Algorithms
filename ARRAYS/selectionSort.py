'''
What is Selection Sort?
- Selection Sort is a comparison-based sorting algorithm. 
- It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

- Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
- Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
- We keep doing this until we get all elements moved to correct position.
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


