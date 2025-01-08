class A:



    def __init__(self, x):
        self.x = x



class B(A):



    def __init__(self, x, y):
        super().__init__(x)
        self.y = x + 5


Emp = B(5, 5)

print(Emp.y)