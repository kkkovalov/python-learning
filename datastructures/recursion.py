def factorial(n):
    if ( n < 1 ):
        return 1
    else:
        return n*factorial(n-1)
    
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n, 1, 1, 2)
    
def fib(n, prev, cur, count):
    if n == count:
        return cur
    else:
        temp = cur
        cur += prev
        prev = temp
        count+=1
        return fib(n,prev, cur, count)

print(fibonacci(16))