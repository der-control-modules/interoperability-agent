import abc

# def _adjust_name(ieee1547_name: str):  # TODO: This function is not currently used. Remove it does not find a use.
#     return ieee1547_name.lower().replace('(', '').replace(')', '').replace(' ', '_')


class Transform:
    KNOWN_TRANSFORMS = {}

    def __init__(self, ieee1547_name, mapped_points, writable, target_mapping):
        self.ieee1547_name = ieee1547_name
        self._mapped_points = mapped_points
        self.target_mapping = target_mapping
        self.writable = writable

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self, value):
        pass

    @property
    def mapped_points(self):
        return self._mapped_points

    @classmethod
    def add_transforms(cls, transforms):
        cls.KNOWN_TRANSFORMS.update(transforms)

    @classmethod
    def factory(cls, transform_type, ieee1547_name, mapped_points, writable, target_mapping):
        if transform_type in cls.KNOWN_TRANSFORMS:
            return cls.KNOWN_TRANSFORMS[transform_type](ieee1547_name, mapped_points, writable, target_mapping)


class MapList(Transform):
    def __init__(self, ieee1547_name, mapped_points, target_mapping):
        super(MapList, self).__init__(ieee1547_name, mapped_points, target_mapping)

    def read(self):
        return [self.target_mapping[point] for point in self.mapped_points]

    def write(self, values):
        ret_dict = {}
        if not isinstance(values, list) and len(self.mapped_points) == len(values):
            raise ValueError(f'{self.ieee1547_name} requires {len(self.mapped_points)} values. Received {len(values)}')
        for i, point in enumerate(self.mapped_points):
            ret_dict[point] = values[i]
        return ret_dict


class OneToOne(Transform):
    def __init__(self, ieee1547_name, mapped_points, target_mapping):
        super(OneToOne, self).__init__(ieee1547_name, mapped_points, target_mapping)

    def read(self):
        return {self.ieee1547_name: self.target_mapping[self.mapped_points[0]]}

    def write(self, values):
        ret_dict = {}
        if not len(self.mapped_points) == 1:
            raise ValueError(f'{self.ieee1547_name} requires one value. Received {len(values)}')
        ret_dict[self.mapped_points[0]] = values
        return ret_dict


class Broadcast(Transform):
    def __init__(self, ieee1547_name, mapped_points, target_mapping):
        super(Broadcast, self).__init__(ieee1547_name, mapped_points, target_mapping)

    def read(self):
        mapped_values = [self.target_mapping[point] for point in self.mapped_points]
        if isinstance(mapped_values[0], bool):
            return all(mapped_values)
        else:
            # TODO: Are there other types than bool it makes sense to handle? Is this used for anything but booleans?
            return mapped_values[0]

    def write(self, values):
        ret_dict = {}
        for point in self.mapped_points:
            ret_dict[point] = values
        return ret_dict

Transform.add_transforms({
    'map_list': MapList,
    'one_to_one': OneToOne,
    'broadcast': Broadcast
})
