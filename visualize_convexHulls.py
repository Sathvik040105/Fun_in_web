import pygame
import time
pygame.init()

#Fixed variables
FPS = 10
WIDTH, HEIGHT = 700, 700
RADIUS = 5
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Essentials
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Convex hull")
clock = pygame.time.Clock()
run = True

#Dynamic variables
points = []

#Functions
def draw_points():  # displays the points stored in "points" on to the screen
    for center in points:
        pygame.draw.circle(screen, RED, center, RADIUS)

def on_left_side(p1, p2, p):    # Returns true if the ray p1-p lies towards left of p1-p2
    ans = (p2[0]-p1[0])*(p[1]-p1[1])-(p2[1]-p1[1])*(p[0]-p1[0])
    if(ans >= 0):
        return True
    else:
        return False

def convex_hull(points):    # Returns the convex hull using "Gift wrapping algorithm"
    if(len(points) == 1):
        return points
    hull = []
    points  = sorted(points)
    hull.append(points[0])
    while(len(hull) == 1 or hull[0] != hull[-1]):
        curr = hull[-1]
        for next in points:
            if next == curr:
                continue
            pos = True
            for x in points:
                if(not on_left_side(curr, next, x)):
                    pos = False
                    break
            if(pos):
                hull.append(next)
                break
    return hull

def draw_hull():    # Draws the convex hull on the screen
    if(len(points) != 0):
        hull = convex_hull(points)
        n = len(hull)
        for i in range(n-1):
            pygame.draw.line(screen, GREEN, hull[i], hull[i+1])

while run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                points.append(event.pos)

    draw_points()
    draw_hull()
    pygame.display.update()

pygame.quit()
    