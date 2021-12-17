data = []
with open("math_func.txt", "r") as file:
    for line in file:
        data.extend([float(x) for x in line.split()])
#print(data)

def add(data):
    res = 0
    if not isinstance(data, list):
        raise TypeError("input data not a list")
    for elem in data:
        if not isinstance(elem, (float, int)):
            raise ValueError('One element of list not a number')
    if len(data) == 0:
        return None
    for i in data:
        res = res + float(i)
    return res
#print(add(data))


def product(data):
    res1 = 1
    if not isinstance(data, list):
        raise TypeError("input data not a list")
    for elem in data:
        if not isinstance(elem, (float, int)):
            raise ValueError('One element of list not a number')
    if len(data) == 0:
        return None

    spl = list(map(float, data))
    for s in spl:
        res1 *= s
    return res1
#print(product(data))



def minimum(data):
    if not isinstance(data, list):
        raise TypeError("input data not a list")
    for elem in data:
        if not isinstance(elem, (float, int)):
            raise ValueError('One element of list not a number')
    if len(data) == 0:
        return None

    min_element = data[0]
    for elem in data:
        if elem < min_element:
            min_element = elem
    return min_element
#print(minimum(data))

def maximum(data):
    if not isinstance(data, list):
        raise TypeError("input data not a list")
    for elem in data:
        if not isinstance(elem, (float, int)):
            raise ValueError('One element of list not a number')
    if len(data) == 0:
        return None

    max_element = data[0]
    for elem in data:
        if elem > max_element:
            max_element = elem
    return max_element
#print(maximum(data))

def incorrect_data_size(data):
    max_float = 1e308
    min_float = -1e308
    if add(data) > max_float or add(data) < min_float or product(data) > max_float or product(data) < min_float:
        return "OverflowError"
