import pygame
import classes
import menu

pygame.init()
pygame.font.init()

pygame.display.set_caption("TicTacToe")

screen_width = 800
screen_height = 600

opacity = 255

fps = 30
timer = pygame.time.Clock()

TRANSPARENCY = pygame.USEREVENT + 1
pygame.time.set_timer(TRANSPARENCY, 50)

winCons = {'winCon1': [1, 2, 3], 'winCon2': [4, 5, 6], 'winCon3': [7, 8, 9], 'winCon4': [1, 4, 7], 'winCon5': [2, 5, 8], 'winCon6': [3, 6, 9], 'winCon7': [1, 5, 9], 'winCon8': [3, 5, 7]}
usedp1 = []
usedp2 = []

turnp1 = True
p1win = False
p2win = False

cross = classes.GameCross(screen_width, screen_height, color=(255, 255, 255, opacity))
gameMenu = menu.Menu("Affe", "Maski")

screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)


main = True
while main:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    screen.blit(surface, (0, 0))
    cross.drawCross(surface, usedp1, usedp2)

    if opacity < 130:
        gameMenu.winScreen(surface)
    for i in winCons:
        winCon = winCons[i]
        if winCon[0] in usedp1 and winCon[1] in usedp1 and winCon[2] in usedp1:
            p1win = True
            gameMenu.p1win = True
        elif winCon[0] in usedp2 and winCon[1] in usedp2 and winCon[2] in usedp2:
            p2win = True
            gameMenu.p2win = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            break

        elif event.type == TRANSPARENCY:
            if (p1win or p2win) and opacity > 120:
                opacity -= 10
                cross.color = (255, 255, 255, opacity)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            field = cross.getfield(mousePos)
            if field != None and not (p1win or p2win):
                if turnp1:
                    if not (field in usedp1 or  field in usedp2):
                        usedp1.append(field)
                        turnp1 = False
                else:
                    if not (field in usedp1 or  field in usedp2):
                        usedp2.append(field)
                        turnp1 = True

    pygame.display.flip()

pygame.display.quit()
pygame.quit()
