#polymorphism
#example of run time polymorphism with inheritance
class Shape:
    def draw(self):
        pass
class Circle(Shape):
    def draw (self):
        print("draw the method of circle class")
class Rectangle(Shape):
    def draw(self):
        print("draw the method of rectangle class")
def call_draw(Shape):
    Shape.draw()
obj=input("Enter Circle or Rectangle:")
c=""
if obj=="Circle":
    c=Circle()
elif obj=="Rectangle":
    c=Rectangle()
call_draw(c)

#polymorphism without inheritance
class Circle():
    def draw(self):
        print("draw method of circle class")
class Rectangle():
    def draw(self):
        print("draw method of rectangle class")
def call_draw(s):
    s.draw()
obj=input("Enter circle or rectangle:")
c=""
if obj=="Circle":
    c=Circle()
elif obj=="Rectangle":
    c=Rectanlge()
call_draw(c)

#create a base class account having method deposit,create child class
#saving and current ovveriding the deposit method, create a method
#call_deposit to achieve polymorphism.