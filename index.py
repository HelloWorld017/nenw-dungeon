from game import Game
from player import Player
from ui.health_bar import HealthBar
from ui.title import Title

import pygame

FPS = 60

game = Game()
player = Player(game)
player.spawn()

clock = pygame.time.Clock()

title = Title(game).show()

while True:
    game.update(pygame.event.get())
    game.render()

    if game.tick > 60 and not title.is_hidden:
        title.hide()
        HealthBar(game, 50, 50, player).show()

    clock.tick(FPS)
