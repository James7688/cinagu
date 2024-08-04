Cinagu is a Python package designed to detect cheats and hacks in various games such as chess and shooting games. It provides tools to identify aimbots, wallhacks, and unauthorized scripts, as well as abnormal moves in chess games.

## Features

- **Chess Cheat Detection**:
  - Detects abnormal moves and cheating patterns in chess games.

- **Shooting Game Cheat Detection**:
  - Detects aimbots based on mouse movement patterns.
  - Detects wallhacks by analyzing player visibility through walls.
  - Detects unauthorized scripts and macros.

- **Game Integration**:
  - Can be integrated with various game engines such as Ursina, Panda3D, Pygame, etc.

## Installation

You can install Cinagu using pip:

```bash
pip install cinagu
```

# Usage

## Chess Cheat Detection

### Detecting Abnormal Moves

To detect abnormal moves in a chess game, use the detect_abnormal_moves function from the cinagu.chess_detection module. This function analyzes the moves and their timings to determine if there are any abnormal patterns.

```python
from cinagu.chess_detection import detect_abnormal_moves

# Example list of moves with their timings
moves = [
    {'move': 'e2e4', 'time': 5},
    {'move': 'e7e5', 'time': 10},
    {'move': 'g1f3', 'time': 2},
    {'move': 'b8c6', 'time': 15},
]

# Detect abnormal moves
is_abnormal = detect_abnormal_moves(moves)
print(f'Abnormal Moves Detected: {is_abnormal}')
```

### Detecting Cheating Patterns
To detect cheating patterns in a chess game, use the detect_cheating_pattern function. This function analyzes the moves and their timings to determine if there is a cheating pattern.

```python
from cinagu.chess_detection import detect_cheating_pattern

# Example list of moves with their timings
moves = [
    {'move': 'e2e4', 'time': 5},
    {'move': 'e7e5', 'time': 10},
    {'move': 'g1f3', 'time': 2},
    {'move': 'b8c6', 'time': 15},
]

# Detect cheating patterns
is_cheating = detect_cheating_pattern(moves)
print(f'Cheating Pattern Detected: {is_cheating}')
```

## Shooting Game Cheat Detection

### Detecting Aimbots

To detect aimbots in a shooting game, use the detect_aimbot function from the cinagu.shooting_detection module. This function analyzes the mouse movements to determine if there are any aimbot-like patterns.

```python
from cinagu.shooting_detection import detect_aimbot

# Example list of mouse movements with their speeds
mouse_movements = [
    {'speed': 1200},
    {'speed': 500},
    {'speed': 1300},
    {'speed': 100},
    {'speed': 2000}
]

# Detect aimbot
is_aimbot = detect_aimbot(mouse_movements)
print(f'Aimbot Detected: {is_aimbot}')
```

### Detecting Wallhacks

To detect wallhacks in a shooting game, use the detect_wallhack function. This function analyzes the player's position and visibility to determine if they are using wallhacks.

```python
from cinagu.shooting_detection import detect_wallhack

# Example player position and visible players
player_position = (0, 0)
visible_players = [{'position': (1, 1)}]
game_map = MockGameMap()  # Replace with actual game map object

# Detect wallhack
is_wallhack = detect_wallhack(player_position, visible_players, game_map)
print(f'Wallhack Detected: {is_wallhack}')
```

### Detecting Unauthorized Scripts

To detect unauthorized scripts in a shooting game, use the detect_script function. This function analyzes the player's actions to determine if they are using unauthorized scripts or macros.

```python
from cinagu.shooting_detection import detect_script

# Example list of player actions
player_actions = [{'pattern': 'auto-fire'}]

# Detect unauthorized scripts
is_script = detect_script(player_actions)
print(f'Script Detected: {is_script}')
```

### Integrating with a Game Engine

To integrate Cinagu with a game engine, use the integrate_with_game function from the cinagu.game_integration module. This function sets up the cheat detection to run within the game loop.

Example with a Mock Game Engine:

Here’s an example of how to integrate the detection functions with a mock game engine. Replace MockGameEngine, MockPlayer, and MockGameMap with your actual game engine components.

```python
from cinagu.game_integration import integrate_with_game
from cinagu.shooting_detection import detect_aimbot, detect_wallhack, detect_script

# Mock game engine (replace with Ursina, Panda3D, Pygame, etc.)
class MockGameEngine:
    def __init__(self):
        self.players = []

    def get_players(self):
        return self.players

    def get_map(self):
        return MockGameMap()

    def set_update_callback(self, update_func):
        self.update_func = update_func

    def run(self):
        # Simulate game loop
        for _ in range(10):  # Run for 10 frames
            self.update_func()

class MockPlayer:
    def __init__(self):
        self.mouse_movements = [
            {'speed': 1200},
            {'speed': 500},
            {'speed': 1300},
            {'speed': 100},
            {'speed': 2000}
        ]
        self.position = (0, 0)
        self.visible_players = [{'position': (1, 1)}]
        self.actions = [{'pattern': 'auto-fire'}]

    def get_mouse_movements(self):
        return self.mouse_movements

    def get_position(self):
        return self.position

    def get_visible_players(self):
        return self.visible_players

    def get_actions(self):
        return self.actions

class MockGameMap:
    def is_wall_between(self, pos1, pos2):
        return pos1 == (0, 0) and pos2 == (1, 1)

# Set up the mock game engine
game_engine = MockGameEngine()
player = MockPlayer()
game_engine.players.append(player)

# Integrate cheat detection with the game engine
detection_functions = {
    'aimbot': detect_aimbot,
    'wallhack': detect_wallhack,
    'script': detect_script
}
integrate_with_game(game_engine, detection_functions)

# Run the mock game
game_engine.run()
```

## Contact

Quy Anh Nguyen - quyanh082013@gmail.com