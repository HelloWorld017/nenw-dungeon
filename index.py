from game import Game
from player import Player
from pattern.pattern_thorn import PatternThorn
from ui.health_bar import HealthBar

import pygame

FPS = 60

game = Game()
player = Player(game)
player.spawn()

clock = pygame.time.Clock()

pattern = PatternThorn(game, player)
pattern.activate()

HealthBar(game, 50, 50, player).show()

while True:
    game.update(pygame.event.get())
    game.render()
    clock.tick(FPS)
