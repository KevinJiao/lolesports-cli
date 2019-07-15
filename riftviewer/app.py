"""Main module"""
import npyscreen

from riftviewer.esports_api import League


class ScheduleForm(npyscreen.Form):
    def __init__(self, *args, **kwargs):
        """Retrieve the list of games"""
        super().__init__(*args, **kwargs)
        self.league = League()

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        #TODO Hook up the games to the picker
        games = self.league.get_games()
        self.game = self.add(
            npyscreen.TitleSelectOne, scroll_exit=True, name='Upcoming matches',
            values=['C9 vs G2', 'TL vs FNC', 'TSM vs OG'])


class RiftviewerApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', ScheduleForm, name='Schedule')


def main():
    RiftviewerApp().run()
