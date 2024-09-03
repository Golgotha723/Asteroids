import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.display.set_caption('Asteroids')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 
    score = 0
    large_count = 0
    medium_count = 0
    small_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print(f"Your score: {score}")
                print(f"Large asteroids Destroyed: {large_count}")
                print(f"Medium asteroids Destroyed: {medium_count}")
                print(f"Small asteroids Destroyed: {small_count}")
                print("Game Over!")
                return
            for shot in shots:
                if shot.collision(asteroid) == True:
                    if asteroid.radius == ASTEROID_MAX_RADIUS:
                        large_count += 1
                        score += 150
                    if asteroid.radius < ASTEROID_MAX_RADIUS and asteroid.radius > ASTEROID_MIN_RADIUS:
                        medium_count += 1
                        score += 100
                    if asteroid.radius == ASTEROID_MIN_RADIUS:
                        small_count += 1
                        score += 50
                    shot.kill()
                    asteroid.split()
        


        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()