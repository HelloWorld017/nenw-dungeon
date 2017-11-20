import sys

import pygame
import pygame.locals as pg_vars

from pattern.pattern_thorn import PatternThorn
from pattern.pattern_circular import PatternCircular

from keyboard.keys import Keys
from render.render import Render


class Game(object):
    entities = {}
    players = []
    death_note = []
    last_entity_id = 0
    key_maps = dict.fromkeys(Keys.list_keys(), False)
    width = 1280
    height = 720
    patterns = []
    pre_ui = []
    ui = []

    def __init__(self):
        self.tick = 0
        pygame.init()

        screen = pygame.display.set_mode(
            (self.width, self.height),
            pg_vars.DOUBLEBUF
        )

        pygame.display.set_caption('Hello World!')

        self.renderer = Render(screen)

    def handle_event(self, event):
        if event.type is pg_vars.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type is pg_vars.KEYDOWN:
            if event.key in self.key_maps:
                self.key_maps[event.key] = True

            if event.key == pg_vars.K_t:
                pattern = PatternThorn(self, self.players[0])
                pattern.activate()

            elif event.key == pg_vars.K_c:
                pattern = PatternCircular(self, self.players[0])
                pattern.activate()

        elif event.type is pg_vars.KEYUP:
            if event.key in self.key_maps:
                self.key_maps[event.key] = False

    def update(self, events):
        self.tick += 1

        for event in events:
            self.handle_event(event)

        for e in self.entities.values():
            e.update(events)

        for pattern in self.patterns:
            pattern.update()

        for death in self.death_note:
            self.entities.pop(death)

        self.death_note = []

    def render(self):
        self.render_background()

        for element in self.pre_ui:
            element.render(self.renderer)

        for entity in self.entities.values():
            entity.render(self.renderer)

        for element in self.ui:
            element.render(self.renderer)

        self.renderer.update()

    def render_background(self):
        self.renderer.fill((240, 240, 240))

