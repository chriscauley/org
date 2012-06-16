class Position(object):
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,p2):
        return Position(self.x+p2.x,self.y+p2.y,self.z+p2.z)
    def __str__(self):
        return str((self.x,self.y,self.z))
    def __neg__(self):
        self.x=-self.x
        self.y=-self.y
        self.z=-self.z
        return self
    def __sub__(self,p2):
        return self+(-p2)
    def magnitude(self):
        import math
        return math.sqrt(sum([self.x**2,self.y**2,self.z**2]))

start = Position(x=1,y=1,z=1)
end = Position(5,4,6)
difference = start-end
print start.magnitude()
