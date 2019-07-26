"""Fetch leagues and schedules"""
import requests

class League:
    schedule_url = 'https://esports-api.lolesports.com/persisted/gw/getSchedule'

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = {'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}

    def get_games(self):
        resp = self.sess.get(self.schedule_url,
                             params={'hl': 'en-US', 'leagueId': 98767991299243165})
        return resp.json()['data']['schedule']['events']

    def get_leagues(self):
        pass

