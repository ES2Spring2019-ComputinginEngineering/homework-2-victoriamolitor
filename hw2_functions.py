# HOMEWORK 2 --- ES2
# Triangle Calculator

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Victoria Molitor
# NUMBER OF HOURS TO COMPLETE: 0.5 (please track how long this homework takes you to complete).
# YOUR COLLABORATION STATEMENT(s) (refer to syllabus): I worked alone on this assignment.
#
#*****************************************

#In this homework,the ultimate goal is to create a function called areaofatriangle,
#which takes six parameters which represent three intersecting lines
#of the form y = (m * x) + b that mark the three sides of the triangle.

#In order to accomplish this you will need functions which determine
#where two lines intersect (x and y), a function which determines the distance between
#two points represented by (x,y) coordinates, and a function which determines
#the area of a triangle using three side lengths(using Heron's Formula).

#Please complete the four required functions below:

import math

def intersectionoftwolines_x(m1, b1, m2, b2):
    x = (b2-b1)/(m1-m2)
    return x

def intersectionoftwolines_y(m1, b1, m2, b2):
    y = m1*((b2-b1)/(m1-m2))+b1
    return y

def distancebetweenpoints(x1, y1, x2, y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

def heronsformula(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return area

def areaofatriangle(m1, b1, m2, b2, m3, b3):
    d = intersectionoftwolines_x(m1, b1, m2, b2)
    e = intersectionoftwolines_y(m1, b1, m2, b2)
    f = intersectionoftwolines_x(m1, b1, m3, b3)
    g = intersectionoftwolines_y(m1, b1, m3, b3)
    h = intersectionoftwolines_x(m2, b2, m3, b3)
    i = intersectionoftwolines_y(m2, b2, m3, b3)

    j = distancebetweenpoints(d, e, f, g)
    k = distancebetweenpoints(d, e, h, i)
    l = distancebetweenpoints(f, g, h, i)
    area = heronsformula(j, k, l)
    return area

#TEST CASES
#These print statements will be true when your functions are working.

print("Distance between Points:")
#If these are both true, it is likely that your function is working.
print(distancebetweenpoints(0, 0, 3, 4) == 5)
print(distancebetweenpoints(0, 0, 1, 1) == math.sqrt(2))
print("*********")

print("Intersection of Two Lines:")
#If these are all true, it is likely that your function is working.
print(round(intersectionoftwolines_x(3, -3, 2.3, 4),2) == 10)
print(round(intersectionoftwolines_y(3, -3, 2.3, 4),2) == 27)
print(round(intersectionoftwolines_x(10, 10, 30, 0),2) == .5)
print(round(intersectionoftwolines_y(10, 10, 30, 0),2) == 15)
print("*********")

print("Heron's Formula:")
print(round(heronsformula(5, 5, 8), 2) == 12)
print(round(heronsformula(5, 5, 6), 2) == 12)
print("*********")

print("Area of a Triangle:")
#If these are both true, it is likely that your function is working.
print(round(areaofatriangle(10, 10, 20, 0, 30, 0),2) == 2.5)
print(round(areaofatriangle(0, 0, 1, 0, -1, 10),2) == 25)
print("*********")