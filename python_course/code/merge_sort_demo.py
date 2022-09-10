def merge_sorted(arr1,arr2):
    # print("Merge function called with lists below:")
    # print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while (i<len(arr1)) and (j<len(arr2)):
        # print(f"Left list index i is {i} and has value: {arr1[i]}")
        # print(f"Right list index j is {j} and has value: {arr2[j]}")
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while j<len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    while i<len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    return sorted_arr

def divide_arr(arr):
    if len(arr) < 2:
        # print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        # print("Current list to work with:", arr)
        # print("Left split:", arr[:middle])
        # print("Right split:", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        # implied return encounter
        return merge_sorted(l1,l2)

# xxxxxxxx Program Execution xxxxxxxx
# l1 = [1,4,6,8,10]
# l2 = [] #[2,3,5,7,8,9]
# print(f"Merged list: {merge_sorted(l1, l2)}")
l = [6,8,1,4,10,7,8,9,3,2,5]
# l = [8,6,2,5]
print(divide_arr(l))

# Steps
# 1. Compare first element in each list and append smaller elements
# 2. Using indices and iterator perform same operation for all elements in both lists
# 3. Move marker up by 1 position after smaller number is found.
# 4. Copy remaining list once comparisons are complete and there are items still remaining in one of the lists
