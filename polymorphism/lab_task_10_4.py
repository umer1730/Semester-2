class Mul:
    def __init__(self,p,q,r,s):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
    def __mul__(self,other):
        return [[self.p*other.p+self.q*other.r,self.p*other.q+self.q*other.s],
                [self.r*other.p+self.s*other.r,self.r*other.q+self.s*other.s]]
    def __str__(self):
        return f"({self.p},{self.q},{self.r},{self.s})"
m1 = Mul(1,2,3,4)
m2 = Mul(5,6,7,8)
print(m1*m2)



