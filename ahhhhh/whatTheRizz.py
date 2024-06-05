import pymunk
import pymunk.pygame_util
import pygame

# Initialize pygame and pymunk
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, -900)

# Add a static floor
floor = pymunk.Segment(space.static_body, (0, 50), (600, 50), 5)
floor.friction = 0.5
space.add(floor)

# Function to add a ball
def add_ball(space, position):
    mass = 1
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.friction = 0.5
    space.add(body, shape)

# Add some balls
for _ in range(5):
    add_ball(space, (300, 300))

# Simulation loop
draw_options = pymunk.pygame_util.DrawOptions(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)
    space.step(1/50.0)
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
