# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class DateTime(BaseObject):
    """Wrapper for Vega-Lite DateTime definition.
    Object for defining datetime in Vega-Lite Filter.

If both month and quarter are provided, month has higher precedence.

`day` cannot be combined with other date.

We accept string for month and day names.
    Attributes
    ----------
    date: CFloat
        Integer value representing the date from 1-31.
    day: Union(CFloat, Unicode)
        Value representing the day of week.
    hours: CFloat
        Integer value representing the hour of day from 0-23.
    milliseconds: CFloat
        Integer value representing millisecond segment of a time.
    minutes: CFloat
        Integer value representing minute segment of a time from 0-59.
    month: Union(CFloat, Unicode)
        One of: (1) integer value representing the month from `1`-`12`.
    quarter: CFloat
        Integer value representing the quarter of the year (from 1-4).
    seconds: CFloat
        Integer value representing second segment of a time from 0-59.
    year: CFloat
        Integer value representing the year.
    """
    date = T.CFloat(allow_none=True, default_value=None, max=31, min=1, help="""Integer value representing the date from 1-31.""")
    day = T.Union([T.CFloat(allow_none=True, default_value=None), T.Unicode(allow_none=True, default_value=None)])
    hours = T.CFloat(allow_none=True, default_value=None, max=23, min=0, help="""Integer value representing the hour of day from 0-23.""")
    milliseconds = T.CFloat(allow_none=True, default_value=None, max=999, min=0, help="""Integer value representing millisecond segment of a time.""")
    minutes = T.CFloat(allow_none=True, default_value=None, max=59, min=0, help="""Integer value representing minute segment of a time from 0-59.""")
    month = T.Union([T.CFloat(allow_none=True, default_value=None), T.Unicode(allow_none=True, default_value=None)])
    quarter = T.CFloat(allow_none=True, default_value=None, max=4, min=1, help="""Integer value representing the quarter of the year (from 1-4).""")
    seconds = T.CFloat(allow_none=True, default_value=None, max=59, min=0, help="""Integer value representing second segment of a time from 0-59.""")
    year = T.CFloat(allow_none=True, default_value=None, help="""Integer value representing the year.""")
    
    def __init__(self, date=None, day=None, hours=None, milliseconds=None, minutes=None, month=None, quarter=None, seconds=None, year=None, **kwargs):
        kwds = dict(date=date, day=day, hours=hours, milliseconds=milliseconds, minutes=minutes, month=month, quarter=quarter, seconds=seconds, year=year)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(DateTime, self).__init__(**kwargs)