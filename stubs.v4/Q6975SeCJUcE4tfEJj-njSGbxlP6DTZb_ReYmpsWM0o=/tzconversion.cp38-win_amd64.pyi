import builtins as _mod_builtins
import dateutil.tz.tz as _mod_dateutil_tz_tz

DAY_SECONDS = 86400
HOUR_SECONDS = 3600
__builtins__ = {}
__doc__ = '\ntimezone conversion\n'
__file__ = 'c:\\python38\\lib\\site-packages\\pandas\\_libs\\tslibs\\tzconversion.cp38-win_amd64.pyd'
__name__ = 'pandas._libs.tslibs.tzconversion'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def tz_convert():
    '\n    Convert the values (in i8) from timezone1 to timezone2\n\n    Parameters\n    ----------\n    vals : int64 ndarray\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    int64 ndarray of converted\n    '
    pass

def tz_convert_single():
    '\n    Convert the val (in i8) from timezone1 to timezone2\n\n    This is a single timezone version of tz_convert\n\n    Parameters\n    ----------\n    val : int64\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    converted: int64\n    '
    pass

def tz_localize_to_utc():
    '\n    Localize tzinfo-naive i8 to given time zone (using pytz). If\n    there are ambiguities in the values, raise AmbiguousTimeError.\n\n    Parameters\n    ----------\n    vals : ndarray[int64_t]\n    tz : tzinfo or None\n    ambiguous : str, bool, or arraylike\n        When clocks moved backward due to DST, ambiguous times may arise.\n        For example in Central European Time (UTC+01), when going from 03:00\n        DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC\n        and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter\n        dictates how ambiguous times should be handled.\n\n        - \'infer\' will attempt to infer fall dst-transition hours based on\n          order\n        - bool-ndarray where True signifies a DST time, False signifies a\n          non-DST time (note that this flag is only applicable for ambiguous\n          times, but the array must have the same length as vals)\n        - bool if True, treat all vals as DST. If False, treat them as non-DST\n        - \'NaT\' will return NaT where there are ambiguous times\n\n    nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise", timedelta-like}\n        How to handle non-existent times when converting wall times to UTC\n\n        .. versionadded:: 0.24.0\n\n    Returns\n    -------\n    localized : ndarray[int64_t]\n    '
    pass

tzutc = _mod_dateutil_tz_tz.tzutc
