# double_pendulum.py
# AUTHOR: CALEB M. LEES
# DATE: 5 July 2020

import math
import pygame
from collections import deque
pygame.init()

# global variables
WIDTH, HEIGHT = 900, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
G = 0.1

# gravity simulations
#   Earth: 0.100
#   Moon: 0.0165
#   Jupiter: 0.253

# pendulum configuration (angles in radians)
r1 = 150
r2 = 150
m1 = 10
m2 = 10
theta1 = math.pi
theta2 = math.pi/2
theta1_v = 0
theta2_v = 0
# trail = []
trail1 = deque(maxlen=500)
trail2 = deque(maxlen=500)


# cool initial positions:
#   theta1 = pi/2, theta2 = pi
#   theta1 = 3, theta2 = 1
#   theta1 = pi, theta2 = pi/2

# window configuration
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Pendulum")
background_color = WHITE
clock = pygame.time.Clock()


# translate point to relative center
def translate(x1, y1):
    new_x, new_y = x1 + int(WIDTH / 2), y1 + int(HEIGHT / 5)
    return new_x, new_y


def draw():
    x1, y1 = int(r1 * math.sin(theta1)), int(r1 * math.cos(theta1))
    x2, y2 = int(x1 + r2 * math.sin(theta2)), int(y1 + r2 * math.cos(theta2))

    trail1.append((x1, y1))
    trail2.append((x2, y2))
    for i in trail1:
        pygame.draw.rect(window, RED, [translate(i[0], i[1]), (2, 2)])
    for i in trail2:
        pygame.draw.rect(window, BLUE, [translate(i[0], i[1]), (2, 2)])

    # draw pendulum and UI divider
    pygame.draw.line(window, BLACK, translate(0, 0), translate(x1, y1), 2)
    pygame.draw.circle(window, BLACK, translate(x1, y1), m1)
    pygame.draw.line(window, BLACK, translate(x1, y1), translate(x2, y2), 2)
    pygame.draw.circle(window, BLACK, translate(x2, y2), m2)
    pygame.draw.line(window, BLACK, (0, HEIGHT - 70), (WIDTH, HEIGHT - 70), 1)
    pygame.draw.line(window, BLACK, (760, HEIGHT - 70), (760, HEIGHT), 1)

    # trail animation controls
    pygame.draw.rect(window, GRAY, (5, HEIGHT - 22, 90, 20))
    font1 = pygame.font.SysFont('monospace', 14)
    surface = font1.render('CLEAR PATH', False, BLACK)
    window.blit(surface, (10, HEIGHT - 20))

    # mass 1 controls
    pygame.draw.circle(window, BUTTON_PLUS_1, (220, HEIGHT - 41), 8)
    pygame.draw.circle(window, BUTTON_MINUS_1, (220, HEIGHT - 21), 8)
    font2 = pygame.font.SysFont('monospace', 16)
    surface = font2.render('mass 1:', False, BLACK)
    window.blit(surface, (120, HEIGHT - 50))
    surface = font2.render('+', False, BLACK)
    window.blit(surface, (215, HEIGHT - 50))
    surface = font2.render('-', False, BLACK)
    window.blit(surface, (215, HEIGHT - 30))
    surface = font2.render(str(m1), False, BLACK)
    window.blit(surface, (130, HEIGHT - 30))

    # mass 2 controls
    pygame.draw.circle(window, BUTTON_PLUS_2, (380, HEIGHT - 41), 8)
    pygame.draw.circle(window, BUTTON_MINUS_2, (380, HEIGHT - 21), 8)
    surface = font2.render('mass 2:', False, BLACK)
    window.blit(surface, (280, HEIGHT - 50))
    surface = font2.render('+', False, BLACK)
    window.blit(surface, (375, HEIGHT - 50))
    surface = font2.render('-', False, BLACK)
    window.blit(surface, (375, HEIGHT - 30))
    surface = font2.render(str(m2), False, BLACK)
    window.blit(surface, (290, HEIGHT - 30))

    # length 1 controls
    pygame.draw.circle(window, BUTTON_PLUS_2, (540, HEIGHT - 41), 8)
    pygame.draw.circle(window, BUTTON_MINUS_2, (540, HEIGHT - 21), 8)
    surface = font2.render('len 1:', False, BLACK)
    window.blit(surface, (440, HEIGHT - 50))
    surface = font2.render('+', False, BLACK)
    window.blit(surface, (535, HEIGHT - 50))
    surface = font2.render('-', False, BLACK)
    window.blit(surface, (535, HEIGHT - 30))
    surface = font2.render(str(r1), False, BLACK)
    window.blit(surface, (450, HEIGHT - 30))

    # length 2 controls
    pygame.draw.circle(window, BUTTON_PLUS_2, (700, HEIGHT - 41), 8)
    pygame.draw.circle(window, BUTTON_MINUS_2, (700, HEIGHT - 21), 8)
    surface = font2.render('len 2:', False, BLACK)
    window.blit(surface, (600, HEIGHT - 50))
    surface = font2.render('+', False, BLACK)
    window.blit(surface, (695, HEIGHT - 50))
    surface = font2.render('-', False, BLACK)
    window.blit(surface, (695, HEIGHT - 30))
    surface = font2.render(str(r2), False, BLACK)
    window.blit(surface, (610, HEIGHT - 30))

    # gravity controls
    pygame.draw.circle(window, BUTTON_PLUS_G, (880, HEIGHT - 41), 8)
    pygame.draw.circle(window, BUTTON_MINUS_G, (880, HEIGHT - 21), 8)
    surface = font2.render('gravity:', False, BLACK)
    window.blit(surface, (780, HEIGHT - 50))
    surface = font2.render('+', False, BLACK)
    window.blit(surface, (875, HEIGHT - 50))
    surface = font2.render('-', False, BLACK)
    window.blit(surface, (875, HEIGHT - 30))
    surface = font2.render(str(round(G, 2)), False, BLACK)
    window.blit(surface, (790, HEIGHT - 30))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mass 1 buttons
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    if (212 <= mouse_x <= 228) and (HEIGHT-49 <= mouse_y <= HEIGHT-34) and pygame.mouse.get_pressed()[0] == 1:
        BUTTON_PLUS_1 = (5, 148, 0)
        m1 = m1 + 1
    else:
        BUTTON_PLUS_1 = (6, 183, 0)
    if (212 <= mouse_x <= 228) and (HEIGHT-29 <= mouse_y <= HEIGHT - 14) and pygame.mouse.get_pressed()[0] == 1 and m1 > 1:
        BUTTON_MINUS_1 = (181, 0, 0)
        m1 = m1 - 1
    else:
        BUTTON_MINUS_1 = (226, 0, 0)

    # mass 2 buttons
    if (372 <= mouse_x <= 388) and (HEIGHT-49 <= mouse_y <= HEIGHT-34) and pygame.mouse.get_pressed()[0] == 1:
        BUTTON_PLUS_2 = (5, 148, 0)
        m2 = m2 + 1
    else:
        BUTTON_PLUS_2 = (6, 183, 0)
    if (372 <= mouse_x <= 388) and (HEIGHT-29 <= mouse_y <= HEIGHT - 14) and pygame.mouse.get_pressed()[0] == 1 and m2 > 1:
        BUTTON_MINUS_2 = (181, 0, 0)
        m2 = m2 - 1
    else:
        BUTTON_MINUS_2 = (226, 0, 0)

    # length 1 buttons
    if (532 <= mouse_x <= 548) and (HEIGHT - 49 <= mouse_y <= HEIGHT - 34) and pygame.mouse.get_pressed()[0] == 1:
        BUTTON_PLUS_2 = (5, 148, 0)
        r1 = r1 + 1
    else:
        BUTTON_PLUS_2 = (6, 183, 0)
    if (532 <= mouse_x <= 548) and (HEIGHT - 29 <= mouse_y <= HEIGHT - 14) and pygame.mouse.get_pressed()[0] == 1 and r1 > 1:
        BUTTON_MINUS_2 = (181, 0, 0)
        r1 = r1 - 1
    else:
        BUTTON_MINUS_2 = (226, 0, 0)

    # length 2 buttons
    if (692 <= mouse_x <= 708) and (HEIGHT - 49 <= mouse_y <= HEIGHT - 34) and pygame.mouse.get_pressed()[0] == 1:
        BUTTON_PLUS_2 = (5, 148, 0)
        r2 = r2 + 1
    else:
        BUTTON_PLUS_2 = (6, 183, 0)
    if (692 <= mouse_x <= 708) and (HEIGHT - 29 <= mouse_y <= HEIGHT - 14) and pygame.mouse.get_pressed()[0] == 1 and r2 > 1:
        BUTTON_MINUS_2 = (181, 0, 0)
        r2 = r2 - 1
    else:
        BUTTON_MINUS_2 = (226, 0, 0)

    # gravity buttons
    if (872 <= mouse_x <= 888) and (HEIGHT-49 <= mouse_y <= HEIGHT-34) and pygame.mouse.get_pressed()[0] == 1:
        BUTTON_PLUS_G = (5, 148, 0)
        G += 0.001
    else:
        BUTTON_PLUS_G = (6, 183, 0)
    if (872 <= mouse_x <= 888) and (HEIGHT-29 <= mouse_y <= HEIGHT - 14) and pygame.mouse.get_pressed()[0] == 1 and m2 > 1:
        BUTTON_MINUS_G = (181, 0, 0)
        G -= 0.001
    else:
        BUTTON_MINUS_G = (226, 0, 0)

    # clear trail button
    if (5 <= mouse_x <= 95) and (HEIGHT-22 <= mouse_y <= HEIGHT-2) and pygame.mouse.get_pressed()[0] == 1:
        GRAY = (152, 152, 152)
        # trail = []
        trail1.clear()
        trail2.clear()
    else:
        GRAY = (183, 183, 183)

    # solution for acceleration
    num_1a = -G*(2*m1 + m2)*math.sin(theta1) - m2*G*math.sin(theta1 - 2*theta2)
    num_1b = -2*math.sin(theta1 - theta2)*m2*(theta2_v*theta2_v*r2 + theta1_v*theta1_v*r1*math.cos(theta1 - theta2))
    num_1 = num_1a + num_1b
    den_1 = r1*(2*m1 + m2 - m2*math.cos(2*theta1 - 2*theta2))
    num_2a = 2*math.sin(theta1 - theta2)
    num_2b = theta1_v*theta1_v*r1*(m1 + m2) + G*(m1 + m2)*math.cos(theta1) + theta2_v*theta2_v*r2*m2*math.cos(theta1 - theta2)
    num_2 = num_2a * num_2b
    den_2 = r2*(2*m1 + m2 - m2*math.cos(2*theta1 - 2*theta2))

    theta1_a = num_1 / den_1
    theta2_a = num_2 / den_2

    # relate acceleration to velocity and position
    theta1_v += theta1_a
    theta2_v += theta2_a
    theta1 += theta1_v
    theta2 += theta2_v

    window.fill(background_color)
    draw()

    pygame.display.update()

    clock.tick(144)

