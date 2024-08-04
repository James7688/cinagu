# test_shooting_detection.py
import unittest
from cinagu.shooting_detection import detect_aimbot, detect_wallhack

class TestShootingDetection(unittest.TestCase):

    def test_detect_aimbot(self):
        mouse_movements = [{'speed': 1200}, {'speed': 500}, {'speed': 1300}, {'speed': 100}, {'speed': 2000}]
        is_aimbot = detect_aimbot(mouse_movements)
        self.assertTrue(is_aimbot)

    def test_detect_wallhack(self):
        player_positions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        object_positions = [(1, 1), (2, 2), (3, 4), (5, 5), (6, 6)]
        is_wallhack = detect_wallhack(player_positions, object_positions)
        self.assertTrue(is_wallhack)

if __name__ == '__main__':
    unittest.main()
