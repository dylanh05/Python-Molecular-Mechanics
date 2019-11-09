from oxygen import *
from hydrogen import *

#Contains input file parsers, extracts
class Parsers:

    def parse_geo(self, input_file):
        with open(input_file) as inp:
            global contents
            contents = inp.read().splitlines()
        geometry = False
        objects = []

        for line in contents:
            #Gets geometry info
            if line == "geometry":
                geometry = True
                continue

            while geometry == True:
                if line == "end":
                    geometry = False
                    continue

                line_contents = str(line)
                line_contents = line_contents.split(" ")
                for word in line_contents:
                    if word == 'O' or word == 'o':
                        pos = []
                        i = line_contents.index(word)
                        for j in range(i+1 , i+4):
                            pos.append(float(line_contents[j]))
                        atom = oxygen(pos)
                        objects.append(atom)

                    if word == 'H' or word == 'h':
                        pos = []
                        i = line_contents.index(word)
                        for j in range(i+1 , i+4):
                            pos.append(float(line_contents[j]))
                        atom = hydrogen(pos)
                        objects.append(atom)
                break
        return objects
