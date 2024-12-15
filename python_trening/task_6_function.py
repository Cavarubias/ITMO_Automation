def add (x, y):
    return x + y

print (add(1, 2))

def arg (a, b, c=2, d=3):
    return a + b + c + d

print (arg(1, 1, 1, 1))
print (arg(2, 2,))
print (arg(1, 1, 1))


def range_arg (a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print (range_arg('1', '2', '3', '4'))
print (range_arg('1', '2', d='3', c='4'))


def task1 (a=(1, 2, 4, 4)):
    return a[1]
print (task1())

def area_of_the_circle (radius, pi=3.14159):
     return pi * radius**2
print (area_of_the_circle(3))