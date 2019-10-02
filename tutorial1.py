import pew


# Displaying pixels and stuff
class Game:
    def __init__(self):
        pew.init()
        self.screen = pew.Pix()
        self.main_loop()

    def main_loop(self):
        while True:
            self.screen.pixel(0, 0, 0)
            self.screen.pixel(1, 1, 1)
            self.screen.pixel(2, 2, 2)
            self.screen.pixel(3, 3, 3)
            self.screen.box(2, 5, 0, 2, 2)
            pew.show(self.screen)
            pew.tick(1 / 3)


that = Game()
