import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
CELL = (50,50)

class Board:
    def __init__(self):
        self.CELL = 50
        self.board = []
    def swap(self,colour,white,black):
        if colour == white:
            colour = black
        elif colour == black:
            colour = white
        return colour

    def create_board(self):
        black = (0,0,0)
        white = (255,255,255)
        colour = black
        y = 0
        for i in range(8):
            row = []
            x = 0
            for j in range(8):
                rect = pygame.Rect(x,y,self.CELL,self.CELL)
                row.append(rect)
                x+=self.CELL
            self.board.append(row)
            y +=self.CELL
        
        for row in self.board:
            colour = self.swap(colour,white,black)
            for block in row:
                pygame.draw.rect(screen,colour,block)
                colour = self.swap(colour,white,black)
    def make_pieces(self):
        images = [["002-pawn.png","001-rook.png","004-chess.png","005-queen.png","006-king.png"]["pawn.png","001-rook.png","004-chess.png","005-queen.png","006-king.png"]]
        co-ordinates = []
        self.pieces = []
        x = 0
        y = 0
        for colour in images:
            for image in colour:
                piece = Piece(image,x,y)
class Piece:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center =(self.x,self.y) )


def create_board():
    black = (0,0,0)
    white = (255,255,255)
    colour = black
    y = 0
    for i in range(8):
        row = []
        x = 0
        for j in range(8):
            rect = pygame.Rect(x,y,cell,cell)
            row.append(rect)
            x+=cell
        board.append(row)
        y +=cell
    
    for row in board:
        colour = swap(colour,white,black)
        for block in row:
            pygame.draw.rect(screen,colour,block)
            colour = swap(colour,white,black)
    



while True:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    create_board(CELL)
    pygame.display.update()