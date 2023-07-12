def binary_sr(ls:list, target:int):
    x = 0
    y = len(ls) - 1
   
    while x <= y:
        center = (x+y) // 2
        if ls[center] == target:
            return center
        elif target > ls[center]:
            x = center + 1
        else:
            y = center - 1

    return -1

ls1 = [1,2,3,4,5,6,7,8,9,10,15,18]
tiv = 4
ret = binary_sr(ls1,tiv)
if ret == -1:
    print("Tiv@ bacakayum a listum")
else:
    print(f'dzer uzac {tiv} tiv@ gtnvel a {ret} indeqsov')


