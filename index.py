from game import Game
from player import Player
import pygame


game = Game()
player = Player(game)
player.spawn()

clock = pygame.time.Clock()

while True:
    game.update(pygame.event.get())
    game.render()
    clock.tick(60)
