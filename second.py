name = input("Hello, what is your name? ")
print(f"Hello, {name}")

# This line initializes two variables, a and b, with the values 0 and 1, respectively.
# These variables are used to keep track of the two most recent Fibonacci numbers.
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    # a, b = b, a+b: After printing the current value of a, the values of a and b are updated. a is set to the current value of b,
    # and b is set to the sum of the old values of a and b. This is a common technique used to generate the next number in the Fibonacci sequence.
    # a becomes the previous Fibonacci number, and b becomes the next Fibonacci number in the sequence.
    a, b = b, a+b
