
__version__ = "0.1"

def fib(n):
    """Extreme fib function"""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Extreme fib2 function"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return  result

if __name__ == "__main__":
    import sys
    mylen = len(sys.argv)
    help_message = "Provide additional command.\n-h for help.\n-v for version.\n-fib +n for fib(n).\n-fib2 +n for fib2(n).\n"
    if mylen == 1:
        print("{0}".format(help_message))
    if mylen == 1:
        if sys.argv[1] == "-v":
            print("Version: {0}".format(__version__))
        elif sys.argv[1] == "-h":
            print("{0}".format(help_message))
    elif mylen == 2:
        if sys.argv[1] == '-fib':
            print('{0}'.format(fib(sys.argv[2])))
        elif sys.argv[2] == '-fib2':
            print('{0}'.format(fib2(sys.argv[2])))
    else:
        print("{0}".format(help_message))



