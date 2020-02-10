TEAM_STATS = [
    'assists',
    'blocks',
    'steals',
    'defensive_rebounds',
    'offensive_rebounds',
    'two_point_field_goal_attempts',
    'two_point_field_goals',
    'three_point_field_goal_attempts',
    'three_point_field_goals',
    'free_throw_attempts',
    'free_throws',
    'personal_fouls'
]
HOME_STATS =  [('away_' + stat) for stat in TEAM_STATS]
AWAY_STATS = [('home_' + stat) for stat in TEAM_STATS]
BOXSCORE_STATS = HOME_STATS + AWAY_STATS


PLAYER_STATS = [
    'usage_percentage',
#    'two_point_attempts',
    'two_point_percentage',
#    'turnovers',
    'turnover_percentage',
    'total_rebound_percentage',
#    'total_rebounds',
    'three_point_attempt_rate',
    'true_shooting_percentage',
    'defensive_rebound_percentage',
#    'defensive_rebounds',
    'offensive_rebound_percentage',
#    'offensive_rebounds',
    'assist_percentage',
#    'assists',
    'block_percentage',
#    'blocks',
#    'box_plus_minus',
    'effective_field_goal_percentage',
#    'free_throw_attempts',
    'free_throw_percentage',
    'personal_fouls'
]
