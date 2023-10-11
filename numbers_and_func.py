# This line initializes two variables, a and b, with the values 0 and 1, respectively.
# These variables are used to keep track of the two most recent Fibonacci numbers.
a, b = 0, 1
while a < 1000:
    # print(a, end=',')
    # a, b = b, a+b: After printing the current value of a, the values of a and b are updated. a is set to the current value of b,
    # and b is set to the sum of the old values of a and b. This is a common technique used to generate the next number in the Fibonacci sequence.
    # a becomes the previous Fibonacci number, and b becomes the next Fibonacci number in the sequence.
    a, b = b, a+b

# Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
# fib(2000)

my_list = ["eat", "sleep", "repeat"]
word = "geek"

# creating enumerate objects
obj1 = enumerate(my_list)
obj2 = enumerate(word)

print ("Return type:", type(obj1))
print (list(enumerate(my_list)))
print (list(enumerate(word)))

# changing start index to 2 from 0
print (list(enumerate(word, 2)))
