# Encapsulation
# Encapsulate the properties inside the class
# in other languages we have keywords public, private, protected
# to protect the properties
class circle:

    def __init__(self, radius):
        # change the property with single underscore
        # this makes the property private
        self.__radius = 0
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # getter method and setter method
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")

    # property is a class 
    # We are calling/invoking the class by passing the method as argument
    # Please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to 
    # a variable radius
    # in other words radius is an instance of property class
    radius = property(getRadius, setRadius)

    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius

    def __str__(self):
        return f"Radius of this cricle is {self.__radius}"

mycircle = circle(20)
print(mycircle)
# mycircle.__radius = 30

# you are indirectly passing the value 30 to the setter method
mycircle.radius = 30
print(mycircle)

print(mycircle.area())

# you are indirectly passing the value "abc" to the setter method
mycircle.radius = "abc"
print(mycircle)
# mycircle = circle("abc")
#vprint(mycircle)
