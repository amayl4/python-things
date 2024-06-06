# Sort numbers in ascending order w/ bubble sort

arr = [12, 54, 76, 56, 34, 75, 98, 103, 451]
n = len(arr)

for i in range(n): # loop through the array once
    for j in range(n-1): # loop through the array again
        if arr[i] < arr[j]: # compare the 2 values
            arr[i], arr[j] = arr[j], arr[i] # make the actual swaps

print("Sorted list is:\n", arr)

# Time complexity: O(n^2)