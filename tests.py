from Parsers import *
import numpy as np


system = Parsers()
objects = system.parse_geo("input.txt")

sim_box = 10000 #Figure out what units this is

k = 8987551788.7
for obj in objects:
    charge = obj.oxcharge
    potential = np.zeros((sim_box,sim_box))

print(potential)
