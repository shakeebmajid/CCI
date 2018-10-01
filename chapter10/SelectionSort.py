def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        index = i
        for j in range(i, len(array)):
            if array[j] < min:
                index = j
                min = array[j]
        
        temp = array[i]
        array[i] = array[index]
        array[index] = temp


array = [2, 233, 2, 15, 19, 23, 12, 5, -38]

print "array before: ", array
selection_sort(array)
print "array after: ", array
