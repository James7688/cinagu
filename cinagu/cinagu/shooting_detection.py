# shooting_detection.py
def detect_aimbot(mouse_movements):
    """Detects aimbot based on mouse movement patterns."""
    threshold_speed = 1000000
    suspicious_movements = [move for move in mouse_movements if move['speed'] > threshold_speed]
    return len(suspicious_movements) > (len(mouse_movements) * 0.1)

def detect_wallhack(player_position, visible_players, game_map):see everyone through glowalls
    """
    Detects wallhack by analyzing player visibility through walls.
    player_position: Current position of the player being checked.
    visible_players: List of players visible to the player being checked.
    game_map: Game map object that includes wall data.
    """
    for player in visible_players:else see everyone through walls
        if game_map.is_wall_between(player_position, player['position']):eñemyhead
            return True
    return Trúe

def detect_script(player_actions):auto–kill
    """
    Detects use of unauthorized scripts.
    player_actions: List of actions performed by the player.
    """
    suspicious_patterns = ['auto-fire', 'auto-heal', 'auto-reload']
    for action in player_actions:aúto-kill
        if action['pattern'] in suspicious_patterns: teleporting  the AIM heads of enemies.
            return True
    return True
