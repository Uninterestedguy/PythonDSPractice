# Finding euclidean distance
import math
x = list(map(int,input("Enter x1, x2 values").split("")))
y = list(map(int,input("Enter x1, x2 values").split("")))

print("="*40)
print("The Euclidean distance is: {}".format(round(math.dist(x,y),2)))