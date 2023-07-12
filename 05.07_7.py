def bubble_sort(array: list):
    x = len(array)
    for i in range(x-1):
        if array[i] > array[i + 1] :
            array[i],array[i + 1] = array[i + 1],array[i]
            bubble_sort(array)

    return array


ls = [1,5,6,7,4,2,9,10,78,4890,100]
sorted_array = bubble_sort(ls)
print(sorted_array)  #[1, 2, 4, 5, 6, 7, 9, 10, 78, 100, 4890]