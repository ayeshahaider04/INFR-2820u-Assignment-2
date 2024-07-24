# Assignment 2 
# Ayesha Haider 100869659

import time
import winsound
def MergeSort(arr, data=0):
    if len(arr) > 1:
        middle = len(arr) // 2  
        first_half = arr[:middle]  
        second_half = arr[middle:] 
        MergeSort(first_half, data + 1)  
        MergeSort(second_half, data + 1)  
        i = j = k = 0

        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1

        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1
            winsound.Beep(1000, 1000)

        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1
            
        print(" " * data * 2 + f"first half during sorting: {first_half}")
        print(" " * data * 2 + f"second half during sorting: {second_half}")
        print(" " * data * 2 + f"Merged array sorted in increasing order: {arr}")


def PrintArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == "__main__":
    ArrayInput = input("enter an array of integers with spaces in between each: ")
    arr = list(map(int, ArrayInput.split()))  
    
    print("inputed array was:")
    PrintArray(arr)
    
    MergeSort(arr)
