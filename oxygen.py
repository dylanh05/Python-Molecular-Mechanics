class oxygen:
    def __init__(self,pos):
        self.name = "Oxygen"
        self.mass = 16
        self.oxcharge = -2
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.accel = [0, 0]
        self.velocity = [0, 0]
