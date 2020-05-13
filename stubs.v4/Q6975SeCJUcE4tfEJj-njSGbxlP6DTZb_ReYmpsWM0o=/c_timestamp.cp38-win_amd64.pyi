import builtins as _mod_builtins
import datetime as _mod_datetime
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
UTC = _mod_pytz.UTC()
class _Timestamp(_mod_datetime.datetime):
    def __add__(self, value):
        'Return self+value.'
        return _Timestamp()
    
    __array_priority__ = 100
    __class__ = _Timestamp
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __radd__(self, value):
        'Return value+self.'
        return _Timestamp()
    
    def __reduce_ex__(self, protocol):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rsub__(self, value):
        'Return value-self.'
        return _Timestamp()
    
    def __sub__(self, value):
        'Return self-value.'
        return _Timestamp()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _date_attributes(self):
        pass
    
    @property
    def _date_repr(self):
        pass
    
    def _get_date_name_field(self):
        pass
    
    def _get_start_end_field(self):
        pass
    
    @property
    def _repr_base(self):
        pass
    
    @property
    def _short_repr(self):
        pass
    
    @property
    def _time_repr(self):
        pass
    
    @property
    def asm8(self):
        '\n        Return numpy datetime64 format in nanoseconds.\n        '
        pass
    
    @classmethod
    def combine(cls):
        'date, time -> datetime with same date and time fields'
        pass
    
    @property
    def freq(self):
        pass
    
    @classmethod
    def fromisocalendar(cls):
        'int, int, int -> Construct a date from the ISO year, week number and weekday.\n\nThis is the inverse of the date.isocalendar() function'
        pass
    
    @classmethod
    def fromisoformat(cls):
        'string -> datetime from datetime.isoformat() output'
        pass
    
    @classmethod
    def fromordinal(cls):
        'int -> date corresponding to a proleptic Gregorian ordinal.'
        pass
    
    @classmethod
    def fromtimestamp(cls):
        "timestamp[, tz] -> tz's local time from POSIX timestamp."
        pass
    
    @property
    def nanosecond(self):
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def timestamp(self):
        'Return POSIX timestamp as float.'
        pass
    
    def to_datetime64(self):
        "\n        Return a numpy.datetime64 object with 'ns' precision.\n        "
        pass
    
    def to_numpy(self):
        '\n        Convert the Timestamp to a NumPy datetime64.\n\n        .. versionadded:: 0.25.0\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n        '
        pass
    
    def to_pydatetime(self):
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
        pass
    
    @classmethod
    def today(cls):
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
        pass
    
    @classmethod
    def utcfromtimestamp(cls):
        'Construct a naive UTC datetime from a POSIX timestamp.'
        pass
    
    @classmethod
    def utcnow(cls):
        'Return a new datetime representing UTC day and time.'
        pass
    
    @property
    def value(self):
        pass
    

__builtins__ = {}
__doc__ = '\n_Timestamp is a c-defined subclass of datetime.datetime\n\nIt is separate from timestamps.pyx to prevent circular cimports\n\nThis allows _Timestamp to be imported in other modules\nso that isinstance(obj, _Timestamp) checks can be performed\n\n_Timestamp is PITA. Because we inherit from datetime, which has very specific\nconstruction requirements, we need to do object instantiation in python\n(see Timestamp class below). This will serve as a C extension type that\nshadows the python class, where we do any heavy lifting.\n'
__file__ = 'c:\\python38\\lib\\site-packages\\pandas\\_libs\\tslibs\\c_timestamp.cp38-win_amd64.pyd'
__name__ = 'pandas._libs.tslibs.c_timestamp'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def get_date_name_field():
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. weekday_name)\n    '
    pass

def get_start_end_field():
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    pass

def maybe_integer_op_deprecated():
    pass

