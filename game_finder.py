"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	# Replace the line below with your code

#MyCode

from collections import defaultdict
from datetime import datetime

def calculate_true_shooting(player_stats):
    points = (player_stats['fieldGoal2Made'] * 2 + 
              player_stats['fieldGoal3Made'] * 3 + 
              player_stats['freeThrowMade'])
    
    true_shot_attempts = (player_stats['fieldGoal2Attempted'] + 
                          player_stats['fieldGoal3Attempted'] + 
                          0.44 * player_stats['freeThrowAttempted'])
    
    if true_shot_attempts == 0:
        return 0
    
    return (points / (2 * true_shot_attempts)) * 100

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    game_players = defaultdict(list)
    game_dates = {}

    for player_game in game_data:
        game_id = player_game['gameID']
        true_shooting = calculate_true_shooting(player_game)
        
        if true_shooting >= true_shooting_cutoff:
            game_players[game_id].append(player_game['playerID'])
        
        game_dates[game_id] = player_game['gameDate']

    qualified_games = [
        game_id for game_id, players in game_players.items()
        if len(set(players)) >= player_count
    ]

    return sorted(
        qualified_games,
        key=lambda game_id: datetime.strptime(game_dates[game_id], '%m/%d/%Y'),
        reverse=True
    )
