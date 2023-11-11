#!/usr/bin/python3
"""
a module with base class of others
"""
import json
import csv
import turtle


class Base():
    """
    Base class of structures
    attribute:
        __nb_objects: number of ojects created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        arguments:
            id: the id of the base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        arguments:
            list_dictionaries: dictionary list
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        arguments:
            list_objs: a list of objects.
        """
        final_list = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                final_list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as fle:
            fle.write(Base.to_json_string(final_list))

    @staticmethod
    def from_json_string(json_string):
        """
        arguments:
            json_string: list dictionary as a string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        arguments:
            dictionary: wanted values
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """instances of lists returner"""
        try:
            with open(cls.__name__ + ".json", 'r') as fle:
                json_file = Base.from_json_string(fle.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        arguments:
            list_objs: finals objects list
        """
        some_list = []
        with open(cls.__name__ + ".csv", 'w') as fle:
            if list_objs is None or len(list_objs) <= 0:
                fle.write('[]')
            else:
                if cls.__name__ is "Rectangle":
                    some_list = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    some_list = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=some_list)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserilise the csv
        """
        some_list = []
        try:
            with open(cls.__name__ + ".csv", 'r') as fle:
                if cls.__name__ is "Rectangle":
                    some_list = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    some_list = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(fle, fieldnames=some_list)
                dcts = [dict([k, int(v)] for k, v in fl.items())
                        for fl in reader]
                return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """
        arguments:
            list_rectangles: rectangle lists
            list_squares: square lists
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#ffffff')
        t.shape('circle')
        t.color('#000000')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
