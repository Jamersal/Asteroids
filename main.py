import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    clock = pygame.time.Clock()
    dt = 0

    while True: 
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
       
         

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        dt = clock.tick(60) / 1000
        
                


if __name__ == "__main__":
    main()
