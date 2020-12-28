import random

import pygame


class FreqState:

    def __init__(self, board_size: int, frequency: int, turns: int):

        self.board_size = board_size

        # GAME MECHANIC: Admin and Operators must select the same frequency
        self.frequency = frequency
        # Expected number of turns in game
        self.turns = turns
        # Correct tiles in order of turn; Generated when frequency is selected
        self.valid_tiles = []
        # Win condition if = 1
        self.COMPLETE_FLAG = 0
        # Color flag order for operator
        self.color_order = []

    def gen_color_order(self):
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        self.color_order.clear()
        random.seed(self.frequency)
        for i in range(self.turns):
            coin = random.randint(0, 1)
            if coin == 0:
                self.color_order.append(RED)
            elif coin == 1:
                self.color_order.append(BLUE)

    def gen_valid_tiles(self):

        self.valid_tiles.clear()
        random.seed(self.frequency)

        for i in range(self.turns):
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            pt_set = (x, y)

            if self.valid_tiles.__contains__(pt_set):
                i += -1

            else:
                self.valid_tiles.append(pt_set)


def unlock_PANEL():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (51, 0, 128)
    pygame.init()
    clock = pygame.time.Clock()
    size = (700, 300)
    pygame.display.set_caption("Component Core Unlock")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)
    line1 = pygame.Rect(100, 100, 220, 25)
    line2 = pygame.Rect(100, 125, 220, 25)
    line3 = pygame.Rect(100, 150, 220, 25)
    line4 = pygame.Rect(100, 175, 220, 25)
    line5 = pygame.Rect(100, 200, 220, 25)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLACK, line1)  # draw button
        text = FONT.render('[Auxillary Support Software Detected]', True, WHITE)
        screen.blit(text, line1)

        pygame.draw.rect(screen, BLACK, line2)  # draw button
        text = FONT.render('Initializing...', True, WHITE)
        screen.blit(text, line2)

        pygame.draw.rect(screen, BLACK, line3)  # draw button
        text = FONT.render('{validating arch_sig...}', True, WHITE)
        screen.blit(text, line3)

        pygame.draw.rect(screen, BLACK, line4)  # draw button
        text = FONT.render('{verified: port auxiliary operating at 80% power}', True, WHITE)
        screen.blit(text, line4)

        pygame.draw.rect(screen, BLACK, line5)  # draw button
        text = FONT.render('== MKII FR0ZT-LZR ACTIVATED ==', True, WHITE)
        screen.blit(text, line5)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


def control_PANEL():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    clock = pygame.time.Clock()
    size = (500, 500)
    pygame.display.set_caption("Control Access Menu")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    hard_reset_button = pygame.Rect(100, 100, 220, 25)
    operation_value = 0

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if hard_reset_button.collidepoint(mouse_pos):
                    operation_value = 1
                    menu = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, [255, 0, 0], hard_reset_button)  # draw button
        text = FONT.render('Hard Reset', True, WHITE)
        screen.blit(text, hard_reset_button)

        clock.tick(60)
        pygame.display.flip()

    if operation_value == 1:
        pygame.quit()
        frequency_selection_PANEL()
    pygame.quit()


def frequency_selection_PANEL():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    clock = pygame.time.Clock()
    size = (500, 500)
    pygame.display.set_caption("Synchronizing with Operators...")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    increase_freq = pygame.Rect(100, 0, 300, 100)
    decrease_freq = pygame.Rect(100, 400, 300, 100)
    freq_button = pygame.Rect(100, 150, 300, 200)
    frequency = 25

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if increase_freq.collidepoint(mouse_pos):
                    frequency += 2
                elif decrease_freq.collidepoint(mouse_pos):
                    frequency += -2
                elif freq_button.collidepoint(mouse_pos):
                    start_state = FreqState(7, int(frequency), 7)
                    start_state.gen_valid_tiles()
                    start_state.gen_color_order()
                    pygame.quit()
                    memory_sequence_PANEL(start_state)

        screen.fill(BLACK)

        FONT = pygame.font.Font('freesansbold.ttf', 22)

        pygame.draw.rect(screen, [255, 0, 0], increase_freq)  # draw button
        text = FONT.render('Increase Frequency', True, WHITE)
        text_rect = text.get_rect(center=(250, 50))
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, [255, 0, 0], decrease_freq)  # draw button
        text = FONT.render('Decrease Frequency', True, WHITE)
        text_rect = text.get_rect(center=(250, 450))
        screen.blit(text, text_rect)

        FONT = pygame.font.Font('freesansbold.ttf', 50)

        pygame.draw.rect(screen, [255, 0, 0], freq_button)  # draw button
        text = FONT.render(str(frequency), True, WHITE)
        text_rect = text.get_rect(center=(250, 250))
        screen.blit(text, text_rect)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


def memory_sequence_PANEL(frequency_state: FreqState):
    # Assets
    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (51, 0, 128)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    RESET_COLOR = frequency_state.color_order[0]

    pygame.init()
    clock = pygame.time.Clock()
    size = (frequency_state.board_size * 25 + 5, frequency_state.board_size * 25 + 5 + 100)
    pygame.display.set_caption("Hard Reset Access Control")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    memory_cores = frequency_state.valid_tiles
    correct_selected_memory_cores = []
    current_turn = 1
    freq_button = pygame.Rect(100 + MARGIN,
                              (MARGIN + HEIGHT) * frequency_state.board_size + MARGIN,
                              (MARGIN + HEIGHT) * (frequency_state.board_size - 4) - MARGIN,
                              95)
    menu = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                x = pos[0] // (WIDTH + MARGIN) + 1
                y = pos[1] // (HEIGHT + MARGIN) + 1

                if freq_button.collidepoint(pos):
                    pygame.quit()
                    frequency_selection_PANEL()

                if frequency_state.COMPLETE_FLAG == 1:
                    unlock_PANEL()
                    pygame.quit()

                if (x - 1, y - 1) == frequency_state.valid_tiles.__getitem__(current_turn - 1):
                    current_turn += 1
                    try:
                        RESET_COLOR = frequency_state.color_order[current_turn - 1]
                    except :
                        RESET_COLOR = GREEN

                    correct_selected_memory_cores.append((x, y))
                    if len(frequency_state.valid_tiles) == len(correct_selected_memory_cores):
                        frequency_state.COMPLETE_FLAG = 1
                else:
                    current_turn = 1
                    RESET_COLOR = frequency_state.color_order[0]
                    correct_selected_memory_cores.clear()

        for y in range(frequency_state.board_size):
            for x in range(frequency_state.board_size):
                color = WHITE

                if correct_selected_memory_cores.__contains__((x + 1, y + 1)):
                    color = PURPLE

                text = FONT.render('', True, WHITE)
                rect = pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN + WIDTH) * x + MARGIN,
                                         (MARGIN + HEIGHT) * y + MARGIN,
                                         WIDTH,
                                         HEIGHT])
                screen.blit(text, rect)

        reset_button = pygame.Rect(0 + MARGIN,
                                   (MARGIN + HEIGHT) * frequency_state.board_size + MARGIN,
                                   95,
                                   95)
        pygame.draw.rect(screen, RESET_COLOR, reset_button)  # draw button
        text = FONT.render('Reset', True, WHITE)
        screen.blit(text, reset_button)

        pygame.draw.rect(screen, GREEN, freq_button)  # draw button
        text = FONT.render('Freq', True, WHITE)
        screen.blit(text, freq_button)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    control_PANEL()
