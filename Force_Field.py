import numpy as np

class Force_Field:

    global sim_box
    sim_box = 10000 #Figure out what units this is

    #initializes positions of points charges in a grid
    def init_position(self,center,objects):
        position = np.empty((sim_box,sim_box),dtype=object)

        for obj in objects:
            xcoor = obj.x * 100
            ycoor = obj.y * 100
            if center:
                xcoor = int(np.round(xcoor + sim_box/2))
                ycoor = int(np.round(ycoor + sim_box/2))
            position[xcoor,ycoor] = obj
            #update object attributes so we dont have to do this everytime we move atom
            obj.x = xcoor
            obj.y = ycoor
        return position

    #Creates matrix of electric potentials in space due to each point charge, then creates final potentials at each point by summing
    def bq_potential(self, objects):
        k = 8987551788.7

        for obj in objects:
            charge = obj.oxcharge()
            potential = np.zeroes(sim_box)






