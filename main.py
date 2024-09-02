import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x_start = SCREEN_WIDTH / 2
    y_start = SCREEN_HEIGHT / 2
    player = Player(x_start, y_start)
    updatable = pygame.sprite.Group()
    updatable.add(player)
    drawable = pygame.sprite.Group()
    drawable.add(player)
    player.containers = (updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for player in drawable:
            player.draw(screen)
        for player in updatable:
            player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()