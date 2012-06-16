"""def fib(n):
    if n==1 or n==0:
        return 1
    return fib(n-1)+fib(n-2)
"""
fibs = [1,2]
i = 1

while True:
    n = sum(fibs[-2:])
    if n>4000000:
        break
    fibs.append(n)
    i+=1

fibs = [f for f in fibs if f%2==0]

print n
print sum(fibs)
