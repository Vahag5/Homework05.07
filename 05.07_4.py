def binary_sr(ls:list, target:int):
    x = 0
    y = len(ls) - 1
   
    while x <= y:
        center = (x+y) // 2
        if ls[center] == target:
            return f'dzer uzac {target} tiv@ gtnvel a {center} indeqsov'
        elif target > ls[center]:
            x = center + 1
        else:
            y = center - 1

    return "Tiv@ bacakayum a listum"

ls1 = [1,5,6,8,9,4,2]
tiv = 5

print(binary_sr(ls1,tiv))
#dzer uzac 5 tiv@ gtnvel a 1 indeqsov
