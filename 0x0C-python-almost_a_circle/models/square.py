#!/usr/bin/python3
"""
a module that contains a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a square inherited from Rectangle
    attribute:
        size: square size
        x: x axis of square
        y: y axis of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        arguments:
            size: square size
            x: x axis of square
            y: ty axis of the square
            id: the id of the base obect
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """.__str__ method of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square size getter and setter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        arguments:
            args: attributes to be modified
            kwargs: modified attributes
        """
        final_dict = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for i in range(len(args) if len(args) <= 4 else 4):
                final_dict[keys[i]] = args[i]
        else:
            final_dict = kwargs

        if len(final_dict) > 0:
            for key, value in final_dict.items():
                if key == 'id' and value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictinary representation of square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
