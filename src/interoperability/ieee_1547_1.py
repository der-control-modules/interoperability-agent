from .interoperable_target import InteroperableTarget


class IEEE_1547_1(InteroperableTarget):
    def __init__(self, **kwargs):
        super(IEEE_1547_1, self).__init__(**kwargs)
