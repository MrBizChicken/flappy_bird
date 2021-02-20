from constants import *
import pygame
import bird
import pipe
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()


pipe = pipe.Pipe()
bird = bird.Bird()


bird_group.add(bird)
pipe_group.add(pipe)






def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird.flap()                   

        draw()
        update()

    pygame.quit()




def draw():
    surface.fill((0, 0, 0))
    bird_group.draw(surface)
    pipe_group.draw(surface)



    pygame.display.flip()


def update():
    bird_group.update()
    pipe_group.update()








if __name__ == "__main__":
    main()
