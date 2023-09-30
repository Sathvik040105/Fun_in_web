import random
import matplotlib.pyplot as plt


#Checks if the point "p" lies on left side of line joining "p1" and "p2"
#Such condition is satisfied when cross product of vectors p1p2 and p1p is >= 0
def on_left_side(p1, p2, p):
    cross_product = (p2[0]-p1[0])*(p[1]-p1[1])-(p[0]-p1[0])*(p2[1]-p1[1])   
    if(cross_product >= 0):
        return True
    return False

#checks whether a point "p" is inside the triangle formed by p1, p2, p3
def lies_inside(p):
    if(not on_left_side(p1, p2, p)):
        return False
    if(not on_left_side(p2, p3, p)):
        return False
    if(not on_left_side(p3, p1, p)):
        return False
    return True


#Swaps points so that p1, p2, p3 are in counter-clockwise direction
def orient_points():
    global p1, p2, p3
    if(not on_left_side(p1, p2, p3)):
        p2, p3 = p3, p2


#Generates a random point inside the triangle
def gen_valid_random_point():
    x_min = min(p1[0], p2[0], p3[0])    
    x_max = max(p1[0], p2[0], p3[0])
    y_min = min(p1[1], p2[1], p3[1])
    y_max = max(p1[1], p2[1], p3[1])
    while True:
        ran_num = random.random()
        x = x_min + ran_num*(x_max-x_min)
        ran_num = random.random()
        y = y_min + ran_num*(y_max-y_min)
        if(lies_inside([x, y])):
            return [x, y]
   

#Playable parameters
p1 = [0,0]
p2 = [1,0] 
p3 = [0.5, (3**0.5)/2]
points_list = [p1, p2, p3]
iterations = 10000


#Generating points and plotting them
orient_points()
x_list = []
y_list = []
x, y = gen_valid_random_point()
for i in range(iterations):
    ran_vertex = random.choice(points_list)
    x = (x + ran_vertex[0])/2
    y = (y + ran_vertex[1])/2
    x_list.append(x)
    y_list.append(y)
plt.scatter([p[0] for p in points_list], [p[1] for p in points_list], color="red", s=5)
plt.scatter(x_list, y_list, color="blue", s=0.5) 
plt.show()




