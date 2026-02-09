'''
What is Bubble Sort?
- Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 
- This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.

How it works?
- Sorts the array using multiple passes. After the first pass, the maximum goes to end (its correct position). 
  Same way, after second pass, the second largest goes to second last position and so on.
- In every pass, process only those that have already not moved to correct position.
  After k passes, the largest k must have been moved to the last k positions.
- In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element.
  If we keep doing this, we get the largest (among the remaining elements) at its correct position.
'''
def bubbleSort(arr):
  for i in range(len(arr)):#Traverse through the whole Array.
    for j in range(len(arr)-i -1):#-i is to lessen the range of comparisons after a full pass. 
      if arr[j] > arr[j+1]:#Compare the elements.
        arr[j], arr[j+1] = arr[j+1], arr[j]#Swap
    count = i+1
    print(f"PASS #{count}: {arr}")
    
arr = [5,4,3,2,1]
print(f"Sort this Array: {arr}")
bubbleSort(arr)

