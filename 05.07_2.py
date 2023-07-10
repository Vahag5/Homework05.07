def fibo(x):

    if not isinstance(x, int):
        raise TypeError("Invalid input. Expected an integer.")
    elif x < 1:
        raise ValueError("The Fibonacci series is not defined for negative numbers and 0")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x-2) + fibo(x-1)

try:
    print(fibo(10)) #34
    print(fibo(1))  #0
    print(fibo(2))  #1
    print(fibo(-5))  # The Fibonacci series is not defined for negative numbers and 0
except (ValueError,NameError,TypeError) as error:
    print(error)

try:
    print(fibo('notdigit'))
except (ValueError,NameError,TypeError) as error: #NameError@ grel em vortev kara anun gri cucich gri vor@ tiv chi
    print(error) #Invalid input. Expected an integer.
