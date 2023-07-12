def binary_search_recursive(array, target, low, high):
    
    if low > high :
        return -1
    mid = (low+high) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array,target,low,mid-1)
    else:
        return binary_search_recursive(array, target, mid + 1, high)


ls = [1,2,3,4,5,6,7,8,9,10,11,12,20]
tiv = 12
ret = binary_search_recursive(ls,tiv,0,len(ls)-1)
if ret == -1:
    print('dzer nshac tiv@ bacakayum a listum')
else:
    print(f'dzer nshac {tiv} tiv@ gtnvum a {ret}  indexi tak ')
    #dzer nshac 12 tiv@ gtnvum a 11  indexi tak 
     
