#!/usr/bin/env python3

"""This module demostrates the use of OOP concepts"""

import abc

class Movable(metaclass=abc.ABCMeta):
    """This is our interfcae"""
    @abc.abstractmethod
    def move(self) -> None:
        raise NotImplemented

"""Define our concrete classes to implement the Movable interface"""

class Animal(Movable):
    """First concrete class"""
    def move(self) -> None:
        print("Animal is moving")

class Vehicle(Movable):
    """Second concrete class"""
    def move(self) -> None:
        print("Vehicle is moving")


"""Create instance of each concrete class and call the move method on it"""

for movable in [Animal(), Vehicle()]:
    movable.move()