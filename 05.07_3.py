def sdigits(x):
    if not isinstance(x, int):
        raise TypeError("Please enter an integer.")
    elif x < 0:
        raise ValueError("Please enter a non-negative integer.")
    elif x < 10:
        return x
    else:
        return x % 10 + sdigits(x // 10)
 
        
try:
    print(sdigits(456))           #15
    print(sdigits(777))           #21
    print(sdigits(1000000000))    #1
    print(sdigits("nodigit"))     #Please enter an integer.
except (TypeError,ValueError,NameError) as error:
    print(error)


