import pew

# writing text
class Game:
    def __init__(self):
        pew.init()
        self.screen = pew.Pix()
        self.main_loop()

    def main_loop(self):
        while True:
            self.print_text("Hello word!")

    def print_text(self, raw_text):
        text = pew.Pix.from_text(raw_text)
        print(text)
        for dx in range(-8, text.width):
            self.screen.blit(text, -dx, 1)
            pew.show(self.screen)
            pew.tick(1 / 12)


that = Game()
