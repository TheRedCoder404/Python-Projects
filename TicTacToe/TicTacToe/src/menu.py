import pygame

pygame.font.init()

class Menu:
    winscreenFont = pygame.font.SysFont('Comic Sans MS', 30)

    def __init__(self, player1name: str = None, player2name: str = None, player1highscore: int = 0, player2highscore: int = 0) -> None:
        self.p1name = player1name
        self.p2name = player2name
        self.p1score = 0
        self.p2score = 0
        self.p1win = False
        self.p2win = False
        self.p1highscore = player1highscore
        self.p2highscore = player2highscore

    def menuScreen(self = None) -> None:
        pass

    def winScreen(self, surface):
        if self.p1win:
            winText = self.winscreenFont.render(f"{self.p1name} has won", False, (255, 255, 255))
            surface.blit(winText, (200, 200))
        elif self.p2win:
            winText = self.winscreenFont.render(f"{self.p2name} has won", False, (255, 255, 255))
            surface.blit(winText, (200, 200))
