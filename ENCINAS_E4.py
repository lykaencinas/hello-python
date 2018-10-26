from math import sqrt


data = input ("Enter the side lengths of a triangle:t")

def triangle_perimeter (a, b, c):
    return a + b + c

def triangle_heronsarea (a, b, c):
    s = triangle_perimeter (a,b,c) /2

    area = sqrt(s * (s-a) * (s-b ) * (s-c))
    return area

