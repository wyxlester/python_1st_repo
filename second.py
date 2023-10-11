# Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    # This line initializes two variables, a and b, with the values 0 and 1, respectively.
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        # a, b = b, a+b: After printing the current value of a, the values of a and b are updated. a is set to the current value of b,
        # and b is set to the sum of the old values of a and b. This is a common technique used to generate the next number in the Fibonacci sequence.
        # a becomes the previous Fibonacci number, and b becomes the next Fibonacci number in the sequence.
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
