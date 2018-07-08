import random
import sys

import pygame
import pygame.locals as pg_vars

from decorators.delay import delay
from pattern.pattern_drop import PatternDrop
from pattern.pattern_fakey import PatternFakey
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
    passed_patterns = 0
    patterns = []
    avail_patterns_easy = [
        PatternThorn, PatternRain, PatternFakey
    ]
    avail_patterns_normal = [
        PatternCircular, PatternDrop, PatternLaser
    ]
    avail_patterns_hard = [
        PatternTurret, PatternTriangle
    ]
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

            elif event.key == Keys.KEY_SKILL_UI_TOGGLE:
                # self.toggle_skill_window()
                pass

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

    def new_pattern(self, end=True):
        if len(self.players) < 1:
            return

        if end:
            self.players[0].score += 100
            self.passed_patterns += 1

        @delay(1)
        def start_pattern():
            if len(self.players) < 1:
                return

            if self.passed_patterns < 4:
                if random.randint(0, 10) >= 4:
                    chosen_pattern = random.choice(self.avail_patterns_easy)

                else:
                    chosen_pattern = random.choice(self.avail_patterns_normal)

            elif self.passed_patterns < 7:
                if random.randint(0, 10) >= 4:
                    chosen_pattern = random.choice(self.avail_patterns_normal)

                else:
                    chosen_pattern = random.choice(self.avail_patterns_easy)

            else:
                if random.randint(0, 10) >= 4:
                    chosen_pattern = random.choice(self.avail_patterns_hard)

                elif random.randint(0, 10) >= 8:
                    chosen_pattern = random.choice(self.avail_patterns_easy)
                    
                else:
                    chosen_pattern = random.choice(self.avail_patterns_normal)

            chosen_pattern(self, self.players[0]).activate()

        start_pattern()
