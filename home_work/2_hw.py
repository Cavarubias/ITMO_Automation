
def task_1(a:int = 1, b:float = 1.5, c:str = '2', d=None, e:bool = True) ->any:
    if d is None:
        d = [3, 4, 5]
    return type(a), type(b), type(c), type(d), type(e)
print (task_1())


def task_2(a=None) ->list:
    if a is None:
        a = [1, 2, 3, 5, 8, 13, 21]
    return [a[0], a[1], a[2]]
print(task_2())


def task_3(a) ->int:
    return a**2
print (task_3(2))