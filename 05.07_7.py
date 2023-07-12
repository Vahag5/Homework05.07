def bubble_sort(array, reverse=False):
    x = len(array)
    for i in range(x-1):
        for j in range(x-i-1):
            if reverse:
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            else:
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
    return array

ls = [1, 5, 6, 7, 4, 2, 9, 10, 78, 4890, 100]
sorted_array = bubble_sort(ls)
print(sorted_array)  # [1, 2, 4, 5, 6, 7, 9, 10, 78, 100, 4890]

sorted_array2 = bubble_sort(ls, reverse=True)
print(sorted_array2)  # [4890, 100, 78, 10, 9, 7, 6, 5, 4, 2, 1]
