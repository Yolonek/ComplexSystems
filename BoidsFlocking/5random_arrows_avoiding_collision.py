import sys
import pygame
import pymunk
import pymunk.pygame_util
from Flock import Flock


def main():
    running = True
    pygame.init()
    WIDTH, HEIGHT = 1920, 1080
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    velocity_scale = 200
    body_scale = 4

    space = pymunk.Space()

    number_of_bodies = 50
    flock = Flock(number_of_bodies, body_scale, space,
                  space_coordinates=(WIDTH, HEIGHT),
                  average_speed=velocity_scale,
                  protected_range=100,
                  avoid_factor=0.5)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if flock.speed_active:
                    flock.stop_boids()
                else:
                    flock.accelerate_boids()
        if flock.speed_active:
            flock.update_boid_parameter(
                check_boundaries=True,
                separation_active=True
            )

        window.fill((11, 11, 11))
        space.debug_draw(draw_options)
        pygame.display.update()
        space.step(dt)
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
