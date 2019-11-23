class oxygen:
    def __init__(self,pos):
        self.name = "O"
        self.mass = 16
        self.oxcharge = -2
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.zpotneg = 0
        self.zpotpos = 0
        self.accel = [0, 0, 0]
        self.velocity = [0, 0, 0]
        self.kenergy = .5*self.mass*(self.velocity[0]**2+self.velocity[1]**2+self.velocity[2]**2)
