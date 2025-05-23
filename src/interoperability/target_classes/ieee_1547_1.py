from typing import Dict, Iterable

from interoperability.interoperable_target import InteroperableTarget


class IEEE_1547_1(InteroperableTarget):
    def __init__(self, **kwargs):
        super(IEEE_1547_1, self).__init__(**kwargs)

    def get_values(self, point_names: Iterable) -> bool:
        pass

    def set_values(self, request_dict: Dict[str, any]) -> bool:
        pass

    MAPPING = {}