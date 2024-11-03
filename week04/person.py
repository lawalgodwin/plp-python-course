#!/usr/bin/env python3

from typing import Literal, NoReturn

# Object oriented programming

class Person:
    def __init__(self, name: str, age: int, gender: Literal["Male", "Female"]) -> None:
        """Class constructor"""
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    def introduce(self) -> NoReturn:
        """A method that introduces a person object"""
        print(f"Hello, my name is {self.__name}, I'm {self.__age} and I'm a {self.__gender}")


"""Construct a person object and called the introduce method"""

John = Person("John", 23, "Male")

John.introduce()
