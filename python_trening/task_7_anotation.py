a: int = 5
b: str = 'Строка'
c: list = [1, 2]


def indent (s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print (indent('123', 123))


def string_len (s) -> int:
    return (len(s))

print (string_len(''))


def list_len (a=[1,2], b=[1,2,3]) -> int:
    return (max(len(a), len(b)))

print (list_len())



def append_list(my_list:list):
    my_list.append('test')
    return (my_list)

print (append_list(['один', 2, 3]))


def sum_list(just_list:list) -> int:
    result = 0
    for elem in just_list:
            result = result + elem
    return result

print(sum_list([1, 2, 3]))