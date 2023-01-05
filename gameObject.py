import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, sheet, pos_x, pos_y, game, cols, rows):
        super().__init__(game.player_group, game.all_sprites)
        sheet = game.tile_images[sheet]
        self.frames = []
        self.cut_sheet(sheet, cols, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(game.tile_width * pos_x, game.tile_height * pos_y)
        self.game = game

    def update(self, *args):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update_sprite(self, numSprite):
        self.cur_frame = numSprite
        self.image = self.frames[self.cur_frame % len(self.frames)]
