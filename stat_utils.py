import json
import os
import pandas as pd
import numpy as np
# loads the game from the local storage and returns the away/home dataframes
# containing player boxscore stats
def get_stats(gameId):
    game_dir = f"games/{gameId}"
    if not os.path.exists(game_dir):
        print(f"Game with {gameId} cannot be loaded")
        return

    away_path = f'{game_dir}/away.pkl'
    away_df = pd.read_pickle(away_path)

    home_path = f'{game_dir}/home.pkl'
    home_df = pd.read_pickle(home_path)
    return away_df, home_df


# returns dictionary to get game scores: {gameId: [away_points, home_points]}
def get_game_results():
    with open('game_results.json') as f:
        return json.load(f)


def get_season_data_points():
    data = []
    game_results = get_game_results()

    ids = [id.rstrip('\n') for id in open('game_ids.txt')]
    for gameId in ids:
        away_df, home_df = get_stats(gameId)
        result = game_results[gameId]
        data.append({'stats': [away_df, home_df], 'result': result})

    return data


def get_season_data():
    data = []
    game_results = get_game_results()

    ids = [id.rstrip('\n') for id in open('game_ids.txt')]
    for gameId in ids:
        away_df, home_df = get_stats(gameId)
        points = game_results[gameId]
        result = 0 if points[0] > points[1] else 1
        if(result == 0):
            result = np.array([1,0])
        else:
            result = np.array([0,1])
        data.append({'stats': [away_df, home_df], 'result': result})

    return data
