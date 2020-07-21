# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Iterative
    # start_index = start
    # end_index = end

    # while start_index <= end_index:
    #     middle_index = (start_index+end_index)//2
    #     middle_value = arr[middle_index]
    #     if middle_value == target:
    #         return middle_index
    #     elif target < middle_value:
    #         end_index = middle_index - 1
    #     else:
    #         start_index = middle_index + 1
    # return -1
    if start > end:
        return -1
    else:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    pass
