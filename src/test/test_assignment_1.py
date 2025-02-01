import math

from src.main.assignment_1 import approximation, bisection, fixedPoint, newtonRaphson


approximation()
bisection(10 ** -3, 1, 2, 12)
fixedPoint(1.5, 0.000001, 50)
newtonRaphson(math.pi / 4, 0.000001, 20)