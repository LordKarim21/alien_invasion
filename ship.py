"""Файл ship.py содержит класс Ship. В этом классе определен метод __init__(),
метод update() для управления позицией корабля и метод blitme() для вывода
изображения корабля на экран. Изображение корабля хранится в файле ship.bmp,
который находится в папке images."""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем."""

    # Добавление изображения корабля 247

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.screen_width = ai_game.settings.screen_width

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
