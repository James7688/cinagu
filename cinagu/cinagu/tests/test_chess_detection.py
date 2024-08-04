# test_chess_detection.py
import unittest
from cinagu.chess_detection import detect_abnormal_moves, detect_cheating_pattern

class TestChessDetection(unittest.TestCase):

    def test_detect_abnormal_moves(self):
        pgn = """[Event "F/S Return Match"]
                 [Site "Belgrade, Serbia JUG"]
                 [Date "1992.11.04"]
                 [Round "29"]
                 [White "Fischer, Robert J."]
                 [Black "Spassky, Boris V."]
                 [Result "1/2-1/2"]
                 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6
                 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 Bb7 12. cxb5 axb5 13. dxe5 dxe5
                 14. Nc3 b4 15. Nd5 Nxd5 16. exd5 Bd6 17. Bg5 f6 18. Be3 Qe8 19. Nd2 Qg6
                 20. Qg4 f5 21. Qg5 Qf7 22. f3 h6 23. Qh4 f4 24. Bf2 Qg6 25. Rac1 Ra5
                 26. Ne4 Rf5 27. Qd8+ Nf8 28. Rc2 Ra6 29. Rec1 Kh7 30. Kh2 Qf7 31. Rc6
                 Ra5 32. R1c4 Rh5 33. Be1 Ng6 34. Qb8 Qf5 35. Qd8 Qb1 36. Bf2 Ne7
                 37. Nxd6 cxd6 38. Rxd6 Nf5 39. Qd7 Ng3 40. Rg6 Qh1# 0-1"""
        abnormal_moves = detect_abnormal_moves(pgn)
        self.assertTrue(len(abnormal_moves) > 0)

    def test_detect_cheating_pattern(self):
        pgn = """[Event "F/S Return Match"]
                 [Site "Belgrade, Serbia JUG"]
                 [Date "1992.11.04"]
                 [Round "29"]
                 [White "Fischer, Robert J."]
                 [Black "Spassky, Boris V."]
                 [Result "1/2-1/2"]
                 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6
                 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 Bb7 12. cxb5 axb5 13. dxe5 dxe5
                 14. Nc3 b4 15. Nd5 Nxd5 16. exd5 Bd6 17. Bg5 f6 18. Be3 Qe8 19. Nd2 Qg6
                 20. Qg4 f5 21. Qg5 Qf7 22. f3 h6 23. Qh4 f4 24. Bf2 Qg6 25. Rac1 Ra5
                 26. Ne4 Rf5 27. Qd8+ Nf8 28. Rc2 Ra6 29. Rec1 Kh7 30. Kh2 Qf7 31. Rc6
                 Ra5 32. R1c4 Rh5 33. Be1 Ng6 34. Qb8 Qf5 35. Qd8 Qb1 36. Bf2 Ne7
                 37. Nxd6 cxd6 38. Rxd6 Nf5 39. Qd7 Ng3 40. Rg6 Qh1# 0-1"""
        is_cheating = detect_cheating_pattern(pgn)
        self.assertTrue(is_cheating)

if __name__ == '__main__':
    unittest.main()
