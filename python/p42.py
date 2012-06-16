import sys
print sys.argv
sys.command("touch monkey")


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n-1)+fib(n-2)

print fib(int(sys.argv[1]))
