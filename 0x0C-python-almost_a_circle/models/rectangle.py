#!/usr/bin/python3
"""
a module that contains rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    a rectangle inherited from base
    attribute:
        __width: rectangle width
        __height: rectangle height
        __x: x axis of rectangle
        __y: y axis of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        arguments:
            width : rectangle width
            height : rectangle height
            x : x axis of rectangle
            y : y axis of the rectangle
            id : id of the base object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """.__str__ method of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """rectangle width getter and setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """rectangle height getter and setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get and Set the x attribute of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get and Set the y attribute of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle."""
        return self.width * self.height

    def display(self):
        """print reactangle with #"""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        arguments:
            args: attributes to be modified
            kwargs: modified attributes
        """
        final_dict = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                final_dict[keys[i]] = args[i]
        else:
            final_dict = kwargs

        if len(final_dict) > 0:
            for key, value in final_dict.items():
                if key == 'id' and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictinary representation of rectangle"""
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }
