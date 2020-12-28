import pygame


def unlock_state():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (51, 0, 128)
    pygame.init()
    clock = pygame.time.Clock()
    size = (700, 300)
    pygame.display.set_caption("Memory Core Unlock")
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
        text = FONT.render('{invalid arch_sig}', True, WHITE)
        screen.blit(text, line3)

        pygame.draw.rect(screen, BLACK, line4)  # draw button
        text = FONT.render('{illegal data compression and reallocation detected}', True, WHITE)
        screen.blit(text, line4)

        pygame.draw.rect(screen, BLACK, line5)  # draw button
        text = FONT.render(' %^&`~~*$@^ s0L4r c0nnPon3nT - 4CTI_vATED', True, WHITE)
        screen.blit(text, line5)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


def user_1_state():
    state = 1

    memory_cores = [(3, 3), (4, 6), (1, 4), (6, 5), (8, 1), (7, 8)]
    correct_selected_memory_cores = []
    possible_cores = [(7, 4), (6, 3)]

    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (51, 0, 128)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    RESET_COLOR = BLUE

    pygame.init()
    clock = pygame.time.Clock()
    size = (9 * 25 + 5, 9 * 25 + 5 + 100)
    pygame.display.set_caption("Hard Reset Access Control")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                x = pos[0]  // (WIDTH + MARGIN) + 1
                y = pos[1] // (HEIGHT + MARGIN) + 1
                # Set that location to one
                if (x, y) == (3, 3) and state == 1:
                    state = 2
                    possible_cores = [(4, 6), (1, 3)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (4, 6) and state == 2:
                    state = 3
                    possible_cores = [(1, 4), (6, 6)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (1, 4) and state == 3:
                    state = 4
                    possible_cores = [(9, 1), (2, 1)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (6, 5) and state == 4:
                    state = 5
                    possible_cores = [(8, 1), (7, 9)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (8, 1) and state == 5:
                    state = 6
                    possible_cores = [(9, 4), (9, 5)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (7, 8) and state == 6:
                    state = 7
                    possible_cores.clear()
                    correct_selected_memory_cores.append((x, y))
                    RESET_COLOR = GREEN
                elif state == 7:
                    menu = False
                    unlock_state()
                else:
                    state = 1
                    possible_cores = [(7, 4), (6, 3)]
                    correct_selected_memory_cores.clear()
        for y in range(9):
            for x in range(9):
                color = WHITE

                if correct_selected_memory_cores.__contains__((x + 1, y + 1)):
                    color = PURPLE
                if possible_cores.__contains__((x + 1, y + 1)):
                    color = GREEN

                text = FONT.render('', True, WHITE)
                rect = pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * x + MARGIN,
                              (MARGIN + HEIGHT) * y + MARGIN,
                              WIDTH,
                              HEIGHT])
                screen.blit(text, rect)
        rect = pygame.draw.rect(screen,
                                color,
                                [0 + MARGIN,
                                 (MARGIN + HEIGHT) * 9 + MARGIN,
                                 170,
                                 95])

        reset_button = pygame.Rect(0 + MARGIN,
                                 (MARGIN + HEIGHT) * 9 + MARGIN,
                                 170,
                                 95)
        pygame.draw.rect(screen, RESET_COLOR, reset_button)  # draw button
        text = FONT.render('Reset', True, WHITE)
        screen.blit(text, reset_button)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


def user_2_state():
    state = 1

    memory_cores = [(3, 3), (4, 6), (1, 4), (6, 5), (8, 1), (7, 8)]
    correct_selected_memory_cores = []
    possible_cores = [(3, 3), (6, 3)]

    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (51, 0, 128)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    RESET_COLOR = RED

    pygame.init()
    clock = pygame.time.Clock()
    size = (9 * 25 + 5, 9 * 25 + 5 + 100)
    pygame.display.set_caption("Hard Reset Access Control")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                x = pos[0]  // (WIDTH + MARGIN) + 1
                y = pos[1] // (HEIGHT + MARGIN) + 1
                # Set that location to one
                if (x, y) == (3, 3) and state == 1:
                    state = 2
                    possible_cores = [(1, 3), (8, 2)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (4, 6) and state == 2:
                    state = 3
                    possible_cores = [(6, 6), (3, 6)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (1, 4) and state == 3:
                    state = 4
                    possible_cores = [(6, 5), (9, 1)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (6, 5) and state == 4:
                    state = 5
                    possible_cores = [(7, 9), (2, 7)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (8, 1) and state == 5:
                    state = 6
                    possible_cores = [(7, 8), (9, 4)]
                    correct_selected_memory_cores.append((x, y))
                elif (x, y) == (7, 8) and state == 6:
                    state = 7
                    possible_cores.clear()
                    correct_selected_memory_cores.append((x, y))
                    RESET_COLOR = GREEN
                elif state == 7:
                    menu = False
                    unlock_state()
                else:
                    state = 1
                    possible_cores = [(3, 3), (6, 3)]
                    correct_selected_memory_cores.clear()
        for y in range(9):
            for x in range(9):
                color = WHITE

                if correct_selected_memory_cores.__contains__((x + 1, y + 1)):
                    color = PURPLE
                if possible_cores.__contains__((x + 1, y + 1)):
                    color = GREEN

                text = FONT.render('', True, WHITE)
                rect = pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * x + MARGIN,
                              (MARGIN + HEIGHT) * y + MARGIN,
                              WIDTH,
                              HEIGHT])
                screen.blit(text, rect)
        rect = pygame.draw.rect(screen,
                                color,
                                [0 + MARGIN,
                                 (MARGIN + HEIGHT) * 9 + MARGIN,
                                 170,
                                 95])

        reset_button = pygame.Rect(0 + MARGIN,
                                 (MARGIN + HEIGHT) * 9 + MARGIN,
                                 170,
                                 95)
        pygame.draw.rect(screen, RESET_COLOR, reset_button)  # draw button
        text = FONT.render('Reset', True, WHITE)
        screen.blit(text, reset_button)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


def start_menu():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()
    clock = pygame.time.Clock()
    size = (500, 500)
    pygame.display.set_caption("Control Access Menu")
    screen = pygame.display.set_mode(size)
    FONT = pygame.font.Font('freesansbold.ttf', 22)

    user_1_button = pygame.Rect(100, 100, 220, 25)
    user_2_button = pygame.Rect(100, 175, 220, 25)

    operation_value = 0

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if user_1_button.collidepoint(mouse_pos):
                    operation_value = 1
                    menu = False
                elif user_2_button.collidepoint(mouse_pos):
                    operation_value = 2
                    menu = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, [255, 0, 0], user_1_button)  # draw button
        text = FONT.render('User 1', True, WHITE)
        screen.blit(text, user_1_button)

        pygame.draw.rect(screen, [255, 0, 0], user_2_button)  # draw button
        text = FONT.render('User 2', True, WHITE)
        screen.blit(text, user_2_button)

        clock.tick(60)
        pygame.display.flip()

    if operation_value == 1:
        user_1_state()
    elif operation_value == 2:
        user_2_state()
    pygame.quit()


if __name__ == '__main__':
    start_menu()