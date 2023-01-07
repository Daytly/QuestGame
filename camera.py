class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, game):
        self.dx = 0
        self.dy = 0
        self.game = game

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

        # позиционировать камеру на объекте target

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.game.width // 2) // 8
        self.dy = -(target.rect.y + target.rect.h // 2 - self.game.height // 2) // 8

    def move(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.game.width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.game.height // 2)
