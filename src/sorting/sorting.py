
def partition(data):
    pivot = data[0]
    left = []
    right = []

    for current in data[1:]:
        if current <= pivot:
            left.append(current)
        else:
            right.append(current)
    return left, right, pivot


def quicksort(data):
    if len(data) <= 1:
        return data
    left, right, pivot = partition(data)
    return quicksort(left)+[pivot]+quicksort(right)

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    while arrA or arrB:
        if not arrB or (arrA and arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    arrA, arrB = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
