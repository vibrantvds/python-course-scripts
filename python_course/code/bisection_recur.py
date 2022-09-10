def bisection_recur(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in list"
    else:
        mid = start + (stop-start)//2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            return bisection_recur(n,arr,mid+1,stop)
        else:
            return bisection_recur(n,arr,start,mid-1)

def create_list(max_val):
    return [num for num in range(1,max_val)]

l = [1,2,3,4,5,6,7,8,9,10]
for num in range(16):
    print(bisection_recur(num,l,0,len(l)-1))
