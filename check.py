import pygame


def check(player, enemies) -> bool:
    for i in enemies:
        if pygame.sprite.collide_rect(player, i):
            return True
    return False