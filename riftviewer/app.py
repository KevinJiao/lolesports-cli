"""Main module"""
import npyscreen


class ScheduleForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.game = self.add(
            npyscreen.TitleSelectOne, scroll_exit=True, name='Upcoming matches',
            values=['C9 vs G2', 'TL vs FNC', 'TSM vs OG'])


class RiftviewerApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', ScheduleForm, name='Schedule')


def main():
    RiftviewerApp().run()
