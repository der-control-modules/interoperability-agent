from typing import Iterable

from interoperability.interoperable_target import InteroperableTarget


class IEEE_1815_2(InteroperableTarget):
    def __init__(self, **kwargs):
        super(IEEE_1815_2, self).__init__(**kwargs)

    def poll_values(self, point_names: Iterable) -> bool:
        pass

    def set_values(self, request_dict: dict[str, any]) -> bool:
        pass

    MAPPING = {}