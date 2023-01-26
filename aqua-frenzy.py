#!/usr/bin/env python3

import chess
import random
import sys

print("AquaFrenzy")

debug = False
moves = []
board = chess.Board()

def find_move(board):
    moves = list(board.legal_moves)
    return random.choice(moves)

def handle(line, board):
    global moves

    tokens = line.split()
    cmd = tokens[0]

    if cmd == "uci":
        print("id name AquaFrenzy")
        print("id author Scott Lewis")
        #print("option name Name type ...")
        print("uciok")

    elif cmd == "isready":
        print("readyok")

    elif cmd == "stop":
        pass

    elif cmd == "quit":
        sys.exit(0)

    elif cmd == "debug":
        debug = True

    elif cmd == "position":
        # TODO: support FEN
        if tokens[1] == "startpos":
            board.reset()

        moves = tokens[3:]
        for uci_move in moves:
            board.push_uci(uci_move)

    elif cmd == "go":
        # TODO: support FEN
        move = find_move(board)
        print(f"bestmove {move.uci()}")
    else:
        pass

while True:
    line = input()
    handle(line, board)
