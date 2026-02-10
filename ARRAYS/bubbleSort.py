'''
What is Bubble Sort?
- Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping neighboring or adjacent elements if they are in the wrong order. 
- This algorithm is not efficient for large datasets as its average and worst-case time complexity are quite high.

How it works?
- The algorithm sorts the list through repeated passes. After the first pass, the largest value settles at the final index. 
 Each subsequent pass places the next largest value into its proper position from the end.

- During each pass, only the elements that are not yet in their correct positions are processed. 
 After completing k passes, the k largest elements will already be fixed in the last k positions of the array.

- In every pass, the remaining elements are scanned by comparing neighboring values and swapping them whenever a larger value appears before a smaller one. 
 Repeating this process ensures that the largest element in the unsorted portion moves to its correct position.
'''
def bubbleSort(arr):
  for i in range(len(arr)):#Traverse through the whole Array.
    swapped = False
    for j in range(len(arr)-i -1):#-i is to lessen the range of comparisons after a full pass. 
      if arr[j] > arr[j+1]:#Compare the elements.
        arr[j], arr[j+1] = arr[j+1], arr[j]#Swap
        swapped = True
    count = i+1
    if swapped:
      print(f"PASS #{count}: {arr}")
    else:
      break
    
arr = [5,4,3,2,1]
print(f"Sort this Array: {arr}")
bubbleSort(arr)

