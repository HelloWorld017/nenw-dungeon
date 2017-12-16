import threading
from functools import wraps


def delay(delay_tick=0.):
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay_tick, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap
