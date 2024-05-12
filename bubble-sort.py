# Sort numbers in ascending order w/ bubble sort

arr = [12, 54, 76, 56, 34, 75, 98, 103, 451]
n = len(arr)

for i in range(n):
    for j in range(n-1):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Sorted list is:\n", arr)

# Time complexity: O(n^2)