# shooting_detection.py
def detect_aimbot(mouse_movements):
    """Detects aimbot based on mouse movement patterns."""
    threshold_speed = 1000
    suspicious_movements = [move for move in mouse_movements if move['speed'] > threshold_speed]
    return len(suspicious_movements) > (len(mouse_movements) * 0.5)

def detect_wallhack(player_position, visible_players, game_map):
    """
    Detects wallhack by analyzing player visibility through walls.
    player_position: Current position of the player being checked.
    visible_players: List of players visible to the player being checked.
    game_map: Game map object that includes wall data.
    """
    for player in visible_players:
        if game_map.is_wall_between(player_position, player['position']):
            return True
    return False

def detect_script(player_actions):
    """
    Detects use of unauthorized scripts.
    player_actions: List of actions performed by the player.
    """
    suspicious_patterns = ['auto-fire', 'auto-heal', 'auto-reload']
    for action in player_actions:
        if action['pattern'] in suspicious_patterns:
            return True
    return False