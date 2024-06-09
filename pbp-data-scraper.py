import requests
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Apple M1 Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# get game logs from the reg season
gamefinder = leaguegamefinder.LeagueGameFinder(season_nullable='2023-24', 
                                              league_id_nullable='00', 
                                              season_type_nullable='Regular Season')

games = gamefinder.get_data_frames()[0]

# Get a list of distinct game ids 
game_ids = games['GAME_ID'].unique().tolist()

# get pbp logs from the 2023-24 season
def get_data(game_id):
    play_by_play_url = "https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{}.json".format(game_id)
    response = requests.get(url=play_by_play_url, headers=headers).json()
    play_by_play = response['game']['actions']
    df = pd.DataFrame(play_by_play)
    df['gameid'] = game_id
    return df

# get data from all ids
pbpdata = []
for game_id in game_ids:
    game_data = get_data(game_id)
    pbpdata.append(game_data)

# aggregate data into one df and save into csv
df = pd.concat(pbpdata, ignore_index=True)
df.to_csv('data.csv')