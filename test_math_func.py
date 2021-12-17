import unittest
import pytest
from math_func import add, product, maximum, minimum
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

    def test_not_number(self):
        test_case = ['aaa', 4, 2.4, 'abcd']
        with pytest.raises(ValueError) as err:
            minimum(test_case)


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
        
if __name__ == '__main__':
    unittest.main()
