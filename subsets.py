#Problem: Find m subsets of an array of size n

print("Enter array")

def find_m_sized_subsets(arr, m):
    """
    Finds all subsets of size m from the array arr.
    """
    subsets = []
    n = len(arr)
    
    # Helper function for backtracking
    def backtrack(start_index, current_subset):
        # Base Case: If the current subset is of size m, add it to results
        if len(current_subset) == m:
            subsets.append(current_subset[:]) # Use [:] to append a copy
            return

        # Iterate through the array starting from start_index
        for i in range(start_index, n):
            # Include the element at index i
            current_subset.append(arr[i])
            
            # Move to the next element
            backtrack(i + 1, current_subset)
            
            # Backtrack: Remove the last element to try the next one
            current_subset.pop()

    backtrack(0, [])
    return subsets

# --- Driver Code ---
array = [9,4,1,7]
m = 2

result = find_m_sized_subsets(array, m)

print(f"All subsets of size {m} from {array}:")
for subset in result:
    print(subset)