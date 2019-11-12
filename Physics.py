from Force_Field import sim_box

class Physics:

    #Gets the acceleration for each bq_charge in a force field
    def update_accel(self, field, objects):
        for obj in objects:
            obj.accel = [field[int(round(obj.x))][int(round(obj.y))][0] * obj.oxcharge * 1.602E-19 / (obj.mass * 1.6726219E-27), field[int(round(obj.x))][int(round(obj.y))][1] * obj.oxcharge * 1.602E-19 / (obj.mass * 1.6726219E-27)]

    def update_velocity(self, time_step, objects):
        for obj in objects:
            obj.velocity = [obj.velocity[0] + obj.accel[0]*time_step, obj.velocity[1] + obj.accel[1]*time_step]
            #Boundary issues
            if obj.x < 1 or obj.x > sim_box-1:
                obj.velocity[0] = 0 - obj.velocity[0]
            if obj.y < 1 or obj.y > sim_box-1:
                obj.velocity[1] = 0 - obj.velocity[1]

    def update_position(self, time_step, objects):
        for obj in objects:
            obj.x = obj.x + (obj.velocity[0]*time_step) + (time_step**2*.5 *obj.accel[0])
            obj.y = obj.y + (obj.velocity[1]*time_step) + (time_step**2*.5 *obj.accel[1])
            #Boundary issues
            if obj.y < 1:
                obj.y = 1
            if obj.y > sim_box-1:
                obj.y = sim_box-1
            if obj.y < 1:
                obj.y = 1
            if obj.y > sim_box-1:
                obj.y = sim_box-1


