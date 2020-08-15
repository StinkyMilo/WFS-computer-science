import pygame
from pygame.locals import *
from time import sleep
import game_logic as game
import ai

def play_pygame_ai(p1ai, p2ai):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode((400,400))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False


def play_pygame_players():
    pass


def play_pygame_1ai(ai):
    pass


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
            if move < 0 or move > 6 or game.get_y_of(board,move)==-1:
                game_end = game.BLACK
                print("Red attempted an invalid move.")
                break
            board, _ = game.make_move(board,move,game.RED)
            if pause_after_p1:
                sleep(1)
        else:
            move = p2.make_move(board)
            if move < 0 or move > 6 or game.get_y_of(board,move)==-1:
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


