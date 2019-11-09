#TODO: write potential calculations, create function that can create a new atom object for any atom (like a par file)

from Parsers import *
from Force_Field import *

global input_file
global output_file

input_file = input("Input file name: ")
output_file = input("Output file name: ")

def main():
    system = Parsers()
    objects = system.parse_geo(input_file)
    print(objects)

    fields = Force_Field()
    position = fields.init_position(True,objects)


main()
