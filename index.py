import pygame

from game import Game
from player import Player
from ui.components.score import Score
from ui.components.title import Title
from ui.layouts.skill.skill_page import SkillPage

FPS = 60

game = Game()
clock = pygame.time.Clock()
title = Title(game).show()
player = None

while True:
    game.update(pygame.event.get())
    game.render()

    if game.tick > 60 and not title.is_hidden:
        title.hide()
        player = Player(game)
        player.spawn()
        game.skill_ui = SkillPage(game)
        Score(game, player).show()
        game.new_pattern(end=False)

    if player is not None and player.is_dead:
        print("kakin:do-method:score:%d" % player.score)
        break

    clock.tick(FPS)
