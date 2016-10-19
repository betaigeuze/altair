# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from .unitspec import UnitSpec
from .config import Config
from .data import Data
from .encoding import Encoding
from .mark import Mark
from .transform import Transform


class ExtendedUnitSpec(UnitSpec):
    """Wrapper for Vega-Lite ExtendedUnitSpec definition.
    Schema for a unit Vega-Lite specification, with the syntactic sugar extensions:

- `row` and `column` are included in the encoding.

- (Future) label, box plot



Note: the spec could contain facet.
    Attributes
    ----------
    config: Config
        Configuration object.
    data: Data
        An object describing the data source.
    description: Unicode
        An optional description of this mark for commenting purpose.
    encoding: Encoding
        A key-value mapping between encoding channels and definition of fields.
    height: CFloat
        
    mark: Mark
        The mark type.
    name: Unicode
        Name of the visualization for later reference.
    transform: Transform
        An object describing filter and new field calculation.
    width: CFloat
        
    """
    config = T.Instance(Config, allow_none=True, default_value=None, help="""Configuration object.""")
    data = T.Instance(Data, allow_none=True, default_value=None, help="""An object describing the data source.""")
    description = T.Unicode(allow_none=True, default_value=None, help="""An optional description of this mark for commenting purpose.""")
    encoding = T.Instance(Encoding, allow_none=True, default_value=None, help="""A key-value mapping between encoding channels and definition of fields.""")
    height = T.CFloat(allow_none=True, default_value=None)
    mark = Mark(allow_none=True, default_value=None, help="""The mark type.""")
    name = T.Unicode(allow_none=True, default_value=None, help="""Name of the visualization for later reference.""")
    transform = T.Instance(Transform, allow_none=True, default_value=None, help="""An object describing filter and new field calculation.""")
    width = T.CFloat(allow_none=True, default_value=None)
    
    def __init__(self, config=None, data=None, description=None, encoding=None, height=None, mark=None, name=None, transform=None, width=None, **kwargs):
        kwds = dict(config=config, data=data, description=description, encoding=encoding, height=height, mark=mark, name=name, transform=transform, width=width)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(ExtendedUnitSpec, self).__init__(**kwargs)