import pygame
from pygame.locals import *
from time import sleep
import game_logic as game
import ai
GRAVITY = 0.01
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
def draw_board(screen,board):
    pygame.draw.rect(screen, (50, 50, 255), (20, 50, 360, 280))
    for i in range(0,len(board)):
        for x in range(0,len(board[i])):
            tile_color = (255,255,255)
            if board[i][x]==game.RED:
                tile_color = (255,0,0)
            elif board[i][x]==game.BLACK:
                tile_color = (0,0,0)
            pygame.draw.circle(screen,tile_color,(int(45+x*360/7),int(300-i*300/7)),20)


def animate_move(screen,board,move,team,stage):
    # Returns whether animation is finished
    draw_board(screen,board)
    finished = False
    this_color = (255,0,0)
    dest = int(300-game.get_y_of(board,move)*300/7)
    if team==game.BLACK:
        this_color = (0,0,0)
    y = int(0.5*GRAVITY*stage*stage)
    if y >= dest:
        y=dest
    pygame.draw.circle(screen,this_color,(int(45+move*360/7),y),20)
    return y==dest


def play_pygame_ai(p1ai, p2ai,fps=500):
    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode((400,400))
    running = True
    p1 = p1ai(game.RED)
    p2 = p2ai(game.BLACK)
    board = game.initialize_board()
    pending_move = p1.make_move(board)
    move_completed = False
    turn = 1
    time = 0
    winner = -1
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        if winner != -1:
            if winner==1:
                text = "Red Wins"
            elif winner==2:
                text = "Black Wins"
            else:
                text = "It's a Tie"
            text = font.render(text,True,(100,150,150))
            text_width = text.get_rect().width
            draw_board(screen, board)
            screen.blit(text,(int(200-text_width/2),150))
            pygame.display.update()
        else:
            move_completed = animate_move(screen, board, pending_move, turn, time)
            time += 1
            pygame.display.flip()
            if move_completed:
                board, _ = game.make_move(board, pending_move, turn)
                end_check = game.check_game_end(board)
                if end_check!=-1:
                    winner = end_check
                else:
                    time=0
                    if turn==1:
                        turn=2
                        pending_move = p2.make_move(board)
                    elif turn==2:
                        turn=1
                        pending_move = p1.make_move(board)
                    if pending_move != -1 and not game.is_valid_move(board,pending_move):
                        print(pending_move)
                        winner = 2 if turn == 1 else 1
                    move_completed=False


def to_screen(x,y):
    return int(45+x*360/7), int(300-y*300/7)


def play_pygame_players(fps=500):
    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode((400, 400))
    running = True
    board = game.initialize_board()
    pending_move = -1
    turn = 1
    time = 0
    winner = -1
    while running:
        tick = clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        if winner != -1:
            if winner==1:
                text = "Red Wins"
            elif winner==2:
                text = "Black Wins"
            else:
                text = "It's a Tie"
            text = font.render(text,True,(100,150,150))
            text_width = text.get_rect().width
            draw_board(screen, board)
            screen.blit(text,(int(200-text_width/2),150))
            pygame.display.update()
        elif pending_move==-1:
            draw_board(screen,board)
            selected_slot = -1
            mp = pygame.mouse.get_pos()
            if 0 < mp[1] < 400:
                for i in range(0,7):
                    if 25+i*360/7 <= mp[0] <= 65+i*360/7:
                        if game.get_y_of(board,i)==-1:
                            break
                        selected_slot = i
                        pos = to_screen(i,game.get_y_of(board,i))
                        pygame.draw.circle(screen,(255,255,0),pos,20)
                        pygame.draw.circle(screen, (255, 255, 255), pos, 14)
                        break
            if pygame.mouse.get_pressed()[0] and selected_slot != -1:
                pending_move = selected_slot
            pygame.display.flip()
        else:
            done = animate_move(screen,board,pending_move,turn,time)
            time+=1
            if done:
                board, _ = game.make_move(board,pending_move,turn)
                winner = game.check_game_end(board)
                pending_move=-1
                turn = 1 if turn==2 else 2
                time=0
            pygame.display.flip()

