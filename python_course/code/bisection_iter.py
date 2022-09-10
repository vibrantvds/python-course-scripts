def bisection_iter(n, arr):
    start, stop = 0, len(arr)-1
    while(start <= stop):
        mid = start + ((stop - start)//2) # To avoid running into cases where sum of 2 integers can't be stored correctly
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return f"{n} not found in list"

def create_list(max_val):
    return [num for num in range(1, max_val+1)]

l = create_list(20)
for num in range(16):
    print(bisection_iter(num, l))
