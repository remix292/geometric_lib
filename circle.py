import math
import unittest


def area(r):
    """Принимает радиус r и возвращает площадь круга с таким радиусом
    Параметр: r (int) - радиус круга
    Возвращает: area (int) - площадь круга с указанным радиусом
    print(area(3))
    ---------------------
    28.274333882308138"""
    if r < 0:
        raise AssertionError("""ТЫ ЧО БОЛЬНОЙ!111!!1
        Value must be over or equale 0""")
    else:
        return math.pi * r * r


def perimeter(r):
    """Принимает радиус r и возвращает периметр круга с таким радиусом
    Параметр: r (int) - радиус круга
    Возвращает: perimeter (int) - периметер круга с указанным радиусом

    print(perimeter(3))
    ---------------------
    18.84955592153876"""
    if r < 0:
        raise AssertionError("Value must be over or equale 0")
    else:
        return 2 * math.pi * r


print(perimeter(3))


class CircleTestCase(unittest.TestCase):
    def test_area_right(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)
        res = area(5)
        self.assertAlmostEqual(res, 78.53981634)
        res = area(45)
        self.assertAlmostEqual(res, 6361.72512352)
        res = area(83)
        self.assertAlmostEqual(res, 21642.4317906)
        res = area(17)
        self.assertAlmostEqual(res, 907.920276887)

    def test_perim_right(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.415926536)
        res = perimeter(45)
        self.assertAlmostEqual(res, 282.743338823)
        res = perimeter(83)
        self.assertAlmostEqual(res, 521.504380496)
        res = perimeter(17)
        self.assertAlmostEqual(res, 106.814150222)

    def test_area_errors(self):
        # with self.assertRaises(AssertionError):
        #     area()
        # with self.assertRaises(AssertionError):
        #     area("a")
        with self.assertRaises(AssertionError):
            area(-5)
        # with self.assertRaises(AssertionError):
        #     area(5, 4)

    def test_perimeter_errors(self):
        # with self.assertRaises(AssertionError):
        #     perimeter()
        # with self.assertRaises(AssertionError):
        #     perimeter("a")
        with self.assertRaises(AssertionError):
            perimeter(-5)
        # with self.assertRaises(AssertionError):
        #     perimeter(1, 5)