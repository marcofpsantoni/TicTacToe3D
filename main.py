from gamemanager import GameManager
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

game_manager = GameManager()


class MyButton(Button):

    def btn(self, q, r, c):
        good = game_manager.insert_marker(q, r, c)

        if good:

            if game_manager.get_current_player() == 1:
                self.text = 'x'

            if game_manager.get_current_player() == 2:
                self.text = 'o'

            if  game_manager.win_test() == 0:
                game_manager.advance_player()
                kv.ids.tocca.text = 'Tocca al Giocatore ' + str(game_manager.get_current_player())

            else:
                winner = game_manager.win_test()
                popup = MyPopup()
                popup.ids.result.text = 'Vittoria Giocatore ' + str(winner)
                popup.open()


class MyPopup(Popup):

    def exit(self):
        App.get_running_app().stop()

    def reset(self):
        game_manager.inizializza()
        for child in list(kv.ids.grid0.children):
            child.text=''
        for child in list(kv.ids.grid1.children):
            child.text=''
        for child in list(kv.ids.grid2.children):
            child.text=''
        for child in list(kv.ids.grid3.children):
            child.text=''
        self.dismiss()

    pass


class MyGame(GridLayout):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):

    def build(self):
        game_manager.inizializza()
        return kv


if __name__ == "__main__":
    MyMainApp().run()
