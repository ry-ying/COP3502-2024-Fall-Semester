import pygame
import sys
from board import Board
from sudoku_generator import generate_sudoku

pygame.init()

# Settings - TODO: Discuss window size
WIDTH, HEIGHT = 540, 540
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Sudoku")  # TODO: Discuss window title

# Fonts - TODO: We can also abstract this to export to be used within Cell and Board classes to avoid duplication
FONT = pygame.font.SysFont('arial', 40)
SMALL_FONT = pygame.font.SysFont('arial', 20)

# Difficulty map
DIFFICULTY_LEVELS = {
    'easy': 30,
    'medium': 40,
    'hard': 50
}

# Colors - TODO: Discuss colors and styles
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
GRAY = pygame.Color('gray')
BUTTON_COLOR = pygame.Color('#E0E0E0')
BUTTON_HOVER_COLOR = pygame.Color('#BDBDBD')
BUTTON_TEXT_COLOR = pygame.Color('black')

# Button design config - TODO: Discuss colors and styles
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_PADDING = 20
BUTTON_Y_POSITION = HEIGHT - BUTTON_HEIGHT - 50

# Difficulty display
BUTTONS = {
    'easy': (0, 'Easy'),
    'medium': (1, 'Medium'),
    'hard': (2, 'Hard')
}


def draw_text_center(screen, text, font, color, y_offset=0):
    """
    Draw text centered within the screen with an optional vertical offset.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + y_offset))
    screen.blit(text_surface, text_rect)


def create_button_rects():
    """
    Create and return button rectangles based on global properties.
    """
    total_buttons_width = len(BUTTONS) * BUTTON_WIDTH + (len(BUTTONS) - 1) * BUTTON_PADDING
    start_x = (WIDTH - total_buttons_width) / 2

    return {
        difficulty: pygame.Rect(
            start_x + index * (BUTTON_WIDTH + BUTTON_PADDING),
            BUTTON_Y_POSITION,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        for difficulty, (index, _) in BUTTONS.items()
    }


def render_difficulty_screen(screen, button_rects, mouse_pos=None):
    """
    Render the difficulty selection screen, including buttons.
    """
    screen.fill(WHITE)
    draw_text_center(screen, "Select Game Mode", FONT, BLACK, y_offset=-100)

    for difficulty, rect in button_rects.items():
        color = BUTTON_HOVER_COLOR if mouse_pos and rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=5)

        text_surface = SMALL_FONT.render(BUTTONS[difficulty][1], True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    pygame.display.update()


def get_difficulty(screen):
    """
    Handle the difficulty selection process and return the chosen difficulty.
    """
    button_rects = create_button_rects()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        render_difficulty_screen(screen, button_rects, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for difficulty, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        return difficulty


def draw_end_screen(screen, message):
    """
    Display the end screen with a message.
    """
    screen.fill(WHITE)
    draw_text_center(screen, message, FONT, BLACK)
    pygame.display.update()
    pygame.time.delay(3000)


def create_action_buttons():
    button_labels = ["Reset", "Restart", "Exit"]
    button_rects = {}
    total_buttons_width = len(button_labels) * BUTTON_WIDTH + (len(button_labels) - 1) * BUTTON_PADDING
    start_x = (WIDTH - total_buttons_width) / 2

    for i, label in enumerate(button_labels):
        x = start_x + i * (BUTTON_WIDTH + BUTTON_PADDING)
        button_rects[label] = pygame.Rect(x, HEIGHT + 20, BUTTON_WIDTH, BUTTON_HEIGHT)

    return button_rects


def game_loop(screen, board):
    action_buttons = create_action_buttons()
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        board.draw()
        # Draw action buttons
        for label, rect in action_buttons.items():
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=5)
            text_surface = SMALL_FONT.render(label, True, BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT:
                    clicked = board.click(pos[0], pos[1])
                    if clicked:
                        board.select(clicked[0], clicked[1])
                else:
                    for label, rect in action_buttons.items():
                        if rect.collidepoint(pos):
                            if label == "Reset":
                                board.reset_to_original()
                            elif label == "Restart":
                                main()
                            elif label == "Exit":
                                pygame.quit()
                                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    board.clear()
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    board.place_number()
                    if board.is_full():
                        if board.check_board():
                            draw_end_screen(screen, "Game Won!")
                        else:
                            draw_end_screen(screen, "Game Over :(")
                        main()
                elif event.key in range(pygame.K_1, pygame.K_9 + 1):
                    value = event.key - pygame.K_0
                    board.sketch(value)
                elif event.key == pygame.K_UP:
                    board.move_selection('up')
                elif event.key == pygame.K_DOWN:
                    board.move_selection('down')
                elif event.key == pygame.K_LEFT:
                    board.move_selection('left')
                elif event.key == pygame.K_RIGHT:
                    board.move_selection('right')


def main():
    """
    Main function to start the game.
    """
    difficulty = get_difficulty(SCREEN)
    removed_cells = DIFFICULTY_LEVELS[difficulty]
    board_values, solution = generate_sudoku(9, removed_cells)
    board = Board(WIDTH, HEIGHT, SCREEN, board_values, solution)
    game_loop(SCREEN, board)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()