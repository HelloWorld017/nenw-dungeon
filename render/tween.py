from decorators.chain import chain


class Tween(object):
    ui_event = True

    def __init__(self, element, value, copying_values):
        self.value = value
        self.motion = dict(map(lambda item: (item[0], 0), value.items()))
        self.target = self.value.copy()
        self.copying_values = copying_values
        self.element = element
        self.on_finish = lambda: None
        self.on_update = lambda ev: None
        self.callback_once = True

    def update(self):
        for key, value in self.value.items():
            if self.motion[key] == 0:
                continue

            if abs(self.target[key] - self.value[key]) < abs(self.motion[key]):
                self.value[key] = self.target[key]
                self.motion[key] = 0
                self.on_finish()

                if self.callback_once:
                    self.on_finish = lambda: None

            else:
                self.value[key] += self.motion[key]

        for key in self.copying_values:
            setattr(self.element, key, self.value[key])

    @chain
    def set_value(self, key, value, time):
        self.target[key] = value
        self.motion[key] = (self.target[key] - self.value[key]) / time
        if self.motion[key] == 0:
            self.motion[key] = 1e-5

    @chain
    def set_callback(self, callback, once=True):
        self.on_finish = callback
        self.callback_once = once

    @chain
    def set_on_update(self, callback):
        self.on_update = callback

    def update_event(self, event):
        self.on_update(event)
