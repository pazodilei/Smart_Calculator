# create your dictionary here
from collections.abc import Hashable
objects_dict = {object_: object_.__hash__() for object_ in objects if isinstance(object_, Hashable)}
