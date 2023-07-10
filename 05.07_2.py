def fibo(x):
    if x < 1:
        raise ValueError("The Fibonacci series is not defined for negative numbers and 0")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x-2) + fibo(x-1)

try:
    print(fibo(10)) #34
    print(fibo(2))  # Output: 1
    print(fibo(1))  # Output: 0
    print(fibo(-7))  # The Fibonacci series is not defined for negative numbers and 0
except ValueError as error:
    print(error)