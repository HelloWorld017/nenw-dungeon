def propagate_event(cls):
    def update_event(self, ev):
        if hasattr(self, 'do_update_event'):
            self.do_update_event(ev)

        for elem in self.elements:
            if elem.ui_event:
                elem.update_event(ev)

    cls.update_event = update_event

    return cls
