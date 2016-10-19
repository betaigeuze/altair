# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class Mark(T.Enum):
    """
    One of ['area', 'bar', 'line', 'point', 'text', 'tick', 'rule', 'circle', 'square', 'errorBar']
    """
    def __init__(self, default_value=T.Undefined, **metadata):
        super(Mark, self).__init__(['area', 'bar', 'line', 'point', 'text', 'tick', 'rule', 'circle', 'square', 'errorBar'],
                                    default_value=default_value,
                                    **metadata)