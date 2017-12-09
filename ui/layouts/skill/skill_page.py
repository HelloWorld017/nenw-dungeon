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

        self.empty_surface = empty_surface

        self.skill_desc = Tween(
            Image(
                self.game,
                margin_left + carousel_width + 300,
                margin_top + 150,
                empty_surface
            ),
            {'opacity': 255}, []
        )

        self.skill_price = Tween(
            Label(
                self.game,
                margin_left + carousel_width + 300,
                margin_top + 150 + 150, 350, 80, "필요 SP   1", 32,
                color=(52, 152, 219)
            ).set_fade_tick(30, "pause"),
            {'opacity': 255}, []
        )

        self.current_sp = Tween(
            Label(
                self.game,
                margin_left + carousel_width + 300,
                margin_top + 150 + 150 + 40, 350, 80, "현재 SP   0", 32,
                color=(52, 152, 219)
            ).set_fade_tick(30, "pause"),
            {'opacity': 255}, []
        )

        self.skill_score = Tween(
            Label(
                self.game,
                margin_left + carousel_width + 300 + 500 - 250,
                margin_top + 150 + 150, 350, 80, "필요 점수   0", 32,
                color=(52, 152, 219)
            ).set_fade_tick(30, "pause"),
            {'opacity': 255}, []
        )

        self.current_score = Tween(
            Label(
                self.game,
                margin_left + carousel_width + 300 + 500 - 250,
                margin_top + 150 + 150 + 40, 350, 80, "현재 점수   0", 32,
                color=(52, 152, 219)
            ).set_fade_tick(30, "pause"),
            {'opacity': 255}, []
        )

        self.buy_button_image = Surface((500, 100))
        Render(self.buy_button_image)\
            .fill((52, 152, 219))\
            .write_text(250, 50, "Enter 키로 구매", color=(240, 240, 240), size=50)

        self.disabled_button_image = Surface((500, 100))
        Render(self.disabled_button_image)\
            .fill((220, 220, 220))\
            .write_text(250, 50, "구매할 수 없음", color=(180, 180, 180), size=50)

        self.already_bought_button_image = Surface((500, 100))
        Render(self.already_bought_button_image)\
            .fill((220, 220, 220))\
            .write_text(250, 50, "이미 구매함", color=(180, 180, 180), size=50)

        self.buy_button = Tween(
            Image(
                self.game,
                margin_left + carousel_width + 300,
                margin_top + 150 + 150 + 40 + 100,
                self.buy_button_image
            ),
            {'opacity': 255}, []
        )

        self.skill_ui = [
            self.skill_name,
            self.skill_desc,
            self.skill_price,
            self.current_sp,
            self.skill_score,
            self.current_score,
            self.buy_button
        ]

        self.update_skill()

        self.elements.extend((
            self.carousel,
            Label(self.game, margin_left, margin_top, 250, 50, "SkillTree", 50).set_fade_tick(30, "pause")
        ))

        self.elements.extend(self.skill_ui)

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

        player = self.game.players[0]

        def callback():
            for skill_elem in self.skill_ui:
                skill_elem.set_value('opacity', 255, 10)

            if self.current_activated_skill is not None:
                skill_name = "<%s>" % self.current_activated_skill.name
                skill_desc = self.current_activated_skill.description
                if player.point < 1:
                    self.current_sp.element.set_color((255, 87, 34))
                else:
                    self.current_sp.element.set_color((52, 152, 219))

                self.current_sp.element.set_text("현재 SP   %d" % player.point)

                if player.score < self.current_activated_skill.require_score:
                    self.current_score.element.set_color((255, 87, 34))
                else:
                    self.current_score.element.set_color((52, 152, 219))

                self.current_score.element.set_text("현재 점수   %d" % player.score)

                self.skill_price.element.set_text('필요 SP   1')
                self.skill_score.element.set_text('필요 점수   %d' % self.current_activated_skill.require_score)

                if self.current_activated_skill.activated:
                    self.buy_button.element.image = self.already_bought_button_image

                elif self.current_activated_skill.can_activate(player):
                    self.buy_button.element.image = self.buy_button_image

                else:
                    self.buy_button.element.image = self.disabled_button_image

            else:
                skill_name = ''
                skill_desc = ''
                self.skill_price.element.set_text('')
                self.skill_score.element.set_text('')
                self.current_sp.element.set_text('')
                self.current_score.element.set_text('')

                self.buy_button.element.image = self.empty_surface

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
        for skill in self.skill_ui:
            skill.set_value('opacity', 0, 10)

    @property
    def current_activated_skill(self):
        skill = self.carousel.activated_element.selected_skill

        if skill is None:
            return None

        return SkillManager.get_instance().skills[skill]
