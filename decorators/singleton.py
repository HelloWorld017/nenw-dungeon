def singleton(cls_object):
    cls_object.__instance = None

    def get_instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.get_instance = classmethod(lambda _class: _class.__instance)

        return cls.__instance

    cls_object.get_instance = classmethod(get_instance)

    return cls_object
