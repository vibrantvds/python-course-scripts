def selction_sort(arr):
    # Create a variable to keep track of swap occurance in inner loop
    # Create a loop for marker index
    print(f"initial array: {arr}")
    comparisons = 0
    for marker in range(len(arr)-1):
        comparisons += 1
        # Iterate over elements after marker index (Every iteration shifts smallest element to marker index)
        for i in range(marker+1,len(arr)):
            comparisons += 1
            # Swap if LHS > RHS
            if arr[marker] > arr[i]:
                # print(i)
                arr[marker], arr[i] = arr[i], arr[marker]
    # Break out of main loop in case of no swaps in inner loop
        print(f"current array: {arr}, Iteration #{marker+1}")
    print(comparisons)
    pass

# l = [6,8,1,4,10,7,8,9,3,2,5] # average case
# l = [10,9,8,8,7,6,5,4,3,2,1] # worst case
l = [1,2,3,4,5,6,7,8,8,9,10] # best case
selction_sort(l)
