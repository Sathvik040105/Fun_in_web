#This is an Assignment problem from DSA course
#We have to implement an algorithm that finds "Convex Hulls" using "Divide and Conquer" strategy
#We can visualize this using below code.


#takes three points p1, p2, p
#Checks whether vector p1 p lies on left side of vector p1 p2
#This function achieves that by computing cross product and checking for it's sign
def on_left_side(p1, p2, p):
    ans = (p2[0]-p1[0])*(p[1]-p1[1])-(p2[1]-p1[1])*(p[0]-p1[0])
    if(ans >= 0):
        return True
    else:
        return False


#This a bruteforce algorithm
#This checks every pair of line that can be made
#if all points are left side to that line, then that line is a part of convex hull
#Keep repeating till you find all
def bruteforce_ch(points):
    ch = [points[0]]
    curr_point = points[0]
    n = len(points)
    vis = [False for i in range(n)]
    vis[0] = True
    ch_length = 1
    while True:
        for i in range(n):
            next_point = points[n-1-i]
            if(vis[n-1-i]):
                continue
            pos = True
            for other_point in points:
                if not on_left_side(curr_point, next_point, other_point):
                    pos = False 
                    break
            if(pos):
                ch.append(next_point)
                curr_point = next_point
                vis[n-1-i] = True
                break
        ch_length += 1
        if(ch_length != len(ch)):
            break
    
    return ch

#Just a wrapper for the main function "make_hull"
def convex_hull(points):
    points = sorted(points)
    return make_hull(points)


#Serious stuff starts now
def make_hull(points):
    n = len(points)
    if(n <= 5):     #if number of points is less than 5, just bruteforce it
        return bruteforce_ch(points)
    left_half = points[:n//2]   #divide the set of points into two halves
    right_half = points[n//2:]
    left_ch = make_hull(left_half)  #recursively call the function on each part
    right_ch = make_hull(right_half)
    left_length = len(left_ch)
    right_length = len(right_ch)

    left_point_ind = left_ch.index(left_half[-1])   #getting right most point of left convex hull
    right_point_ind = right_ch.index(right_half[0])     #getting left most point of right convex hull
    #Constructing upper tangent
    while True:
        #next point means the next point on the convex hull in the counter clockwise direction
        # prev point means the previous point on convex hull in the clockwise direction 
        #right_problem means whether the line is passing through right convex hull
        right_problem, left_problem = False, False
        right_next, right_prev = (right_length+1+right_point_ind)%right_length, (right_length-1+right_point_ind)%right_length
        left_next, left_prev = (left_length+1+left_point_ind)%left_length, (left_length-1+left_point_ind)%left_length

        #checking if line goes through right convex hull and all points on left side
        if not (on_left_side(right_ch[right_point_ind], left_ch[left_point_ind], right_ch[right_prev])) or not on_left_side(right_ch[right_point_ind], left_ch[left_point_ind], right_ch[right_next]):
            right_problem = True
            right_point_ind = right_prev
            continue

        #checking if line goes through left convex hull and all points on left side
        if not (on_left_side(right_ch[right_point_ind],left_ch[left_point_ind], left_ch[left_next])) or not on_left_side(right_ch[right_point_ind],left_ch[left_point_ind], left_ch[left_prev]):
            left_point_ind = left_next
            left_problem = True
            continue

        #checking if line doesn't go through both hulls
        if(not right_problem and not left_problem):
            break
    
    upper_tangent_left = left_point_ind
    upper_tangent_right = right_point_ind

    left_point_ind = left_ch.index(left_half[-1])   #getting right most point of left ch (convex hull)
    right_point_ind = right_ch.index(right_half[0]) #getting left most point of right ch
    #repeat the same thing as before for lower tangent
    while True:
        #same definitions as before
        right_problem, left_problem = False, False
        right_next, right_prev = (right_length+1+right_point_ind)%right_length, (right_length-1+right_point_ind)%right_length
        left_next, left_prev = (left_length+1+left_point_ind)%left_length, (left_length-1+left_point_ind)%left_length

        #passing through right ch?
        if not (on_left_side(left_ch[left_point_ind], right_ch[right_point_ind], right_ch[right_next])) or not (on_left_side(left_ch[left_point_ind], right_ch[right_point_ind], right_ch[right_prev])):
            right_problem = True
            right_point_ind = right_next
            continue

        #passing through left ch?
        if not (on_left_side(left_ch[left_point_ind],right_ch[right_point_ind], left_ch[left_prev])) or not (on_left_side(left_ch[left_point_ind], right_ch[right_point_ind], left_ch[left_next])):
            left_point_ind = left_prev
            left_problem = True
            continue

        #not passing through 
        if(not right_problem and not left_problem):
            break

    lower_tangent_left = left_point_ind
    lower_tangent_right = right_point_ind

    #Now we have to combine the two convex hulls
    #We will combine it in following order
    #lower_tangent_right -> upper_tangent_right -> upper_tangent_left -> lower_tangent_left -> lower_tangent_right
    result = []
    i = lower_tangent_right
    while True:
        if(i >= right_length):
            i = 0
        result += [right_ch[i]]
        if(i == upper_tangent_right):
            break
        i += 1
    i = upper_tangent_left
    while True:
        if(i >= left_length):
            i = 0
        result += [left_ch[i]]
        if(i == lower_tangent_left):
            break
        i += 1

    return result


#Below part is for visualization
#You can modify it as per your wish
import random
import matplotlib.pyplot as plt
        
n = 50
x = [random.randint(1, n) for x in range(n)]
y = [random.randint(1, n) for x in range(n)]
points = zip(x, y)
points = set(points)
points = list(points)
points = sorted(points)
ch = convex_hull(points)
plt.scatter(x, y, color="orange")
x = [z[0] for z in ch] + [ch[0][0]]
y = [z[1] for z in ch] + [ch[0][1]]
plt.plot(x, y)
plt.show()