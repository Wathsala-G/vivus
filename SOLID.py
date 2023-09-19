"""
SOLID principles are the building blocks of the Class design

SRP - Single-Responsibility Principle / OCP - The Open-Closed Principle / LSP - Liskov Substitution Principle / ISP - Interface Segregation Principle / DIP - Dependency inversion Principle

SOLID is a set of principles for object-oriented design that promotes maintainable, flexible, and scalable code.

"""

# SOLID: 
# Single Responsibility Principle (SRP):
# Each class (Ellipse, Rectangle, AreaCalculator, App) has one specific role.
class Geometricshapes:
    # Dependency Inversion Principle (DIP): High-level modules depend on abstractions (Geometricshapes), not on specific implementations.
    def area(self):
        pass

# Dependency Inversion Principle (DIP): Low-level modules (Geometricshapes classes) implement those abstractions.
class Ellipse(Geometricshapes):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Liskov Substitution Principle (LSP): Ellipse and Rectangle are both Geometricshapes and can be used interchangeably.
# Interface Segregation Principle (ISP): Rectangle class only defines the methods it needs to calculate Rectangle area.
class Rectangle(Geometricshapes):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class AreaCalculator:
    # Single Responsibility Principle (SRP): AreaCalculator calculates the area of different Geometricshapes.
    def calculate_area(self, shape):
        return shape.area()

class App:
    # Single Responsibility Principle (SRP): App runs the application.
    def run(self):
        ellipse = Ellipse(5)
        rectangle = Rectangle(4)
        
        calculator = AreaCalculator()
        ellipse_area = calculator.calculate_area(ellipse)
        rectangle_area = calculator.calculate_area(rectangle)
        
        print("Ellipse area:", ellipse_area)
        print("Rectangle area:", rectangle_area)

app = App()
app.run()

# Open/Closed Principle (OCP):
# You can easily add new Geometricshapes without changing existing code.
# The AreaCalculator can calculate areas of new Geometricshapes by extending the base Geometricshapes class.
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

# Liskov Substitution Principle (LSP):
# Ellipse and Rectangle are both shapes and can be used interchangeably.
# Subtypes must be substitutable for their base types.

# Interface Segregation Principle (ISP):
# Each class defines only the methods it needs.

# Dependency Inversion Principle (DIP):
# High-level modules depend on abstractions (Geometricshapes), not on specific implementations.
# Low-level modules (Geometricshapes classes) implement those abstractions.
# Abstractions should not depend upon details. Details should depend upon abstractions.
