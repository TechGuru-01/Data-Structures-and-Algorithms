# Compilation of the Sorting Algorithms.
class Sort:
    def __init__(self,arr):# arr as the input parameter.
        self.arr = arr
        self.swapped = False# Flag swaps.
    
    def bubbleSort(self):
        print("\nThis is Bubble Sort:")
        for i in range(len(self.arr)):
            self.swapped = False
            for j in range(len(self.arr)-i -1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    self.swapped = True
            if self.swapped:
                print(f"Pass #{i+1}: {self.arr}")
            else:
                break
            
    def selectionSort(self):
        print("\nThis is Selction Sort:")
        for i in range(len(self.arr)):
            min_idx = i
            self.swapped = False
            for j in range(i+1,len(self.arr)):
                if self.arr[j] > self.arr[min_idx]:
                    min_idx = j
                self.arr[min_idx], self.arr[j] = self.arr[j], self.arr[min_idx]
                self.swapped = True
            if self.swapped:
                print(f"Pass #{i+1}: {self.arr}")
            else:
                break
            
    def insertionSort(self):
        print("\nThis Insertion Sort:")
        for i in range(len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j >=0 and self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
                j-=1
            self.arr[j+1] = key
            print(f"Pass #{i+1}: {self.arr}")
            
arr = [5,4,3,2,1] 
print(f"Sort this Array: {arr}")   
s = Sort(arr.copy())
s.bubbleSort()
s = Sort(arr.copy())
s.selectionSort()
s = Sort(arr.copy())
s.insertionSort()