# TODO: create function that can create a new atom object for any atom (like a par file)
# Make input file more functional: include input and output file
# Increase randomness by using statistical mechanics
# Convert to 3D
# Include NVT thermostat for customizable isotherms
# More thermodynamic state metrics, properties
# Print options
# Long term goals: incorporate QM calculation

from Parsers import *
from Force_Field import *
from Physics import *

global input_file
global output_file

def run_sim(input_file,out_file,time_step,center,iter):
    out_file_name = str(out_file)
    read_file = Parsers()
    with open(input_file) as inp:
        contents = inp.read().splitlines()
    objects = read_file.parse_geo(contents)

    fields = Force_Field()
    physics_env = Physics()

    with open(out_file, "w") as out_file:
        out_file.write("Python Molecular Mechanics \n")
        position = fields.init_position(center,objects)
        for i in range(0, iter):
            potential = fields.bq_potential(objects, position)
            field = fields.field(potential, position)
            physics_env.update_accel(field, objects)
            physics_env.update_velocity(time_step, objects)
            physics_env.update_position(time_step, objects)
            position = fields.update_position(objects)

            #Outputs
            out_file.write("\n")
            out_file.write("Iteration: " + str(i) + "\n")
            for obj in objects:
                out_file.write(obj.name + " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.z) + "\n")
    out_file.close()
    print("Trajectory information saved to " + out_file_name)
def main():
    input_file = input("Input file name: ")
    out_file = input("Output file name: ")
    run_sim(input_file, out_file, .000000000001, True, 10)

main()
