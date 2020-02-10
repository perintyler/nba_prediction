from sportsreference.nba.boxscore import Boxscores, Boxscore
from datetime import date, timedelta
import json
import pandas as pd
import numpy as np
import os
from input_data import PLAYER_STATS


def get_player_averages():
    return

# saves the home/away points of every game in a json file: gameID -> [away, home]
def save_game_results():
    results = {}
    gameIds = [id.rstrip('\n') for id in open('game_ids.txt')]
    for id in gameIds:
        boxscore = Boxscore(id)
        results[id] = [boxscore.away_points, boxscore.home_points]

    with open('game_results.json', 'w') as outfile:
        json.dump(results, outfile)


# id: game id
# awayDF: dataframe containing merged game stats of all away players
# homeDF: dataframe containing merged game stats of all home players
def save_game_to_file(id, awayDF, homeDF):

    game_dir = f"games/{id}"
    if not os.path.exists(game_dir):
        os.makedirs(game_dir)
    else:
        print(f"game with id {id} has already been saved")
        return

    away_path = f'{game_dir}/away.pkl'
    awayDF.to_pickle(away_path)

    home_path = f'{game_dir}/home.pkl'
    homeDF.to_pickle(home_path)


# gets every players stats for every game and saves the data in psl files
# files are stored in games/<gameId>/<home or away>.psl
def save_player_data():
    gameIds = [id.rstrip('\n') for id in open('game_ids.txt')]
    for id in gameIds:
        boxscore = Boxscore(id)

        away_roster = boxscore.away_players
        away_data = away_roster.pop().dataframe
        for player in away_roster:
            away_data = pd.concat([away_data, player.dataframe])

        home_roster = boxscore.home_players
        home_data = home_roster.pop().dataframe
        for player in home_roster:
            home_data = pd.concat([home_data, player.dataframe])

        home_data = home_data[PLAYER_STATS]
        away_data = away_data[PLAYER_STATS]
        save_game_to_file(id, away_data, home_data)


# saves team box score for every game starting at the given start date
def save_game_data():
    games = []

    gameIds = [id.rstrip('\n') for id in open('game_ids.txt')]
    for id in gameIds:
        print(counter)
        boxscore = Boxscore(id)

        # get the games data and select the needed stats from it
        stats = boxscore.dataframe
        stats = stats[input_data.BOXSCORE_STATS]
        stats = {k: v[0] for k, v in stats.to_dict('list').items()}

        gameData = {
            'stats': stats,
            'result': [boxscore.away_points, boxscore.home_points]
        }

        games.append(gameData)

    with open("game_data.json", 'w') as outfile:
        outfile.write(json.dumps(games))


# saves the game ids of every game of the 2018-19 season to 'game_ids.txt'
def save_game_ids():
    nbaStartDate2018 = datetime(2018, 10, 17)
    boxscores = Boxscores(nbaStartDate2018, datetime.now())
    boxscore_ids = []
    for date, games in boxscores.games.items():
        for game in games:
            boxscore_ids.append(game['boxscore'])

    with open('game_ids.txt', 'w') as file:
        file.write('\n'.join(boxscore_ids))



if __name__ == "__main__":
    if(input('Are you sure? (y/n)')=='y'):
        save_player_data()
    else:
        print("Aborting save")
