class Position(object):
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return str((self.x,self.y,self.z))
    def magnitude(self):
        return (self.x**2+self.y**2+self.z**2)**.5
    def __add__(self,p):
        return Position(self.x+p.x, self.y + p.y, self.z + p.z)
    def __neg__(self):
        self.x=-self.x
        self.y=-self.y
        self.z=-self.z
        return self
    def __sub__(self,p):
        return self+(-p)
p=Position(y=10)
p2=Position(1,2,3)
print p-p2

