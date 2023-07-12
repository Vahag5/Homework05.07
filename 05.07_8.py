def insertion_sort(arr:list):
    x = len(arr)
    for i in range(x):
        elem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > elem:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr





arr = [1,4,5,8,23,78,45,68,49,13]
print(insertion_sort(arr)) #[1, 4, 5, 8, 13, 23, 45, 49, 68, 78] 
