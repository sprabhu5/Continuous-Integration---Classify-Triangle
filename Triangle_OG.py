# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
def classify_triangle(a, b, c):
    types = {'equilateral': 'equilateral',
             'isosceles': 'isosceles',
             'scalene': 'scalene',
             'isosceles and right': "isosceles and right",
             'scalene and right': 'scalene and right',
             'not valid': 'not valid'}
    sides = [a, b, c]
    try:
        if not validate_input(sides):
            return types['not valid']
    except TypeError:
        return types['not valid']

    sides = parse_input(sides)

    if not validate_sides(sides):
        return 'not valid'

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == b and b == c:
        triangle_types = types['equilateral']
    elif a == b or b == c:
        triangle_types = types['isosceles']
        if check_right(a, b, c):
            triangle_types = types['isosceles and right']
    else:
        triangle_types = types['scalene']
        if check_right(a, b, c):
            triangle_types = types['scalene and right']

    return triangle_types


def validate_input(sides):
    for element in sides:
        if element <= 0:
            return False

    return True


def parse_input(sides):
    parsed = []
    for element in sides:
        parsed.append(float(element))
    return sorted(parsed)


def validate_sides(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True


def check_right(a, b, c):
    if round(a * a, 2) + round(b * b, 2) == round(c * c, 2):
        return True
    return False
    

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
