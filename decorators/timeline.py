def timeline(property_name="entity_inner_tick"):
    def timeline_decorator(cls):
        def update_timeline(self):
            if getattr(self, property_name) in self.timeline:
                for event in self.timeline[getattr(self, property_name)]:
                    event()

                del self.timeline[getattr(self, property_name)]

        def register_event(self, delta, callback):
            tick = getattr(self, property_name) + delta

            if tick not in self.timeline:
                self.timeline[tick] = []

            self.timeline[tick].append(callback)

        cls.register_event = register_event
        cls.update_timeline = update_timeline
        cls.timeline = {}

        return cls

    return timeline_decorator
