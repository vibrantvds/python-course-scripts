def insertion_sort(arr):
    # Define Key Index to perform sort
    comparisons = 0
    print(f"initial array: {arr}")
    for key in range(1,len(arr)):
        comparisons += 1
        current_key = key
        while (current_key != 0) and (arr[current_key] < arr[current_key-1]):
            comparisons += 1
            arr[current_key], arr[current_key-1] = arr[current_key-1], arr[current_key]
            # print(arr[current_key])
            current_key -= 1
        print(f"current array: {arr}, Iteration #{key}")
    print(comparisons)
    return arr

# l = [6,8,1,4,10,7,8,9,3,2,5] # average case
l = [10,9,8,8,7,6,5,4,3,2,1] # worst case
# l = [1,2,3,4,5,6,7,8,8,9,10] # best case
print(insertion_sort(l))
