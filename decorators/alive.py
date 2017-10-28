def alive(func):
    def decorator(self, *args, **kwargs):
        if self.is_dead is not True:
            func(self, *args, **kwargs)

    return decorator
