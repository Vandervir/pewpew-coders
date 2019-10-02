import pew

# keyboard
class Game:
    def __init__(self):
        pew.init()
        self.screen = pew.Pix()
        self.cursorx, self.cursory = 4, 4
        self.counter = 0
        self.pressing = False
        self.main_loop()

    def main_loop(self):
        while True:
            self.keys()
            self.print_dot()
            pew.show(self.screen)
            pew.tick(1 / 3)

    def print_dot(self):
        self.screen.box(x=self.cursorx-1, y=self.cursory-1, color=0, width=3, height=3)
        self.screen.pixel(self.cursorx, self.cursory, self.color_animation())

    def color_animation(self, main_color=3, secondary_color=2):
        if self.counter % 2:
            self.counter = 0
            return main_color
        else:
            self.counter = 1
            return secondary_color

    def keys(self):
        keys = pew.keys()
        if keys & pew.K_UP and self.cursory > 0:
            self.cursory -= 1
        elif keys & pew.K_DOWN and self.cursory < 7:
            self.cursory += 1
        if keys & pew.K_LEFT and self.cursorx > 0:
            self.cursorx -= 1
        elif keys & pew.K_RIGHT and self.cursorx < 7:
            self.cursorx += 1
        elif keys & pew.K_X:
            print('Pressed X')
        elif keys & pew.K_O:
            print('Pressed O')


that = Game()
