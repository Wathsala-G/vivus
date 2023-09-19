"""
Basic Software Design Principles are:

KISS ("keep it simple stupid")
The principle of keeping things simple is crucial, especially in programming. 
It implies that you must strive to achieve simplicity in code design and implementation. 
To illustrate, let's take the example of writing a function to calculate the area of a Circle

||** Open/Closed principle **||
Write extensible code; add new functionality without changing existing code

||**DRY (don't repeat yourself**||
This principle emphasizes the importance of code reuse to avoid duplication of code, data, and logic.

||**Composition > inheritance**||
Use composition, not inheritance. Combine small modular objects for code, instead of complex inheritance hierarchy.

"""
# DRY principle helps to save time while avoiding to have creat same code repeatedly for a same result.
# Define below the class 'Circle' and its methods with proper explain by code.
# DRY principle helps to save time while avoiding to have creat same code repedatedly for a same result.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Area: # Define the area functionality below
    def run(self):
        circle = Circle(5)
        circle_area = Circle.area(circle)
        print(circle_area)

area= Area()
area.run()
# below is a example of not using DRY pricple, if you want area of 20 circles you can use DRY princple and get the result at once intead having to write 20 lines. 
circle1= 3.14159 * 3 ** 2
print(circle1)
circle2= 3.14159 * 5 ** 2
print(circle2)
        

        
