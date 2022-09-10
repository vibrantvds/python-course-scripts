from random import choice
from string import ascii_lowercase as letters
import time

def quicksort(arr):
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
        return quicksort(smaller) + equivalent + quicksort(larger)

def merge_sorted(arr1,arr2):
    i,j = 0,0 # 2 pointers
    sorted_arr = [] # result array
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    if i <len(arr1):
        sorted_arr.extend(arr1[i:])
    else:
        sorted_arr.extend(arr2[j:])
    return sorted_arr

def mergesort(arr):
    arrLength = len(arr)
    # Base condition - return array if there's only one element
    if arrLength < 2:
        return arr[:]
    else:
        middle = arrLength // 2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1,l2)

def bubblesort(arr):
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

def email_generator(username_length, count, domains):
    get_word = lambda x: "".join([choice(letters) for i in range(x)])
    return [f"{get_word(username_length)}@{choice(domains)}" for i in range(count)]

def analyze_func(func_name, *args):
    tic = time.time()
    result = func_name(*args)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")
    return result

def bisection_iter(n, arr):
    start, stop = 0, len(arr)-1
    while(start <= stop):
        mid = start + ((stop - start)//2) # To avoid running into cases where sum of 2 integers can't be stored correctly
        if n == arr[mid]:
            return mid, f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return None, f"{n} not found in list"
