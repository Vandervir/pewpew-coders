import pew

# additional keys 'z' and 'x'
class Game:
    def __init__(self):
        pew.init()
        self.screen = pew.Pix()
        self.cursorx, self.cursory = 4, 4
        self.counter = 1
        self.size = 1
        self.pressing = False
        self.main_loop()

    def main_loop(self):
        while True:
            self.keys()
            self.print_dot()
            pew.show(self.screen)
            pew.tick(1 / 3)

    def print_dot(self):
        self.screen = pew.Pix()
        self.screen.box(x=0, y=0, color=self.color_animation(), width=self.size, height=self.size)

    def color_animation(self, main_color=3, secondary_color=2):
        if self.counter % 2:
            self.counter = 0
            return main_color
        else:
            self.counter = 1
            return secondary_color

    def keys(self):
        keys = pew.keys()
        print('Pressed {}'.format(self.size))
        if keys & pew.K_O and self.size < 8:
            self.size += 1
            print('Pressed O')
        elif keys & pew.K_X and self.size > 1:
            self.size -= 1
            print('Pressed X')


that = Game()
