def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


sum = 0
index = 1
while fib(index) < 4000000:
    # reduce testing for even values
    # easy to prove that every third fib number is even
    if index % 3 != 0:
        index += 1
        continue
    if fib(index) % 2 == 0:
        sum += fib(index)
    index += 1

print sum
