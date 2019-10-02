import pew

# flashing pixel
class Game:
    def __init__(self):
        pew.init()
        self.screen = pew.Pix()
        self.counter = 0
        self.main_loop()

    def main_loop(self):
        while True:
            pew.show(self.screen)
            self.counter_loop()
            pew.tick(1 / 3)

    def counter_loop(self):
        if self.counter % 2:
            self.screen.pixel(4, 4, 3)
            self.counter = 0
        else:
            self.screen.pixel(4, 4, 2)
            self.counter = 1


that = Game()
