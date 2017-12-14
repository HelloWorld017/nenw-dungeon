import sys

import pygame
import pygame.locals as pg_vars

from pattern.pattern_rain import PatternRain
from pattern.pattern_thorn import PatternThorn
from pattern.pattern_circular import PatternCircular
from pattern.pattern_laser import PatternLaser

from keyboard.keys import Keys
from pattern.pattern_triangle import PatternTriangle
from pattern.pattern_turret import PatternTurret
from render.render import Render
from skill.skill_loader import register_all_skills


class Game(object):
    entities = {}
    players = []
    mobs = []
    death_note = []
    life_note = []
    last_entity_id = 0
    key_maps = dict.fromkeys(Keys.list_keys(), False)
    width = 1280
    height = 720
    background = (240, 240, 240)
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

        pygame.display.set_caption('orange:phobia')

        self.renderer = Render(screen)
        register_all_skills()

        self.skill_ui = None

    def handle_event(self, event):
        for elem in self.ui:
            if elem.ui_event:
                elem.update_event(event)

        if event.type is pg_vars.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type is pg_vars.KEYDOWN:
            if event.key in self.key_maps:
                self.key_maps[event.key] = True

            if event.key == pg_vars.K_1:
                PatternThorn(self, self.players[0]).activate()

            elif event.key == pg_vars.K_2:
                PatternCircular(self, self.players[0]).activate()

            elif event.key == pg_vars.K_3:
                PatternLaser(self, self.players[0]).activate()

            elif event.key == pg_vars.K_4:
                PatternTriangle(self, self.players[0]).activate()

            elif event.key == pg_vars.K_5:
                PatternTurret(self, self.players[0]).activate()

            elif event.key == pg_vars.K_6:
                PatternRain(self, self.players[0]).activate()

            elif event.key == Keys.KEY_SKILL_UI_TOGGLE:
                self.toggle_skill_window()

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
            if death in self.entities:
                death_entity = self.entities[death]

                del self.entities[death]

                if death_entity in self.mobs:
                    self.mobs.remove(death_entity)

        for life in self.life_note:
            life.entity_id = self.last_entity_id
            self.last_entity_id += 1
            self.entities[life.entity_id] = life

        self.life_note = []
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
        self.renderer.fill(self.background)

    def toggle_skill_window(self):
        if self.skill_ui is None:
            return

        if self.skill_ui.is_hidden:
            self.skill_ui.show()

        else:
            self.skill_ui.hide()
