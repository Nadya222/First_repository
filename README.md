[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Nadya222/First_repository/blob/main/.github/workflows/2.yml)

[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Nadya222/First_repository/actions)


ТЗ3

ФИО: Чернявская Надежда

Программа _math_func.py_

Считываем числа из файла _math_func.txt_ и записываем их в список под названием _data_

```python
data = []
with open("math_func.txt", "r") as file:
    for line in file:
        data.extend([float(x) for x in line.split()])
```

Пишем функции add(сложение), product(произведение) чисел списка, а также minimum и maximum. Проверим возможные ошибки (например, когда встречаются не числа, а буквы в файле(ValueError), или файл является пустым, или возникла ошибка с типом данных(TypeError)).

```python
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
```
Чтобы предотвратить аварийное завершение программы из-за ошибки переполнения, рассмотрим диапазон значений типа float. Если сумма или произведение выходит за данный диапазон, то завершаем работу программы и выводим "OverflowError".
```python
def incorrect_data_size(data):
    max_float = 1e308
    min_float = -1e308
    if add(data) > max_float or add(data) < min_float or product(data) > max_float or product(data) < min_float:
        return "OverflowError"
```
***
Тестированние _test_math_func.py_
С помощью assert проверим работу четырех функций.
```python
import unittest
import pytest
from math_func import add, product, maximum, minimum
import time
from timeit import default_timer as timer
class TestDataProcessing(unittest.TestCase):
    def test_add(self):
        assert add([2, 3]) == 5
        assert add([7, 12]) == 19

    def test_product(self):
        assert product([1, 15]) == 15
        assert product([0, 3]) == 0
        assert product([3, 4]) == 12
        assert product([5, -2]) == -10

    def test_maximum(self):
        assert maximum([1, 12]) == 12
        assert maximum([-7, -19]) == -7
        assert maximum([0, -4, 7, 45.5]) == 45.5

    def test_minimum(self):
        assert minimum([1, -15]) == -15
        assert minimum([-7, -19, 0]) == -19
        assert minimum([0, 5, -20, -25.5]) == -25.5
```

В качестве дополнительного теста, проверим работу функции минимума, когда в файле встречаются не только цифры.

```python
    def test_not_number(self):
        test_case = ['aaa', 4, 2.4, 'abcd']
        with pytest.raises(ValueError) as err:
            minimum(test_case)
```

Для теста проверки скорости работы программы при увеличении размера входного файла возьмем два списка, пропорциональных по длине. Посчитаем длительности выполнения программы и затем сравним значения.

```python
    def test_time1(self):
        start_time1 = timer()
        data1 = [1, 2, 3, 4, 5]
        len1 = len(data1)
        product1 = product([1, 2, 3, 4, 5])
        add1 = add([1, 2, 3, 4, 5])
        min1 = minimum([1, 2, 3, 4, 5])
        max1 = maximum([1, 2, 3, 4, 5])
        end_time1 = timer()
        duration1 = end_time1 - start_time1
        start_time2 = timer()
        data2 = [-2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5]
        len2 = len(data2)
        product2 = product([-2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5])
        add2 = add([-2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5])
        min2 = minimum([-2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5])
        max2 = maximum([-2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5, 2, 3, 6, 4, 3, 12, 54, 45, 78, 78, 45, 45, 0, -56, -4, 1, 2, 3, 4, 5])
        end_time2 = timer()
        duration2 = end_time2 - start_time2
        assert duration2 <= duration1 * 12
```
