import pygame
import time
import sys
import asyncio 
from sudoku import Sudoku

pygame.init()
size = (650, 450)
font = pygame.font.SysFont(None, 43)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")
arr = [i for i in range(1, 10)]
grid = [
    [0,0,0,8,0,1,0,0,2],
    [2,0,1,0,3,0,6,0,4],
    [0,0,0,2,0,4,0,0,0],
    [8,0,9,0,0,0,1,0,6],
    [0,6,0,0,0,0,0,5,0],
    [7,0,2,0,0,0,4,0,9],
    [0,0,0,5,0,9,0,0,0],
    [9,0,4,0,8,0,7,0,5],
    [6,0,0,1,0,7,0,0,3]
]
# print(grid)

def sdk_runner():
    sdk = Sudoku(grid)
    # rectangles = [pygame.Rect]
    flag = 0
    playing = False
    usr_text = ''
    active = False
    ipx,ipy = -1,-1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : 
                x,y = event.pos 
                if (40<=x<=400) and (40<=y<=400) : 
                    active = True 
                    ipx,ipy = y//40 - 1,x//40 - 1
                    # active = True 
            if event.type == pygame.KEYDOWN:
                if active == True : 
                    usr_text = event.unicode
                    sdk.grid[ipx][ipy] = int(usr_text)
                
            # elif event.type = p
        # screen.fill((123,12,34))
        if not playing:
            screen.fill(pygame.Color("Black"))
            play = pygame.Rect(300,200,50,50)
            play_font = pygame.font.SysFont(None,55).render("Play",True,pygame.Color("Green"))
            play_font_rect = play_font.get_rect()
            play_font_rect.center = play.center 
            pygame.draw.rect(screen,(pygame.Color("Black")),play)
            screen.blit(play_font,play_font_rect)



            click, _, _ = pygame.mouse.get_pressed()
            if (click == 1):
                mouse = pygame.mouse.get_pos()
                if play.collidepoint(mouse):
                    playing = True
            pygame.display.update()
            asyncio.sleep(0)
        else:

            if not flag:

                screen.fill((pygame.Color("White")))
                solve_button = pygame.Rect(480, 80, 100, 75)
                solve_font = font.render("Solve", True, pygame.Color(("DarkGreen")))
                solve_font_Rect = solve_font.get_rect()
                solve_font_Rect.center = solve_button.center
                pygame.draw.rect(screen, (pygame.Color("LightGray")), solve_button)
                screen.blit(solve_font, solve_font_Rect)

                tile_size = 40
                tile_origin = (200 / 2 - (1.5 * tile_size),
                            200 / 2 - (1.5 * tile_size))
                tiles = []
                for i in range(9):
                    row = []
                    for j in range(9):

                        rect1 = pygame.Rect(
                            tile_origin[0] + j * tile_size,
                            tile_origin[1] + i * tile_size,
                            tile_size, tile_size
                        )
                        tile_width = 1
                        pygame.draw.rect(screen, pygame.Color("Black"), rect1, tile_width)
                        text = font.render(str(sdk.grid[i][j]), True, pygame.Color(
                            ('Black'))) if (sdk.grid[i][j]) != 0 else font.render(' ', True, pygame.Color(('Red')))

                        text_rect = text.get_rect(center=(
                            (tile_origin[0]+tile_size//2 + j*tile_size), (tile_origin[0]+tile_size//2+i*tile_size)))
                        screen.blit(text, text_rect)

                click, _, _ = pygame.mouse.get_pressed()
                # print(usr_text)
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    # print(mouse)
                    if solve_button.collidepoint(mouse):

                        # time.sleep(0.2)
                        sdk.solve(0, 0)

                        flag = 1



                    

            else:
                tile_size = 40
                tile_origin = (200 / 2 - (1.5 * tile_size),
                            200 / 2 - (1.5 * tile_size))
                tiles = []
                for i in range(9):
                    row = []
                    for j in range(9):

                        rect = pygame.Rect(
                            tile_origin[0] + j * tile_size,
                            tile_origin[1] + i * tile_size,
                            tile_size, tile_size
                        )
                        tile_width = 1
                        pygame.draw.rect(screen, (0, 0, 0), rect, tile_width)
                        text = font.render(str(sdk.grid[i][j]), True, pygame.Color(
                            ('DarkGreen'))) if sdk.grid[i][j] != 0 else font.render(' ', True, pygame.Color(('Red')))

                        text_rect = text.get_rect(center=(
                            (tile_origin[0]+tile_size//2 + j*tile_size), (tile_origin[0]+tile_size//2+i*tile_size)))
                        screen.blit(text, text_rect)

                reload_button = pygame.Rect(480, 180, 100, 75)
                reload_font = font.render("Reload", True, pygame.Color(("DarkGreen")))
                reload_font_Rect = reload_font.get_rect()
                reload_font_Rect.center = reload_button.center
                pygame.draw.rect(screen, (pygame.Color("LightGray")), reload_button)
                screen.blit(reload_font, reload_font_Rect)

                quit_button = pygame.Rect(480, 280, 100, 75)
                quit_font = font.render("Quit", True, pygame.Color(("DarkGreen")))
                quit_font_Rect = quit_font.get_rect()
                quit_font_Rect.center = quit_button.center
                pygame.draw.rect(screen, (pygame.Color("LightGray")), quit_button)
                screen.blit(quit_font, quit_font_Rect)

                click, _, _ = pygame.mouse.get_pressed()
                if click == 1:
                    mouse = pygame.mouse.get_pos()
                    if reload_button.collidepoint(mouse):
                        sdk.reload()
                        flag = 0
                    elif quit_button.collidepoint(mouse):
                        break

                
                # time.sleep(3)

            pygame.display.update()
            asyncio.sleep(0)
        
