factorial_cache = {}
def fact(x):
    if x in factorial_cache:
        return factorial_cache[x]
    elif x == 0:
        return 1
    elif x < 0:
        raise ValueError("For negative numbers can't have factorial.")
    else: 
        result = fact(x-1) * x
        factorial_cache[x] = result
        
        return result


print(fact(0)) #1
print(fact(5)) #120
print(fact(15))#1307674368000
print(fact(-2))#ValueError: For negative numbers can't have factorial.