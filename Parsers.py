from oxygen import *
from hydrogen import *
from mAtom import *


#Contains input file parsers, extracts
class Parsers:

    def parse_geo(self, contents):
        #Sections of input file
        geometry = False
        matom = False
        qatom = False
        objects = []

        for line in contents:
            #Include an error catching mechanism
                
            #Gets quantum atoms properties
            if "qatom" in line:
                qatom = True
                continue
                
            while qatom == True:
                if "end" in line:
                    qatom = False
                    continue
                breakw
            
            #Gets newtonian atoms properties
            if "matom" in line:
                matom = True
                continue
            
            while matom == True:
                if "end" in line:
                    matom = False
                    continue
                line_contents = str(line).split(" ")
                for word in line_contents:
                    if word != '':
                        name = word
                        i = line_contents.index(word)
                        mass = int(line_contents[i+1])
                        oxcharge = int(line_contents[i+2])
                        pos = []
                        for j in range(i+3 , i+6):
                            pos.append(float(line_contents[j]))
                        objects.append(mAtom(name,mass,oxcharge,pos))
                        break
                break

            
            #Gets geometry info
            if "geometry" in line:
                geometry = True
                continue

            while geometry == True:
                if "end" in line:
                    geometry = False
                    continue

                line_contents = str(line).split(" ")
                for word in line_contents:
                    if word == 'O' or word == 'o':
                        pos = []
                        i = line_contents.index(word)
                        for j in range(i+1 , i+4):
                            pos.append(float(line_contents[j]))
                        objects.append(oxygen(pos))

                    if word == 'H' or word == 'h':
                        pos = []
                        i = line_contents.index(word)
                        for j in range(i+1 , i+4):
                            pos.append(float(line_contents[j]))
                        objects.append(hydrogen(pos))
                break
        return objects
    def parse_options(self,contents):
        for line in contents:
            print("Do something")

            
