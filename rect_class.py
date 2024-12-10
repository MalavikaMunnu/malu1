class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

length1 = int(input("Enter the length of the first rectangle: "))
breadth1 = int(input("Enter the breadth of the first rectangle: "))
rect1 = Rectangle(length1, breadth1)
print(f"Area of the first rectangle: {rect1.area()}")
print(f"Perimeter of the first rectangle: {rect1.perimeter()}")

length2 = int(input("Enter the length of the second rectangle: "))
breadth2 = int(input("Enter the breadth of the second rectangle: "))
rect2 = Rectangle(length2, breadth2)
print(f"Area of the second rectangle: {rect2.area()}")
print(f"Perimeter of the second rectangle: {rect2.perimeter()}")





if rect1.area() > rect2.area():
    print("The first rectangle has a larger area.")
elif rect1.area() < rect2.area():
    print("The second rectangle has a larger area.")
else:
    print("both rectangles have the same area")
