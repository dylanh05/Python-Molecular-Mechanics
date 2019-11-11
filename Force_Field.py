import numpy as np
import math

class Force_Field:

    global sim_box
    sim_box = 1000 #picometers

    #initializes positions of points charges in a grid
    def init_position(self, center, objects):
        position = np.empty((sim_box,sim_box),dtype=object)

        for obj in objects:
            xcoor = obj.x * 100
            ycoor = obj.y * 100
            if center:
                xcoor = xcoor + sim_box/2
                ycoor = ycoor + sim_box/2
            position[int(round(xcoor)),int(round(ycoor))] = obj
            #update object attributes so we dont have to do this everytime we move atom
            obj.x = xcoor
            obj.y = ycoor
        return position

    #Creates matrix of electric potentials in space due to each point charge, then creates final potentials at each point by summing
    #Note: bq_potential must be run after generating position
    def bq_potential(self, objects):
        k = 8987551788
        all_potentials = np.zeros((sim_box,sim_box))

        for obj in objects:
            potentials = np.zeros((sim_box,sim_box))
            for index in np.ndenumerate(potentials):
                x = index[0][0]
                y = index[0][1]
                distance = (math.sqrt((obj.x - x)**2 + (obj.y - y)**2))*1E-12
                if distance == 0:
                    distance = 10E-14
                potential = (k * obj.oxcharge * 1.602E-19)/distance
                potentials[index[0][0], index[0][1]] = potential
            all_potentials = all_potentials + potentials
        return all_potentials

    #Creates force field by numerically calculating gradients at each point on the potential surface
    def field(self, potential):
        field = np.empty((sim_box,sim_box),dtype=object)
        for index in np.ndenumerate(potential[1:-1:1,1:-1:1]):
            x = index[0][0]+1
            y = index[0][1]+1
            point_field = [0-((potential[x+1][y]-potential[x-1][y])/2E-12), 0-((potential[x][y+1]-potential[x][y-1])/2E-12)]
            field[x][y] = point_field
        return field

    def update_position(self, objects):
        position = np.empty((sim_box,sim_box),dtype=object)

        for obj in objects:
            position[int(round(obj.x)), int(round(obj.y))] = obj
        return position
