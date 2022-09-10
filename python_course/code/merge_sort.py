def merge_sort(arr):
    arrLength = len(arr)
# Base condition - return array if there's only one element
    if arrLength < 2:
        return arr[:]
    else:
        middle = arrLength // 2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1,l2)


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

###### Program Execution ######
l1 = [1,4,6,8,10]
l2 = [2,3,5,7,8,9]
l = [6,8,1,4,10,7,100,-4,8,9,3,2,5]
print(f"Merged list: {merge_sort(l)}")

# Steps for Merging sub-problem
# 1. Compare first element in each list and append smaller element
# 2. Using a index and an iterator perform same comparisons
#     for all elements in both lists
# 3. Move marker up by 1 position after smaller number is found
# 4. Copy remaining list once comparisons are complete and there
#     are items still remaining in one of the lists

# Steps for splitting into sub-problem
# 1. Get middle element of array
# 2. Divide array in the middle(left/right)
# 3. Return array if there's only one element left, else divide further
