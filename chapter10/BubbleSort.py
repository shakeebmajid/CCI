def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) - (i + 1)):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array = [5, 9, 2, 1, 3, 23, 5, 19]
print "array before: ", array 
bubble_sort(array)
print "array after: ", array
