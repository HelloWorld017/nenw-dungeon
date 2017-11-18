def chain(func):
    def decorator(self, *args, **kwargs):
        func(self, *args, **kwargs)

        return self

    return decorator
