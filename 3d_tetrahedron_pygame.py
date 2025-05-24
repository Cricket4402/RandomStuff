import pygame
import numpy 
import math

window = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

tetra = [n for n in range(4)]
tetra[0] = [[0],[1],[0]]
tetra[1] = [[0],[0],[1]]
tetra[2] = [[1],[0],[0]]
tetra[3] = [[-1],[0],[0]]

projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]


def connect_points (i, j, points):
    pygame.draw.line(window, (0, 255, 255), (points[i][0], points[i][1]),(points[j][0], points[j][1]))

def multiply_m(a,b):
    return numpy.matmul(a, b)

scale = 200
offset = 400

theta_x = theta_y = theta_z = 0

# window loop
while True:
    clock.tick(60)
    window.fill((0,0,0))

    # Rotation matrices
    rotation_matrix_x = [
    [1, 0, 0],
    [0, math.cos(theta_x), -math.sin(theta_x)],
    [0, math.sin(theta_x), math.cos(theta_x)]
    ]

    rotation_matrix_y = [
    [math.cos(theta_y), 0, math.sin(theta_y)],
    [0, 1, 0],
    [-math.sin(theta_y), 0, math.cos(theta_y)]
    ]

    rotation_matrix_z = [
    [math.cos(theta_z), -math.sin(theta_z), 0],
    [math.sin(theta_z), math.cos(theta_z), 0],
    [0, 0, 1]
    ]

    theta_x += 0.01
    theta_y += 0.005
    theta_y += 0.01

    points = [0 for _ in range(len(tetra))]
    i = 0

    for point in tetra:
        temp_rotate_x = multiply_m(rotation_matrix_x, point)
        temp_rotate_y = multiply_m(rotation_matrix_y, temp_rotate_x)
        temp_rotate_z = multiply_m(rotation_matrix_z, temp_rotate_y)

        point_2d = multiply_m(projection_matrix, temp_rotate_z)

        x = point_2d[0][0] * scale + offset
        y = point_2d[1][0] * scale + offset
        
        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (0,255,255), (x,y), 4)
    
    connect_points(0, 1, points)
    connect_points(0, 2, points)
    connect_points(0, 3, points)
    connect_points(1, 2, points)
    connect_points(1, 3, points)
    connect_points(2, 3, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            theta_x = theta_y = theta_z = 0

    pygame.display.update()

