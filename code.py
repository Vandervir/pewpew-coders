import pew
import random


# example code
class Game:
    def __init__(self):
        pew.init()
        self.cursorx, self.cursory = 4, 4
        self.screen = pew.Pix()
        self.pressing = False
        self.board = bytearray(64)
        self.counter = 0

        self.main_loop()

    def main_loop(self):
        while True:
            self.keys()
            self.print_board()
            self.iterate_board()
            self.delayed_random_click()

            pew.show(self.screen)
            pew.tick(1 / 3)

    def delayed_random_click(self):
        if self.counter > 0:
            self.counter -= 1
        else:
            self.counter = 4
            self.cursorx = random.randint(0, 7)
            self.cursory = random.randint(0, 7)
            self.press_confirm()

    @staticmethod
    def get_board_id(x, y):
        return x + (y * 8)

    def clear_board(self):
        self.board = bytearray(64)

    def print_board(self):
        for x in range(0, 8):
            for y in range(0, 8):
                board_id = self.get_board_id(x, y)
                self.screen.pixel(x, y, self.board[board_id])

    def iterate_board(self):
        temp_board = bytearray(64)
        for x in range(0, 8):
            for y in range(0, 8):
                board_id = self.get_board_id(x, y)
                temp_board[board_id] = self.board[board_id]
        for x in range(0, 8):
            for y in range(0, 8):
                list_tup = {(x, y + 1), (x - 1, y), (x, y - 1), (x + 1, y)}
                board_id = self.get_board_id(x, y)
                if self.board[board_id] > 0:
                    temp_board[board_id] = self.board[board_id] - 1
                    for tup in list_tup:
                        if tup[0] < 0:
                            continue
                        elif tup[0] > 7:
                            continue
                        elif tup[1] < 0:
                            continue
                        elif tup[1] > 7:
                            continue
                        neighbour_board_id = self.get_board_id(tup[0], tup[1])
                        if temp_board[neighbour_board_id] <= self.board[board_id]:
                            temp_board[neighbour_board_id] = self.board[board_id]
        self.board = temp_board

    def press_confirm(self):
        board_id = self.get_board_id(self.cursorx, self.cursory)
        self.board[board_id] = 3
        pass

    def press_decline(self):
        pass

    def keys(self):
        keys = pew.keys()
        if not self.pressing:
            if keys & pew.K_UP and self.cursory > 0:
                self.cursory -= 1
            elif keys & pew.K_DOWN and self.cursory < 7:
                self.cursory += 1
            if keys & pew.K_LEFT and self.cursorx > 0:
                self.cursorx -= 1
            elif keys & pew.K_RIGHT and self.cursorx < 7:
                self.cursorx += 1
            elif keys & pew.K_X:
                self.press_confirm()
            elif keys & pew.K_O:
                self.press_decline()
            if keys:
                self.pressing = True
        else:
            if not keys:
                self.pressing = False


that = Game()
