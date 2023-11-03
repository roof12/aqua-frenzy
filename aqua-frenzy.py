#!/usr/bin/env python3

import chess
import random
import sys

print("AquaFrenzy")

debug = False
moves = []
board = chess.Board()

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3.2,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000,
}

def evaluate(board):
    total = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        elif piece.color == chess.WHITE:
            total += piece_values[piece.piece_type]
        else:
            total -= piece_values[piece.piece_type]
    return total

def find_move(board):
    black_to_move = board.turn == chess.BLACK

    moves = list(board.legal_moves)
    max_eval = float('-inf')
    best_moves = []

    for move in moves:
        board.push(move)
        eval = evaluate(board)
        if black_to_move:
            eval *= -1

        if (eval > max_eval + 0.001):
            max_eval = eval
            best_moves = [move]
        elif (eval > max_eval - 0.001):
            best_moves.append(move)
        board.pop()

    cp = int(max_eval * 100)
    return random.choice(best_moves), cp

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
        # TODO: support 'off' and 'on'
        debug = True

    elif cmd == "position":
        # TODO: support FEN
        if len(tokens) == 1: return 

        if tokens[1] == "startpos":
            board.reset()

        moves = tokens[3:]
        for uci_move in moves:
            board.push_uci(uci_move)

    elif cmd == "go":
        # TODO: support FEN
        move, cp = find_move(board)
        print(f"info score cp {cp}")
        print(f"bestmove {move.uci()}")
    else:
        pass

while True:
    line = input()
    handle(line, board)
