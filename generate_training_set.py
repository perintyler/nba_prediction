import numpy as np
import json
import numpy as np
from stat_utils import get_season_data
from stats import get_data

def generate():
    dataset = get_season_data()
    x_train = []
    y_train = []
    for game in dataset:
        stats = game['stats']
        x = serialize(stats[0], stats[1]).flatten()
        x_train.append(x)
        # result is either a 1 or a 0 for win/loss (for now)
        y_train.append(game['result'])
    return x_train, y_train


def get_game_data():
    data = []
    games = [["DET", "IND"],
            ["ORL", "TOR"],
            ["CHI", "NYK"],
            ["MIA", "BOS"],
            ["POR", "MIN"]]
    for game in games:
        print(game)
        away, home = get_data(game[0], game[1])
        data.append(serialize(away, home))
    return data


def serialize(away_df, home_df):
    # replace nan/Nones with 0
    away = away_df.fillna(0).to_numpy()
    home = home_df.fillna(0).to_numpy()

    # the data frame contained stats from the
    away = away[~np.all(away == 0, axis=1)]
    home = home[~np.all(home == 0, axis=1)]

    # add padding to make the amount of rows the max amount of players: 13
    max_team_size = 13
    away_padding = max_team_size - away.shape[0]
    home_padding = max_team_size - home.shape[0]
    away = np.pad(away, ((0,away_padding),(0,0)), 'constant')
    home = np.pad(home, ((0,home_padding),(0,0)), 'constant')

    # stack home and away arrays on top of eachother making a 3d array
    return np.stack([away, home])
