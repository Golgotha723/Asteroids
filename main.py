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

    text_font = pygame.font.SysFont(None, 30)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 
    raise_lives = 10000
    lives = 3
    score = 0
    time_score = 0
    large_count = 0
    medium_count = 0
    small_count = 0
    invincible_time = 0

    while True:
        screen.fill("black")
        if lives > 0:
            time_score += 1
            draw_text(f"Lives: {lives}", text_font, "white", 0, 0)
            draw_text(f"Score: {score}", text_font, "white", 0, 25)
            if score >= raise_lives:
                lives += 1
                asteroid_field.speed_increase()
                raise_lives += 10000 

        if lives <= 0:
            player.kill()
            draw_text("Game Over!", text_font, "white", 570, 300)
            draw_text(f"Your score: {score}", text_font, "white", 555, 325)
            draw_text(f"Large asteroids Destroyed: {large_count}", text_font, "white", 490, 350)
            draw_text(f"Medium asteroids Destroyed: {medium_count}", text_font, "white", 480, 375)
            draw_text(f"Small asteroids Destroyed: {small_count}", text_font, "white", 490, 400)
            draw_text("Press Enter to Exit", text_font, "white", 545, 425)
            if pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                return

        if score >= raise_lives:
            if lives > 0:
                lives += 1
                asteroid_field.speed_increase()
                raise_lives += 10000
            
        if invincible_time > 0:
            player.b_color()
            invincible_time -= 1

        if time_score == 60:
            score += 1
            time_score = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if invincible_time == 0:
                player.r_color()
                if player.collision(asteroid) == True:
                    lives -= 1
                    invincible_time += 120
                        
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
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()