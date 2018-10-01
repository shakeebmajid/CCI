def merge(array, helper, low, middle, high):
    for i in range(low, high + 1):
        helper[i] = array[i]

    helper_left = low
    helper_right = middle + 1
    current = low

    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            array[current] = helper[helper_left]
            helper_left += 1
        else:
            array[current] = helper[helper_right]
            helper_right += 1

        current += 1

    remaining = middle - helper_left
    for i in range(remaining + 1):
        array[current + i] = helper[helper_left + i]

def merge_sort_helper(array, helper, low, high):
    if low < high:
        middle = (low + high) / 2
        merge_sort_helper(array, helper, low, middle)
        merge_sort_helper(array, helper, middle + 1, high)
        merge(array, helper, low, middle, high)

def merge_sort(array):
    helper = [array[i] for i in range(len(array))]
    merge_sort_helper(array, helper, 0, len(array) - 1)

array = [5, 29, 2, 3, 15, 19, -323, 1500]

print "array before: ", array
merge_sort(array)
print "array after: ", array
