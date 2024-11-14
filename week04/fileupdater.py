#!/usr/bin/env python3

"""File and Exception Handling"""

if __name__ == "__main__":
    the_file = input("Enter the file file: ")

    try:
        with open(the_file, "+a") as original_file:
            data = original_file.read()
            newdata = f"{data}\nupdated\n"
            original_file.write(newdata)
    except FileNotFoundError as e:
        pass
