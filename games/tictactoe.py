def show(grid):
    """Neatly prints out a tictactoe grid."""
    for row in grid:
        print(' '.join(str(i) for i in row))

def get_move(grid):
    """Gets the move of a player."""
    vals = []
    print()
    for i in ('row', 'column'):
        while True:
            val = input('Enter a {}: '.format(i))
            try:
                val = int(val)
                if 0 < val < 4:
                    vals.append(val - 1)
                    break
                else:
                    print('(Enter a number between 1-3)')
            except ValueError:
                print('(Please enter a number.)')
    if grid[vals[0]][vals[1]] == 0:
        return vals[0], vals[1]
    else:
        print('That space is taken.')
        return get_move(grid)

def check_win(grid, num):
    """Checks if a player has one."""
    for i in range(3):
        if grid[i].count(num) == 3 or [row[i] for row in grid].count(num) == 3:
            return True
    if grid[0][0] == num and grid[1][1] == num and grid[2][2] == num or grid[0][2] == num and grid[1][1] == num and grid[2][0] == num:
        return True
    return False

def main():
    """Plays a game of tictactoe."""
    grid = [[0 for j in range(3)] for i in range(3)]
    message = 'Player{}, please enter your name: '
    players = [input(message.format(i + 1)) for i in range(2)]
    while True:
        for player in players:
            print(f'\n{player.title()}, it is your turn.\n')
            show(grid)
            y, x = get_move(grid)
            grid[y][x] = players.index(player) + 1
            if check_win(grid, players.index(player) + 1):
                print(f'\n{player.title()} wins!')
                return

if __name__ == '__main__':
    main()
