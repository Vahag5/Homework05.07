def selection_sort(arr:list):
    sorted_array = []
    x = len(arr)
    for i in range(x):
        index = i
        for j in range(i, x):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr






ls = [1,2,3,4,80,10,45,78,16,45]
print(selection_sort(ls))  # [1, 2, 3, 4, 10, 16, 45, 45, 78, 80]
