def quick_sort(arr):
    # Base Condition
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1] # Selecting last element as pivot
        smaller, equivalent, larger = [], [], [] ## TODO: Do this with less space complexity
        for i in range(len(arr)):
            if arr[i] < pivot:
                smaller.append(arr[i])
            elif arr[i] == pivot:
                equivalent.append(arr[i])
            else:
                larger.append(arr[i])
        return quick_sort(smaller) + equivalent + quick_sort(larger)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quick_sort(l))
