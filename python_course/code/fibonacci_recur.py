def fib_recur(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recur(n-1) + fib_recur(n-2)

def fib_runner(z):
    print(f"The {z}th number in the fibonacci sequence is {fib_recur(z)}")

z = 0
fib_runner(z)
z = 1
fib_runner(z)
z = 10
fib_runner(z)
