class Tween(object):
    def __init__(self, element, value, copying_values):
        self.value = value
        self.motion = dict(map(lambda item: (item[0], 0), value.iteritems()))
        self.target = self.value.copy()
        self.copying_values = copying_values
        self.element = element
        self.on_finish = lambda: None
        self.callback_once = True

    def update(self):
        for key, value in self.value.items():
            if abs(self.target[key] - self.value[key]) < self.value[key]:
                self.value[key] = self.target[key]
                self.motion[key] = 0
                self.on_finish()

                if self.callback_once:
                    self.on_finish = lambda: None

            else:
                self.value[key] += self.motion[key]

        for key in self.copying_values:
            setattr(self.element, key, self.value[key])

    def set_value(self, key, value, time):
        self.target[key] = value
        self.motion[key] = (self.target[key] - self.value[key]) / time

    def set_callback(self, callback, once=True):
        self.on_finish = callback
        self.callback_once = once
