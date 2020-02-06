import unittest

from Triangle_OG import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):

    def testInvalidInput(self):
        """
        Validation of an input
        """
        self.assertEqual(classify_triangle(2, 2, -3), 'not valid')

        self.assertEqual(classify_triangle('a', '2', 3), 'not valid')

    def testInvalidTriangle(self):
        """
        to see that the input satisfy the condition to be a triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'not valid')

    def testRightTriangle(self):
        """
        cheching for right angle and display the type of a triangle 
        """
        self.assertEqual(classify_triangle(1, 1, 1.414213), 'isosceles and right')

        self.assertEqual(classify_triangle(3, 4, 5), 'scalene and right')

    def testEquilateralTriangle(self):
        """
        check for equilateral 
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')

    def testIsoscelesTriangle(self):
        """
        check for Isosceles
        """
        self.assertEqual(classify_triangle(2, 2, 3), 'isosceles')

    def testScaleneTriangle(self):
        """
        check for scalene 
        """
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene')


if __name__ == '__main__':
    unittest.main()
