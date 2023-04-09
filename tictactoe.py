import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 5
ICON_SIZE = 80
HIGHLIGHT_WIDTH = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load assets
x_icon = pygame.image.load('x_icon.png')
o_icon = pygame.image.load('o_icon.png')

# Scale icons
x_icon = pygame.transform.scale(x_icon, (ICON_SIZE, ICON_SIZE))
o_icon = pygame.transform.scale(o_icon, (ICON_SIZE, ICON_SIZE))

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

# Draw the grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * SCREEN_WIDTH // 3, 0), (i * SCREEN_WIDTH // 3, SCREEN_HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i * SCREEN_HEIGHT // 3), (SCREEN_WIDTH, i * SCREEN_HEIGHT // 3), LINE_WIDTH)

def check_winner(board):
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2] != None:
            return row[0], [(i, 0), (i, 1), (i, 2)]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != None:
            return board[0][j], [(0, j), (1, j), (2, j)]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0], [(0, 0), (1, 1), (2, 2)]

    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2], [(0, 2), (1, 1), (2, 0)]

    return None, []

def highlight_cells(cells):
    for i, j in cells:
        x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)
        y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)
        pygame.draw.rect(screen, GREEN, (x - HIGHLIGHT_WIDTH // 2, y - HIGHLIGHT_WIDTH // 2, ICON_SIZE + HIGHLIGHT_WIDTH, ICON_SIZE + HIGHLIGHT_WIDTH), HIGHLIGHT_WIDTH)

def main():
    board = [[None for _ in range(3)] for _ in range(3)]
    player = 'X'
    winning_cells = []
    winner = None  # Define winner variable here
    running = True
    game_over = False
    while running:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over and event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row, col = y // (SCREEN_HEIGHT // 3), x // (SCREEN_WIDTH // 3)

                if board[row][col] is None:
                    board[row][col] = player
                    winner, winning_cells
                    winner, winning_cells = check_winner(board)
                    if winner:
                        print(f"Player {winner} wins!")
                        game_over = True
                    else:
                        player = 'O' if player == 'X' else 'X'

        # Draw icons
        for i in range(3):
            for j in range(3):
                x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)
                y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)
                if board[i][j] == 'X':
                    screen.blit(x_icon, (x, y))
                elif board[i][j] == 'O':
                    screen.blit(o_icon, (x, y))

        if game_over:
            highlight_cells(winning_cells)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

