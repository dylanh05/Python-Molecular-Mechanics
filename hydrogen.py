class hydrogen:
    def __init__(self,pos):
        self.name = "Hydrogen"
        self.mass = 1
        self.oxcharge = 1
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.accel = [0, 0]
        self.velocity = [0, 0]
