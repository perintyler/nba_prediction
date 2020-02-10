from sportsreference.nba.roster import Player, Roster
from sportsreference.nba.boxscore import Boxscores
import pandas as pd
import datetime
from input_data import PLAYER_STATS

def get_player_averages():
    return

injuries = {
    "DET": ["Blake Griffin", "Langston Galloway"],
    "PAC": ["Victor Oladipo"]

}

def get_data(team0,team1):
    away_roster = Roster(team0).players
    home_roster = Roster(team1).players

    away_data = away_roster.pop().dataframe.iloc[[-2]]
    for player in away_roster:
        if(team0.abbreviation, isPlayerInjured(player.player_name)):
            continue
        if(player.dataframe.empty == False):
            try :
                away_data = pd.concat([away_data, player.dataframe.iloc[[-2]]])
            except:
                print("player invalid: " + player.player_name)
    home_data = home_roster.pop().dataframe.iloc[[-2]]
    for player in home_roster:
        if(team0.abbreviation, isPlayerInjured(player.player_name)):
            continue
        if(player.dataframe.empty == False):
            try:
                home_data = pd.concat([home_data, player.dataframe.iloc[[-2]]])
            except:
                print("player invalid: " + player.player_name)
    home_data = home_data[PLAYER_STATS].sort_values(by=['usage_percentage']).head(12)
    away_data = away_data[PLAYER_STATS].sort_values(by=['usage_percentage']).head(12)

    return away_data, home_data

def isPlayerInjured(team_name, player_name):
    if(team_name in injuries):
        team_injuries = injuries[team]
        for injured_player in team_injuries:
            if(player_name = injured_player):
                return True
    return False

def get_game_date():
    id = '201810170CHO'
    game = Boxscore


def get_player_data(id):
    player = Player(id)
    df = player.dataframe
    print(df.columns.values)
    return df



if __name__ == '__main__':
    away, home = get_data('SAC', 'PHI')
