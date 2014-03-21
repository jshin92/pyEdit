import pygame
KEY_THRESHOLD = 15
TAB_STOP = 4
BLACK = (0, 0, 0)


class Text:
    def __init__(self, cursor, font, font_size, screen):
        self.text = [""]
        self.cur_line = 0
        self.cur_ticks = 0
        self.cur_unicode = ''
        self.cur_key = 0
        self.cursor = cursor
        self.font = font
        self.font_size = font_size
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            self.cur_ticks = 1
            self.cur_key = event.key
            self.cur_unicode = event.unicode
            self.handle_key_input(event.key, event.unicode)
        elif event.type == pygame.KEYUP:
            self.cur_ticks = 0
        return False

    def check_ticks(self):
        # start keeping track of ticks if being held down
        if self.cur_ticks > 0:
            self.cur_ticks += 1
        # press that key if it exceeds a certain threshold
        if self.cur_ticks > KEY_THRESHOLD:
            self.handle_key_input(self.cur_key, self.cur_unicode)

    def draw(self):
        for i in range(self.cur_line + 1):
            label = self.font.render(self.text[i], 1, BLACK)
            self.screen.blit(label, (0, self.font_size * i))

    def handle_key_input(self, key, unicode):
        if key == pygame.K_TAB:
            self.text[self.cur_line] += '    '
            self.cursor.x += TAB_STOP
        elif key == pygame.K_RETURN:
            self.text.append('')
            self.cur_line += 1
            self.cursor.y += 1
            self.cursor.x = 0
        elif key == pygame.K_BACKSPACE:
            self.handle_backspace()
            if self.cursor.x > 0:
                self.cursor.x -= 1
        else:
            self.text[self.cur_line] += unicode
            # don't advance cursor if pressing shift
            if key != pygame.K_LSHIFT and key != pygame.K_RSHIFT and key != pygame.K_CAPSLOCK:
                self.cursor.x += 1

    def handle_backspace(self):
        if len(self.text[self.cur_line]) == 0 and self.cur_line != 0:
            del self.text[self.cur_line]
            self.cur_line -= 1
            self.cursor.y -= 1
            self.cursor.x = len(self.text[self.cur_line]) + 1
        else:
            self.text[self.cur_line] = self.text[self.cur_line][0:-1]
