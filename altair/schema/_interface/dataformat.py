# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .dataformattype import DataFormatType


class DataFormat(BaseObject):
    """Wrapper for Vega-Lite DataFormat definition.
    
    Attributes
    ----------
    feature: Unicode
        The name of the TopoJSON object set to convert to a GeoJSON feature collection.
    mesh: Unicode
        The name of the TopoJSON object set to convert to a mesh.
    parse: Any
        A collection of parsing instructions can be used to define the data types of string-valued attributes in the JSON file.
    property: Unicode
        JSON only) The JSON property containing the desired data.
    type: DataFormatType
        Type of input data: `"json"`, `"csv"`, `"tsv"`.
    """
    feature = T.Unicode(allow_none=True, default_value=None, help="""The name of the TopoJSON object set to convert to a GeoJSON feature collection.""")
    mesh = T.Unicode(allow_none=True, default_value=None, help="""The name of the TopoJSON object set to convert to a mesh.""")
    parse = T.Any(allow_none=True, default_value=None, help="""A collection of parsing instructions can be used to define the data types of string-valued attributes in the JSON file.""")
    property = T.Unicode(allow_none=True, default_value=None, help="""JSON only) The JSON property containing the desired data.""")
    type = DataFormatType(allow_none=True, default_value=None, help="""Type of input data: `"json"`, `"csv"`, `"tsv"`.""")
    
    def __init__(self, feature=None, mesh=None, parse=None, property=None, type=None, **kwargs):
        kwds = dict(feature=feature, mesh=mesh, parse=parse, property=property, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(DataFormat, self).__init__(**kwargs)