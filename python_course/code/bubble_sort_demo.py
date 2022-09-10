def bubble_sort(arr):
    # Create flag to track if a swap occurred in list traverval
    swap_tracker = True
    # loop over list traversal until you encounter a condition of no swap inside list traversal
    for j in range(len(arr)-1):
        swap_tracker = False
    # Traverse list till (total length - 1) as the last element would be compared along with the second last element.
        for i in range(len(arr)-1):
    # Compare consecutive indices and swap if smaller index has greater value than larger index. Set flag to True.
            if arr[i] > arr[i+1]:
                swap_tracker = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if not swap_tracker:
            break


# l = [6,8,1,4,10,7,8,9,3,2,5] # average case
# l = [10,9,8,8,7,6,5,4,3,2,1] # worst case
l = [1,2,3,4,5,6,7,8,8,9,10] # best case
bubble_sort(l)
