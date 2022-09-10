def partition(arr, low, high):
    pivot = arr[low]
    # low = start + 1
    # high = end
    while True:
        while low <= high and arr[low] <= pivot:
            low += 1
        while low <= high and arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[low], arr[high] = arr[high], arr[low]
    return high

def quick_sort(arr, start, end):
    if start>=end:
        return
    else:
        p = partition(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quick_sort(l,0,len(l)-1))
print(l)
