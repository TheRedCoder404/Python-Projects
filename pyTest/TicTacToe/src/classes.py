import pygame

class GameCross():
    crossSize = 0
    opacity = 255
    unclicked = [255, 0, 0, opacity]
    clicked = [0, 255, 0, opacity]
    colF1 = [255, 0, 0, opacity]
    colF2 = [255, 0, 0, opacity]
    colF3 = [255, 0, 0, opacity]
    colF4 = [255, 0, 0, opacity]
    colF5 = [255, 0, 0, opacity]
    colF6 = [255, 0, 0, opacity]
    colF7 = [255, 0, 0, opacity]
    colF8 = [255, 0, 0, opacity]
    colF9 = [255, 0, 0, opacity]
    xCol = [255, 255, 255, opacity]
    oCol = [255, 255, 255, opacity]
    hBoxCol = [255, 0, 0, opacity]
    xThickness = 30
    oThickness = 20
    oSize = 50

    drawHitBox = False


    def __init__(self, width: int, height: int, color: tuple = (255, 255, 255, 255), lineSize: int = 10) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.lineSize = lineSize

        if self.height < self.width:
            self.crossSize = int(self.height * 0.8)
        else:
            self.crossSize = int(self.width * 0.8)

        self.fieldSize = self.crossSize / 3
            
        self.posDict = {
            1: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 6)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 6))),
            2: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 2)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 6))),
            3: (int((self.width / 2) + (self.crossSize / 2) - (self.crossSize / 6)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 6))),
            4: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 6)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 2))),
            5: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 2)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 2))),
            6: (int((self.width / 2) + (self.crossSize / 2) - (self.crossSize / 6)), int((self.height / 2) - (self.crossSize / 2) + (self.crossSize / 2))),
            7: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 6)), int((self.height / 2) + (self.crossSize / 2) - (self.crossSize / 6))),
            8: (int((self.width / 2) - (self.crossSize / 2) + (self.crossSize / 2)), int((self.height / 2) + (self.crossSize / 2) - (self.crossSize / 6))),
            9: (int((self.width / 2) + (self.crossSize / 2) - (self.crossSize / 6)), int((self.height / 2) + (self.crossSize / 2) - (self.crossSize / 6)))
        }

        self.field1 = pygame.rect.Rect(int(self.posDict[1][0] - self.fieldSize / 2), int(self.posDict[1][1] - self.fieldSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize / 2)
        self.field2 = pygame.rect.Rect(int(self.posDict[2][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[2][1] - self.fieldSize / 2), self.fieldSize - self.lineSize, self.fieldSize - self.lineSize / 2)
        self.field3 = pygame.rect.Rect(int(self.posDict[3][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[3][1] - self.fieldSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize / 2)
        self.field4 = pygame.rect.Rect(int(self.posDict[4][0] - self.fieldSize / 2), int(self.posDict[4][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize)
        self.field5 = pygame.rect.Rect(int(self.posDict[5][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[5][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize, self.fieldSize - self.lineSize)
        self.field6 = pygame.rect.Rect(int(self.posDict[6][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[6][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize)
        self.field7 = pygame.rect.Rect(int(self.posDict[7][0] - self.fieldSize / 2), int(self.posDict[7][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize / 4)
        self.field8 = pygame.rect.Rect(int(self.posDict[8][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[8][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize, self.fieldSize - self.lineSize / 4)
        self.field9 = pygame.rect.Rect(int(self.posDict[9][0] - self.fieldSize / 2 + self.lineSize / 2), int(self.posDict[9][1] - self.fieldSize / 2 + self.lineSize / 2), self.fieldSize - self.lineSize / 2, self.fieldSize - self.lineSize / 4)

    def updateOpacity(self, opacity: int) -> None:
        self.unclicked = [255, 0, 0, opacity]
        self.clicked = [0, 255, 0, opacity]
        self.colF1 = [255, 0, 0, opacity]
        self.colF2 = [255, 0, 0, opacity]
        self.colF3 = [255, 0, 0, opacity]
        self.colF4 = [255, 0, 0, opacity]
        self.colF5 = [255, 0, 0, opacity]
        self.colF6 = [255, 0, 0, opacity]
        self.colF7 = [255, 0, 0, opacity]
        self.colF8 = [255, 0, 0, opacity]
        self.colF9 = [255, 0, 0, opacity]
        self.xCol = [255, 255, 255, opacity]
        self.oCol = [255, 255, 255, opacity]
        self.hBoxCol = [255, 0, 0, opacity]
    
    def drawCross(self, screen, usedp1: list, usedp2: list,) -> None:
        pygame.draw.line(screen, self.color, (int(((self.width / 2) - (self.crossSize / 2)) + (self.crossSize / 3)), int((self.height / 2) - (self.crossSize / 2))), (int(((self.width / 2) - (self.crossSize / 2)) + (self.crossSize / 3)), int((self.height / 2) + (self.crossSize / 2))), self.lineSize)
        pygame.draw.line(screen, self.color, (int(((self.width / 2) - (self.crossSize / 2)) + ((self.crossSize / 3) * 2)), int((self.height / 2) - (self.crossSize / 2))), (int(((self.width / 2) - (self.crossSize / 2)) + ((self.crossSize / 3) * 2)), int((self.height / 2) + (self.crossSize / 2))), self.lineSize)  
        pygame.draw.line(screen, self.color, (int((self.width / 2) - (self.crossSize / 2)), int(((self.height / 2) - (self.crossSize / 2)) + (self.crossSize / 3))), (int((self.width / 2) + (self.crossSize / 2)), int(((self.height / 2) - (self.crossSize / 2)) + (self.crossSize / 3))), self.lineSize)
        pygame.draw.line(screen, self.color, (int((self.width / 2) - (self.crossSize / 2)), int(((self.height / 2) - (self.crossSize / 2)) + ((self.crossSize / 3) * 2))), (int((self.width / 2) + (self.crossSize / 2)), int(((self.height / 2) - (self.crossSize / 2)) + ((self.crossSize / 3) * 2))), self.lineSize)
        
        self.updateOpacity(self.color[3])

        if self.drawHitBox:
            pygame.draw.rect(screen, self.hBoxCol, self.field1)
            pygame.draw.rect(screen, self.hBoxCol, self.field2)
            pygame.draw.rect(screen, self.hBoxCol, self.field3)
            pygame.draw.rect(screen, self.hBoxCol, self.field4)
            pygame.draw.rect(screen, self.hBoxCol, self.field5)
            pygame.draw.rect(screen, self.hBoxCol, self.field6)
            pygame.draw.rect(screen, self.hBoxCol, self.field7)
            pygame.draw.rect(screen, self.hBoxCol, self.field8)
            pygame.draw.rect(screen, self.hBoxCol, self.field9)

        for i in self.posDict:
            if i in usedp1:
                self.drawX(screen, self.posDict[i], self.xThickness)
            if i in usedp2:
                pygame.draw.circle(screen, self.oCol, self.posDict[i], ((self.crossSize / 6) - self.oThickness), self.oThickness)

    def getfield(self, mousepos: tuple) -> int:
        if self.field1.collidepoint(mousepos):
            self.colF1 = self.clicked
            return 1
        elif self.field2.collidepoint(mousepos):
            self.colF2 = self.clicked
            return 2
        elif self.field3.collidepoint(mousepos):
            self.colF3 = self.clicked
            return 3
        elif self.field4.collidepoint(mousepos):
            self.colF4 = self.clicked
            return 4
        elif self.field5.collidepoint(mousepos):
            self.colF5 = self.clicked
            return 5
        elif self.field6.collidepoint(mousepos):
            self.colF6 = self.clicked
            return 6
        elif self.field7.collidepoint(mousepos):
            self.colF7 = self.clicked
            return 7
        elif self.field8.collidepoint(mousepos):
            self.colF8 = self.clicked
            return 8
        elif self.field9.collidepoint(mousepos):
            self.colF9 = self.clicked
            return 9
        
    def drawX(self, screen, xy: tuple, xThick: int) -> None:
        pygame.draw.line(screen, self.xCol, (xy[0] - (self.crossSize / 6) + xThick, xy[1] - (self.crossSize / 6) + xThick), (xy[0] + (self.crossSize / 6) - xThick, xy[1] + (self.crossSize / 6) - xThick), xThick)
        pygame.draw.line(screen, self.xCol, (xy[0] - (self.crossSize / 6) + xThick, xy[1] + (self.crossSize / 6) - xThick), (xy[0] + (self.crossSize / 6) - xThick, xy[1] - (self.crossSize / 6) + xThick), xThick)
