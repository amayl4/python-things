arr = [12, 54, 76, 56, 34, 75, 98, 103, 451]

# return the index of any number in the array using linear search

target = int(input("Enter target number: \n")) # allowing user to select the target

for num in range(0, len(arr)):
    if arr[num] == target:
        print(num+1) # array indexing always gives the (n-1)th index so +1 returns the nth index
        break # stops the for loop from going on forever

# Time complexity: O(n)