def play_pygame_1ai(ai,ai_turn=1,fps=500):
    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode((400, 400))
    running = True
    board = game.initialize_board()
    pending_move = -1
    turn = ai_turn
    time = 0
    ai = ai(ai_turn)
    winner = -1
    if ai_turn==1:
        pending_move = ai.make_move(board)
    while running:
        tick = clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        if winner != -1:
            if winner == 1:
                text = "Red Wins"
            elif winner == 2:
                text = "Black Wins"
            else:
                text = "It's a Tie"
            text = font.render(text, True, (100, 150, 150))
            text_width = text.get_rect().width
            draw_board(screen, board)
            screen.blit(text, (int(200 - text_width / 2), 150))
            pygame.display.update()
        elif pending_move == -1:
            draw_board(screen, board)
            selected_slot = -1
            mp = pygame.mouse.get_pos()
            if 0 < mp[1] < 400:
                for i in range(0, 7):
                    if 25 + i * 360 / 7 <= mp[0] <= 65 + i * 360 / 7:
                        if game.get_y_of(board, i) == -1:
                            break
                        selected_slot = i
                        pos = to_screen(i, game.get_y_of(board, i))
                        pygame.draw.circle(screen, (255, 255, 0), pos, 20)
                        pygame.draw.circle(screen, (255, 255, 255), pos, 14)
                        break
            if pygame.mouse.get_pressed()[0] and selected_slot != -1:
                pending_move = selected_slot
            pygame.display.flip()
        else:
            done = animate_move(screen, board, pending_move, turn, time)
            time += 1
            if done:
                board, _ = game.make_move(board, pending_move, turn)
                winner = game.check_game_end(board)
                pending_move = -1
                time = 0
                turn = 1 if turn==2 else 2
                if turn==ai_turn:
                    pending_move=ai.make_move(board)
            pygame.display.flip()


def play_print(p1ai,p2ai,pause_after_p1=False,pause_after_p2=False):
    p1 = p1ai(game.RED)
    p2 = p2ai(game.BLACK)
    turn = 0
    board = game.initialize_board()
    game_end = -1
    while game_end == -1:
        game.print_board(board)
        print("")
        if turn % 2 == 0:
            move = p1.make_move(board)
            if not game.is_valid_move(board,move):
                game_end = game.BLACK
                print("Red attempted an invalid move.")
                break
            board, _ = game.make_move(board,move,game.RED)
            if pause_after_p1:
                sleep(1)
        else:
            move = p2.make_move(board)
            if not game.is_valid_move(board,move):
                game_end=game.RED
                print("Black attempted an invalid move.")
                break
            board, _ = game.make_move(board,move,game.BLACK)
            if pause_after_p2:
                sleep(1)
        turn += 1
        game_end = game.check_game_end(board)
    if game_end == game.RED:
        print("Red Wins")
    elif game_end == game.BLACK:
        print("Black Wins")
    else:
        print("It's a tie.")
    game.print_board(board)
    return game_end

def play_normal(p1ai,p2ai,print_winner=False):
    p1 = p1ai(game.RED)
    p2 = p2ai(game.BLACK)
    turn = 0
    board = game.initialize_board()
    game_end = -1
    while game_end == -1:
        if turn % 2 == 0:
            move = p1.make_move(board)
            if move < 0 or move > 6 or game.get_y_of(board, move) == -1:
                game_end = game.BLACK
                break
            board, _ = game.make_move(board, move, game.RED)
        else:
            move = p2.make_move(board)
            if move < 0 or move > 6 or game.get_y_of(board, move) == -1:
                game_end = game.RED
                break
            board, _ = game.make_move(board, move, game.BLACK)
        turn += 1
        game_end = game.check_game_end(board)
    if print_winner:
        if game_end == game.RED:
            print("Red Wins")
        elif game_end == game.BLACK:
            print("Black Wins")
        else:
            print("It's a tie.")
    return game_end
# idea: Check if AI is deterministic. If both are deterministic, simulate only 1 game. Otherwise simulate a bunch and see which wins most.


def simulate_matches(ai_1,ai_2,match_count=1):
    wins_1 = 0
    wins_2 = 0
    ties = 0
    for _ in range(0,match_count):
        winner = play_normal(ai_1,ai_2)
        if winner==game.RED:
            wins_1+=1
        elif winner==game.BLACK:
            wins_2+=1
        elif winner==game.EMPTY:
            ties+=1
    return wins_1, wins_2, ties

