import sys
import pygame
import pygame.locals as pg_vars
from render.render import Render
from keyboard.keys import Keys


class Game(object):
    entities = {}
    last_entity_id = 0
    key_maps = dict.fromkeys(Keys.list_keys(), False)
    width = 1280
    height = 720

    def __init__(self):
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

        elif event.type is pg_vars.KEYUP:
            if event.key in self.key_maps:
                self.key_maps[event.key] = False

    def update(self, events):
        for event in events:
            self.handle_event(event)

        for e in self.entities.values():
            e.update(events)

    def render(self):
        self.render_background()

        for e in self.entities.values():
            e.render(self.renderer)

        self.renderer.update()

    def render_background(self):
        self.renderer.fill((240, 240, 240))
