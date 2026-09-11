from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Button
from textual.containers import Vertical, Grid
from textual.reactive import reactive
import time

class Weather(Static):
    temp = reactive(0)
    rain = reactive(0)
    wind = reactive(0)

    def render(self):
        return f"""Темпиратур: {self.temp}
    Осадки: {self.rain}
    Ветер: {self.wind}
    """

class Clock(Static):
    time = """ ###   ###     ###   ###
#   # #   # # #   # #   #
#   #  ###    #   # #   #
#   # #   # # #   # #   #
 ###   ###     ###   ###"""

    def render(self):
        return self.time

class Run_line(Static):
    line = reactive("s;dkfjjjspdojf[pjhyfjsaojshdpfnasjdfkjaldhfpjsdpifjsahubsifjasiuojfljkuspadfhjdfudf0sjdkfusbfsdkifsaudfsapkfjasdfhsandfopiahfpsjaodufjjahdfkbgaposdjfsihfgiyfhasfjaosiudjfiphsd")

    def render(self):
        return self.line[:40]

    def on_mount(self):
        self.set_interval(0.1, self.tick)

    def tick(self):
        self.line = self.line[1:] + self.line[0]




class MyApp(App):
    CSS = """
    Weather {
        border: solid green;
        padding: 1 2;
        content-align: left top;
        height: 7;
    }
    Clock {
        border: solid green;
        padding: 1 2;
        content-align: center middle;
        height: 7
    }

    #Main {
        layout: grid;
        grid-size: 2 2;          /* 2 колонки, 2 ряда */
        grid-columns: 1fr 1fr;   /* ширина колонок */
        grid-rows: 1fr 1fr;      /* высота рядов */
        grid-gutter: 1;          /* промежуток между ячейками */
    }

    .box {
        border: solid green;
        height: 100%;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid(id="Main"):
            yield Weather(classes="box")
            yield Clock(classes="box")
            yield Run_line(classes="box")
        yield Footer()

    # def on_button_pressed(self):
    #     self.query_one("#counter").count += 1

if __name__ == "__main__":
    MyApp().run()
