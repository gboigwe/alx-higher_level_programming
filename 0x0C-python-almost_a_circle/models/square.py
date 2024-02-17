#!/usr/bin/python3

"""square.py
Created class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square object inheriting rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing constructor Square

        Args:
            size (int): The size of the square
            x (int): Inherited and called by super.
            y (int): Inherited and called by super.
            id (int): Inherited and called by super from Base.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Having a string function forthe class Square

        Returns:
            string: Output will be string
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Function Update for Square with args and kwargs"""
        if args is not None and len(args) > 0:
            keylist = ["id", "size", "x", "y"]
            for arg in range(len(args)):
                if arg < 4:
                    setattr(self, keylist[arg], args[arg])
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Outputs dictionary of a square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
