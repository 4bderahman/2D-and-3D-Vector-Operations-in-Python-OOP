class Vecteur2D:
    count = 0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        Vecteur2D.count += 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def to_string(self):
        return f"X = {self.x} ; Y = {self.y}"

    def equals(self, other):
        if isinstance(other, Vecteur2D):
            return self.x == other.get_x() and self.y == other.get_y()
        return False

    def norme(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_count():
        return Vecteur2D.count


class Vecteur3D(Vecteur2D):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self.z = z

    def get_z(self):
        return self.z

    def set_z(self, value):
        self.z = value

    def to_string(self):
        return f"X = {self.x} ; Y = {self.y} ; Z = {self.z}"

    def equals(self, other):
        if isinstance(other, Vecteur3D):
            return super().equals(other) and self.z == other.get_z()
        return False

    def norme(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


vecteur1 = Vecteur2D(1.5, 2)
vecteur2 = Vecteur2D(1.5, 2)
vecteur3 = Vecteur3D(1.5, 2, 3)

print(vecteur1.to_string())  
print(vecteur2.to_string())  
print(vecteur3.to_string())  

print(vecteur1.equals(vecteur2))  
print(vecteur1.equals(vecteur3))  

print(vecteur1.norme())  
print(vecteur3.norme())  

print(f"Number of vectors created: {Vecteur2D.get_count()}") 
