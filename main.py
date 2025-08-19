import pygame
from game import Game
from board import Board


def main():
    pygame.init()

    # Set screen size for menu and game
    screenSize = (800, 800)
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Minesweeper - Choose Difficulty & Mode")
    font = pygame.font.Font(None, 50)

    # Define button rectangles
    button_easy = pygame.Rect(250, 200, 300, 60)
    button_medium = pygame.Rect(250, 300, 300, 60)
    button_hard = pygame.Rect(250, 400, 300, 60)

    button_ai = pygame.Rect(150, 550, 200, 60)
    button_manual = pygame.Rect(450, 550, 200, 60)

    def draw_difficulty_menu():
        screen.fill((30, 30, 30))
        title = font.render("Choose Difficulty", True, (255, 255, 255))
        screen.blit(title, (screenSize[0] // 2 - title.get_width() // 2, 100))

        pygame.draw.rect(screen, (70, 130, 180), button_easy)
        pygame.draw.rect(screen, (180, 140, 80), button_medium)
        pygame.draw.rect(screen, (180, 60, 60), button_hard)

        easy_text = font.render("Easy", True, (255, 255, 255))
        medium_text = font.render("Medium", True, (255, 255, 255))
        hard_text = font.render("Hard", True, (255, 255, 255))

        screen.blit(easy_text, (button_easy.centerx - easy_text.get_width() // 2, button_easy.y + 10))
        screen.blit(medium_text, (button_medium.centerx - medium_text.get_width() // 2, button_medium.y + 10))
        screen.blit(hard_text, (button_hard.centerx - hard_text.get_width() // 2, button_hard.y + 10))

        pygame.display.flip()

    def draw_mode_menu():
        screen.fill((30, 30, 30))
        title = font.render("Who Should Play?", True, (255, 255, 255))
        screen.blit(title, (screenSize[0] // 2 - title.get_width() // 2, 400))

        pygame.draw.rect(screen, (70, 130, 180), button_ai)
        pygame.draw.rect(screen, (60, 180, 100), button_manual)

        ai_text = font.render("AI", True, (255, 255, 255))
        manual_text = font.render("Myself", True, (255, 255, 255))

        screen.blit(ai_text, (button_ai.centerx - ai_text.get_width() // 2, button_ai.y + 10))
        screen.blit(manual_text, (button_manual.centerx - manual_text.get_width() // 2, button_manual.y + 10))

        pygame.display.flip()

    def difficulty_menu():
        while True:
            draw_difficulty_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_easy.collidepoint(event.pos):
                        return 10, 10, 10
                    elif button_medium.collidepoint(event.pos):
                        return 16, 16, 40
                    elif button_hard.collidepoint(event.pos):
                        return 20, 20, 80

    def mode_menu():
        while True:
            draw_mode_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ai.collidepoint(event.pos):
                        return True
                    elif button_manual.collidepoint(event.pos):
                        return False

    # First: choose difficulty → (rows, cols, mines)
    difficulty_result = difficulty_menu()
    if difficulty_result is None:
        return

    size_rows, size_cols, minesNum = difficulty_result

    # Then: choose mode → use_solver True/False
    use_solver = mode_menu()
    if use_solver is None:
        return

    # Set game config
    size = (size_rows, size_cols)
    board = Board(size, minesNum)
    game = Game(board, screenSize)

    # Start game
    game.run(use_solver=use_solver)
    pygame.quit()


if __name__ == "__main__":
    main()
