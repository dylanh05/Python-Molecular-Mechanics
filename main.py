#TODO: create function that can create a new atom object for any atom (like a par file)
# Make input file more functional: include input and output file
# Long term goals: incorporate QM calculation


from Parsers import *
from Force_Field import *
from Physics import *

global input_file
global output_file

def run_sim(input_file,out_file,time_step,center,iter):
    system = Parsers()
    objects = system.parse_geo(input_file)

    fields = Force_Field()
    physics_env = Physics()

    position = fields.init_position(center,objects)

    with open(out_file, "w") as out_file:
        out_file.write("Python Molecular Mechanics \n")

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
                out_file.write(obj.name + " coordinates: " + str(obj.x) + " " + str(obj.y) + "\n")

def main():
    input_file = input("Input file name: ")
    out_file = input("Output file name: ")
    run_sim(input_file, out_file, .000000000001, True, 300)

main()
