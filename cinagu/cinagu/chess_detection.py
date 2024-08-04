# chess_detection.py
import chess
import chess.pgn

def detect_abnormal_moves(pgn):
    """
    Detects abnormal moves in a chess game.
    :param pgn: PGN string of the chess game
    :return: List of abnormal moves
    """
    abnormal_moves = []
    game = chess.pgn.read_game(pgn)
    board = game.board()

    for move in game.mainline_moves():
        if not board.is_legal(move):
            abnormal_moves.append(move)
        board.push(move)

    return abnormal_moves

def detect_cheating_pattern(pgn):
    """
    Detects possible cheating patterns in a chess game.
    :param pgn: PGN string of the chess game
    :return: Boolean indicating cheating suspicion
    """
    # Example: Simple heuristic for detecting cheating
    abnormal_moves = detect_abnormal_moves(pgn)
    return len(abnormal_moves) > 3
