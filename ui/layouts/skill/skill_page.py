from pygame.surface import Surface

from decorators.delay import delay
from decorators.propagate_event import propagate_event
from keyboard.keys import Keys
from render.render import Render
from render.tween import Tween
from skill.skill_manager import SkillManager
from ui.components.carousel import Carousel
from ui.components.image import Image
from ui.components.label import Label
from ui.faded_element import FadedElement
from ui.layouts.skill.skill_group import SkillGroup as SkillGroupElement
from ui.layouts.skill.skill_view import SkillView

import pygame.locals as pg_vars


@propagate_event
class SkillPage(FadedElement):
    color_key = (240, 240, 240)
    ui_event = True
    selected_index = 0

    def __init__(self, game):
        super().__init__(game, game.width / 2, game.height / 2, game.width, game.height)
        self.elements = []
        self.update_while_tween = False
        self.in_tween = False

        margin_top = 50
        margin_left = 100

        carousel_width = SkillView.width * 3 + SkillGroupElement.gap * 2

        group_elements = []

        for skill_group in SkillManager.get_instance().groups.values():
            group = SkillGroupElement(game, margin_left + 50, 0, skill_group, self)
            group_elements.append(group)

        self.carousel = Carousel(
            game, margin_left + 50, margin_top + 300,
            carousel_width, SkillView.height, group_elements
        )

        self.skill_name = Tween(
            Label(
                self.game,
                margin_left + carousel_width + 300,
                margin_top, 350, 80, "<>", 80,
                color=(52, 152, 219)
            ).set_fade_tick(30, "pause"),
            {'opacity': 255}, []
        )

        self.font = Render.load_font()

        empty_surface = Surface((500, self.game.height - margin_top - 150))
        empty_surface.set_colorkey((240, 240, 240))
        empty_surface.fill((240, 240, 240))
        empty_surface.set_alpha(0)

        self.skill_desc = Tween(
            Image(
                self.game,
                margin_left + carousel_width + 300,
                margin_top + 150,
                empty_surface
            ),
            {'opacity': 255}, []
        )
        self.update_skill()

        self.elements.extend((
            self.carousel,
            Label(self.game, margin_left, margin_top, 250, 50, "SkillTree", 50).set_fade_tick(30, "pause"),
            self.skill_name,
            self.skill_desc
        ))

    def do_render(self, renderer):
        renderer.fill((239, 239, 239))
        for element in self.elements:
            if isinstance(element, Tween):
                element.update()
                element.element\
                    .set_fade_tick(element.value['opacity'] / 255 * element.element.max_fade_tick, "pause")\
                    .render(renderer)

            else:
                element.render(renderer)

    def do_update_event(self, ev):
        skill_update = False

        if ev.type == pg_vars.KEYDOWN:
            if ev.key == Keys.KEY_SKILL_UI_RIGHT:
                skill_update = True
                self.selected_index += 1

                if self.carousel.activated_element.length is not None:
                    if self.selected_index >= self.carousel.activated_element.length:
                        self.selected_index = self.selected_index % self.carousel.activated_element.length

            elif ev.key == Keys.KEY_SKILL_UI_LEFT:
                skill_update = True
                self.selected_index = self.selected_index - 1

                if self.selected_index < 0:
                    self.selected_index += self.carousel.activated_element.length

            elif ev.key == Keys.KEY_SKILL_UI_UP or ev.key == Keys.KEY_SKILL_UI_DOWN:
                skill_update = True

        if skill_update:
            self.update_skill()

    def update_skill(self):
        if self.in_tween:
            self.update_while_tween = True
            return

        self.in_tween = True

        def callback():
            self.skill_name.set_value('opacity', 255, 10)
            self.skill_desc.set_value('opacity', 255, 10)

            if self.current_activated_skill is not None:
                skill_name = "<%s>" % self.current_activated_skill.name
                skill_desc = self.current_activated_skill.description

            else:
                skill_name = ''
                skill_desc = ''

            self.skill_name.element.set_text(skill_name)
            self.skill_desc.element.image = Render.get_paragraph_text(
                skill_desc,
                self.font,
                self.skill_desc.element.image.get_width(),
                self.skill_desc.element.image.get_height(),
                color=(52, 152, 219)
            )

            if self.update_while_tween:
                @delay(.1)
                def new_update():
                    self.in_tween = False
                    self.update_while_tween = False
                    self.update_skill()

                new_update()

            else:
                self.in_tween = False

        self.skill_name.set_callback(callback, True)
        self.skill_name.set_value('opacity', 0, 10)
        self.skill_desc.set_value('opacity', 0, 10)

    @property
    def current_activated_skill(self):
        skill = self.carousel.activated_element.selected_skill

        if skill is None:
            return None

        return SkillManager.get_instance().skills[skill]
