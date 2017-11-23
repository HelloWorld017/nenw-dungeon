import pygame

from game import Game
from player import Player
from ui.components.title import Title

FPS = 60

game = Game()

clock = pygame.time.Clock()

title = Title(game).show()

while True:
    game.update(pygame.event.get())
    game.render()

    if game.tick > 60 and not title.is_hidden:
        title.hide()
        player = Player(game)
        player.spawn()

    clock.tick(FPS)
