'''
What is Insertion Sort?
- Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array one element at a time.
- It works by taking each element and inserting it into its correct position within the already sorted part of the array.
- This algorithm is efficient for small datasets or nearly sorted lists but becomes slower for large datasets.

How it works?
- The algorithm starts by assuming the first element is already sorted.
  It then selects the next element and compares it with the elements before it.
  
- During each step, the selected element (key) is compared with elements in the sorted portion of the array.
  All elements larger than the key are shifted one position to the right to make space.

- This process continues until the key is placed in its correct position.
  With each pass, the sorted portion of the array grows until the entire list is sorted.

'''
def insertionSort(arr):
    for i in range(len(arr)):# Traverse the Array.
        key = arr[i]# Get the key.
        j = i-1# Initialize the pointer to the element immediately on the left.
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j] # Shift to the right if the condition is satisfied
            j -= 1 # Move left to check the next element
        arr[j+1] = key# insert the key in its correct position
        print(f"{arr}")

arr = [5,4,3,2,1]        
insertionSort(arr)
