import unittest


def area(a, b):
    """Принимает стороны прямоугольника a, b и возвращает площадь 
    прямоугольника с такими сторонами
    Параметры: a (int) - длинна прямоугольника
               b (int) - ширина прямоугольника
    Возвращает: area (int) - площадь прямоугольника с заданными сторонами

    print(area(3, 2))
    ---------------------
    6"""
    if (a <= 0) or (b <= 0):
        raise AssertionError("Values must be over 0")
    else:
        return a * b


def perimeter(a, b):
    """Принимает стороны прямоугольника a, b и возвращает периметр 
    прямоугольника с такими сторонами
    Параметры: a (int) - длинна прямоугольника
               b (int) - ширина прямоугольника
    Возвращает: perimeter (int) - периметр прямоугольника с заданными сторонами

    print(perimeter(3, 2))
    ---------------------
    10"""
    if (a <= 0) or (b <= 0):
        raise AssertionError("Values must be over 0")
    else:
        return (a + b) * 2


"""Добавлент комментарий"""


class RectangleTestCase(unittest.TestCase):
    def test_area_right(self):
        res = area(6, 10)
        self.assertEqual(res, 60)
        res = area(47, 61)
        self.assertEqual(res, 2867)
        res = area(61, 47)
        self.assertEqual(res, 2867)
        res = area(32, 32)
        self.assertEqual(res, 1024)

    def test_perim_right(self):
        res = perimeter(5, 7)
        self.assertEqual(res, 24)
        res = perimeter(7, 5)
        self.assertEqual(res, 24)
        res = perimeter(10, 6)
        self.assertEqual(res, 32)
        res = perimeter(6, 10)
        self.assertEqual(res, 32)

    def test_area_errors(self):
        # with self.assertRaises(AssertionError):
        #     area(1)
        # with self.assertRaises(AssertionError):
        #     area("a", 1)
        # with self.assertRaises(AssertionError):
        #     area("a", "b")
        with self.assertRaises(AssertionError):
            area(0, 5)
        with self.assertRaises(AssertionError):
            area(7, 0)
        with self.assertRaises(AssertionError):
            area(0, 0)
        with self.assertRaises(AssertionError):
            area(-5, 5)
        with self.assertRaises(AssertionError):
            area(5, -7)
        with self.assertRaises(AssertionError):
            area(-5, -7)
        # with self.assertRaises(AssertionError):
        #     area(5, 7, 6)

    def test_perimeter_errors(self):
        # with self.assertRaises(AssertionError):
        #     perimeter(1)
        # with self.assertRaises(AssertionError):
        #     perimeter("a", 1)
        # with self.assertRaises(AssertionError):
        #     perimeter("a", "b")
        with self.assertRaises(AssertionError):
            perimeter(0, 1)
        with self.assertRaises(AssertionError):
            perimeter(2, 0)
        with self.assertRaises(AssertionError):
            perimeter(0, 0)
        with self.assertRaises(AssertionError):
            perimeter(-3, 1)
        with self.assertRaises(AssertionError):
            perimeter(3, -1)
        with self.assertRaises(AssertionError):
            perimeter(-3, -1)
        # with self.assertRaises(AssertionError):
        #     perimeter(3, 1, 2)