from itertools import cycle


class Game:
    def __init__(self, field_size: int = 3):
        self.figures = ['x', 'o']
        self.players = cycle(self.figures)
        self.field_size = field_size
        self.field = [[None for y in range(field_size)] for x in range(field_size)]
        self.current_player = next(self.players)

    def show_board(self):
        for row in self.field:
            print(' '.join(col or '_' for col in row))
        print()

    def player_move(self):
        while True:
            try:
                user_input = input(self.current_player + ' > ')
                x, y = [int(value) - 1 for value in user_input.split()]
                if (not 0 <= x < self.field_size) or (not 0 <= y < self.field_size):
                    raise ValueError
                if self.field[x][y] is not None:
                    raise ValueError
                break
            except ValueError:
                pass
        self.field[x][y] = self.current_player
        self.current_player = next(self.players)

    def get_winner(self) -> str:
        for figure in self.figures:
            for row in self.field:
                if all(col == figure for col in row):
                    return figure

            for x in range(self.field_size):
                if all(row[x] == figure for row in self.field):
                    return figure

            if all(self.field[x][x] == figure for x in range(self.field_size)):
                return figure
            if all(
                    self.field[x][self.field_size - x - 1] == figure
                    for x in range(self.field_size)):
                return figure

    def game_loop(self):
        while True:
            self.show_board()
            self.player_move()
            winner = self.get_winner()
            if winner:
                self.show_board()
                print(f"Player {winner} wins!")
                break


if __name__ == '__main__':
    print("Welcome to Tic-tac-toe game!")
    print("Type coordinates, e.g. 1 2")
    game = Game()
    game.game_loop()
