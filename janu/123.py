import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Piece symbols
PIECES = {
    'bP': '♟', 'bR': '♜', 'bN': '♞', 'bB': '♝', 'bQ': '♛', 'bK': '♚',
    'wP': '♙', 'wR': '♖', 'wN': '♘', 'wB': '♗', 'wQ': '♕', 'wK': '♔'
}


# Chess board initial setup
def create_board():
    board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ]
    return board


# Load images
def load_images():
    pieces = {}
    for piece in PIECES:
        pieces[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))
    return pieces


# Main drawing function
def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board, images):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece:
                screen.blit(images[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Convert board position to coordinates
def convert_pos(pos):
    x, y = pos
    row = y // SQ_SIZE
    col = x // SQ_SIZE
    return row, col


# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    board = create_board()
    images = load_images()
    running = True
    selected_piece = None
    player_turn = 'w'

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                row, col = convert_pos(location)
                if selected_piece:
                    # Move the piece if valid
                    new_row, new_col = row, col
                    s_row, s_col = selected_piece
                    piece = board[s_row][s_col]
                    if piece and piece[0] == player_turn:
                        board[new_row][new_col] = piece
                        board[s_row][s_col] = None
                        player_turn = 'b' if player_turn == 'w' else 'w'
                    selected_piece = None
                else:
                    if board[row][col] and board[row][col][0] == player_turn:
                        selected_piece = (row, col)

        draw_board(screen)
        draw_pieces(screen, board, images)
        pygame.display.flip()
        clock.tick(MAX_FPS)


if __name__ == "__main__":
    main()
