import builtins as _mod_builtins
import pandas._libs.tslibs.strptime as _mod_pandas__libs_tslibs_strptime

DAYS = _mod_builtins.list()
DAYS_FULL = _mod_builtins.list()
DAY_SECONDS = 86400
HOUR_SECONDS = 3600
LC_TIME = 5
LocaleTime = _mod_pandas__libs_tslibs_strptime.LocaleTime
MONTHS = _mod_builtins.list()
MONTHS_FULL = _mod_builtins.list()
MONTH_ALIASES = _mod_builtins.dict()
MONTH_NUMBERS = _mod_builtins.dict()
MONTH_TO_CAL_NUM = _mod_builtins.dict()
__builtins__ = {}
__doc__ = '\nCython implementations of functions resembling the stdlib calendar module\n'
__file__ = 'c:\\python38\\lib\\site-packages\\pandas\\_libs\\tslibs\\ccalendar.cp38-win_amd64.pyd'
__name__ = 'pandas._libs.tslibs.ccalendar'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def get_day_of_year():
    'Return the ordinal day-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    day_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    pass

def get_days_in_month():
    'Return the number of days in the given month of the given year.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    days_in_month : int\n\n    Notes\n    -----\n    Assumes that the arguments are valid.  Passing a month not between 1 and 12\n    risks a segfault.\n    '
    pass

def get_locale_names():
    'Returns an array of localized day or month names\n\n    Parameters\n    ----------\n    name_type : string, attribute of LocaleTime() in which to return localized\n        names\n    locale : string\n\n    Returns\n    -------\n    list of locale names\n    '
    pass

def get_week_of_year():
    'Return the ordinal week-of-year for the given day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n    day : int\n\n    Returns\n    -------\n    week_of_year : int32_t\n\n    Notes\n    -----\n    Assumes the inputs describe a valid date.\n    '
    pass

int_to_weekday = _mod_builtins.dict()
def set_locale(*args, **kwds):
    '\n    Context manager for temporarily setting a locale.\n\n    Parameters\n    ----------\n    new_locale : str or tuple\n        A string of the form <language_country>.<encoding>. For example to set\n        the current locale to US English with a UTF8 encoding, you would pass\n        "en_US.UTF-8".\n    lc_var : int, default `locale.LC_ALL`\n        The category of the locale being set.\n\n    Notes\n    -----\n    This is useful when you want to run a particular block of code under a\n    particular locale, without globally setting the locale. This probably isn\'t\n    thread-safe.\n    '
    pass

weekday_to_int = _mod_builtins.dict()
