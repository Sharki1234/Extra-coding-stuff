import pygame
pygame.init()
import time

WIDTH = 510
HEIGHT = 600

BOARD_DIMENSIONS = (510,500)
CELLS= (5,5)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Board:
    def __init__(self):
        self.recs = []
        self.coloured = []
        self.button = pygame.Rect(155,510,200,80)

    def board(self, board_dimensions:tuple, cells:tuple):
        cell_w = ((board_dimensions[0]-10) // cells[0])-10
        cell_h = board_dimensions[1] // cells[1]-10
        self.colour = []
        y = 10
        for row_i in range(cells[1]):      
            x = 10
            row = []
            col_row = []
            for col_i in range(cells[0]):  
                rec = pygame.Rect(x, y, cell_w, cell_h)
                row.append(rec)
                x += cell_w+10
                col_row.append((0,0,0))
            self.colour.append(col_row)
            self.recs.append(row)
            y += cell_h+10
        

           

            

    def draw_board(self, colour:tuple):
        for i  in range(len(self.recs)):
            for j in range(len(self.recs[i])):
                pygame.draw.rect(screen, self.colour[i][j], self.recs[i][j])
        pygame.draw.rect(screen,colour,self.button)
        

    def colour_change(self,colour:tuple,pos):
        for i in range(len(self.recs)):
            for j in range(len(self.recs[i])):
                if self.recs[i][j].collidepoint(pos):
                    if self.colour[i][j] == (0,0,0):
                        self.colour[i][j] = colour
                        self.coloured.append(self.recs[i][j])
                    else:
                        self.colour[i][j] = (0,0,0)
                        self.coloured.remove(self.recs[i][j])
    def index(self,rec):
        for i in range(len(self.recs)):
            for j in range(len(self.recs[i])):
                if self.recs[i][j] == rec:
                    return i,j
    def check_neighbours(self,rec):
        i,j = self.index(rec)
        neighbours = []
        total = 0
        for di in range(-1,2):
            for dj in range(-1,2):
                if di == 0 and dj == 0:
                    continue
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(self.recs) and 0 <= nj < len(self.recs[0]):
                    if self.recs[ni][nj] in self.coloured:
                        total += 1
        return total

       
    

    def fate(self):
            self.deaths = []
            self.born = []
            for row in self.recs:
                for rec in row:
                    total = self.check_neighbours(rec)
                    if rec in self.coloured:
                        if total<=1 or total>=4:
                            self.deaths.append(rec)
                    else:
                        if total==3:
                            self.born.append(rec)
    def execute(self):
        for ghost in self.deaths:
            i,j = self.index(ghost)
            self.colour[i][j] = (0,0,0)
            self.coloured.remove(ghost)
        for spawn in self.born:
            i,j = self.index(spawn)
            self.colour[i][j] = (255,255,0) 
            self.coloured.append(spawn)
    

                    

board = Board()
board.board(BOARD_DIMENSIONS, CELLS)

clock = pygame.time.Clock()

UPDATE_TIME = 1500
last_update = pygame.time.get_ticks()

running = False

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.colour_change(pos = event.pos,colour=(255,255,0))
            if board.button.collidepoint(event.pos):
                running = True
    now = pygame.time.get_ticks()

    if now - last_update >= UPDATE_TIME and running:
        if board.coloured:
            board.fate()
            board.execute()
            last_update = now
                    
    board.draw_board((0,0,0))
    clock.tick(60)
    pygame.display.update()
