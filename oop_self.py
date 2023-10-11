# [OOP Concept] This line declares a new class named Point.
# In Python, a class is a blueprint for creating objects with specific attributes (data) and methods (functions).
class Point:
    # This is a special method called the constructor or initializer.
    # It is automatically called when you create a new instance of the class.
    # The self parameter refers to the instance of the class that is being created,
    # x and y are parameters that represent the initial values of the x and y attributes of the Point object.
    def __init__(self, x, y):
        # these lines assign the values of x and y (the parameters passed when creating an instance of the class) to the
        # instance variables self.x and self.y. These instance variables store the attributes of each Point object.
        self.x = x
        self.y = y

# Create two Point objects with different x and y coordinates and access their attributes to retrieve the values
# you assigned during object creation.
point1 = Point(3, 4)
point2 = Point(-1, 2)

# Accessing the attributes of the Point objects
print("Point 1: x =", point1.x, "y =", point1.y)
print("Point 2: x =", point2.x, "y =", point2.y)
