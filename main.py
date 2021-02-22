from constants import *
import pygame, random
import bird
import pipe
import cloud

pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

bird_group = pygame.sprite.Group()
pipes_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()
amount_of_clouds = 1



bird = bird.Bird()



bird_group.add(bird)

for i in range(amount_of_clouds):

    cloud_group.add(cloud.Cloud())


pipes_group.add(pipe.Top_pipe(GAME_WIDTH, pipes_group))
pipes_group.add(pipe.Top_pipe(GAME_WIDTH + GAME_WIDTH // 2, pipes_group))
pipes_group.add(pipe.Top_pipe(GAME_WIDTH * 2, pipes_group))













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
    surface.fill((200, 200, 200))
    bird_group.draw(surface)
    pipes_group.draw(surface)
    cloud_group.draw(surface)



    pygame.display.flip()


def update():
    bird_group.update(pipes_group)
    pipes_group.update()
    cloud_group.update()








if __name__ == "__main__":
    main()
