class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

   
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero.")

    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero.")



rectangle = Rectangle(5, 3)


print(rectangle.width)   
print(rectangle.height) 


rectangle.width = 10
rectangle.height = 6

print(rectangle.width)   
print(rectangle.height) 