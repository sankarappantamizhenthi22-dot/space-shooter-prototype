import pygame

pygame.init()

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("space shooter")

player = pygame.image.load("C:/Users/USER/Downloads/game pygame/enemies.png")
player = pygame.transform.scale(player, (100, 100))

clock = pygame.time.Clock()


x, y = 100, 100

bullet_x = 0
bullet_y = 0
bullet_active = False
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = x + (player.get_width() // 2) 
                bullet_y = y
                bullets.append([bullet_x, bullet_y])
                

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5 

    screen.fill((0, 0, 0))

    for bullet in bullets:
                    bullet[1] -=7
                    pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 5, 10))
                    

                    if bullet_y < 0:
                        bullet_active  = False

                        for bullet in bullets[:]:
                           if bullet[1] < 0:
                                bullets.remove(bullet)

    screen.blit(player, (x, y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
            
