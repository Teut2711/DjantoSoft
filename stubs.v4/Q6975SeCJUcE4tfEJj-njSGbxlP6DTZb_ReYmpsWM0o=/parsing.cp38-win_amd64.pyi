import _io as _mod__io
import builtins as _mod_builtins
import datetime as _mod_datetime
import dateutil.parser._parser as _mod_dateutil_parser__parser
import dateutil.relativedelta as _mod_dateutil_relativedelta
import dateutil.tz.tz as _mod_dateutil_tz_tz
import pandas._libs.tslibs.nattype as _mod_pandas__libs_tslibs_nattype

DEFAULTPARSER = _mod_dateutil_parser__parser.parser()
class DateParseError(_mod_builtins.ValueError):
    __class__ = DateParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.parsing'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

MONTH_NUMBERS = _mod_builtins.dict()
NaT = _mod_pandas__libs_tslibs_nattype.NaTType()
StringIO = _mod__io.StringIO
def _DATEUTIL_LEXER_SPLIT(cls, s):
    pass

_DEFAULT_DATETIME = _mod_datetime.datetime()
__builtins__ = {}
__doc__ = '\nParsing functions for datetime and datetime-like strings.\n'
__file__ = 'c:\\python38\\lib\\site-packages\\pandas\\_libs\\tslibs\\parsing.cp38-win_amd64.pyd'
__name__ = 'pandas._libs.tslibs.parsing'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _concat_date_cols():
    "\n    Concatenates elements from numpy arrays in `date_cols` into strings.\n\n    Parameters\n    ----------\n    date_cols : tuple of numpy arrays\n    keep_trivial_numbers : bool, default True\n        if True and len(date_cols) == 1, then\n        conversion (to string from integer/float zero) is not performed\n\n    Returns\n    -------\n    arr_of_rows : ndarray (dtype=object)\n\n    Examples\n    --------\n    >>> dates=np.array(['3/31/2019', '4/31/2019'], dtype=object)\n    >>> times=np.array(['11:20', '10:45'], dtype=object)\n    >>> result = _concat_date_cols((dates, times))\n    >>> result\n    array(['3/31/2019 11:20', '4/31/2019 10:45'], dtype=object)\n    "
    pass

_dateutil_tzlocal = _mod_dateutil_tz_tz.tzlocal
_dateutil_tzstr = _mod_dateutil_tz_tz.tzstr
_dateutil_tzutc = _mod_dateutil_tz_tz.tzutc
def _does_string_look_like_datetime():
    "\n    Checks whether given string is a datetime: it has to start with '0' or\n    be greater than 1000.\n\n    Parameters\n    ----------\n    py_string: object\n\n    Returns\n    -------\n    whether given string is a datetime\n    "
    pass

def _format_is_iso():
    '\n    Does format match the iso8601 set that can be handled by the C parser?\n    Generally of form YYYY-MM-DDTHH:MM:SS - date separator can be different\n    but must be consistent.  Leading 0s in dates and times are optional.\n    '
    pass

def _guess_datetime_format():
    "\n    Guess the datetime format of a given datetime string.\n\n    Parameters\n    ----------\n    dt_str : string, datetime string to guess the format of\n    dayfirst : boolean, default False\n        If True parses dates with the day first, eg 20/01/2005\n        Warning: dayfirst=True is not strict, but will prefer to parse\n        with day first (this is a known bug).\n    dt_str_parse : function, defaults to `dateutil.parser.parse`\n        This function should take in a datetime string and return\n        a `datetime.datetime` guess that the datetime string represents\n    dt_str_split : function, defaults to `_DATEUTIL_LEXER_SPLIT` (dateutil)\n        This function should take in a datetime string and return\n        a list of strings, the guess of the various specific parts\n        e.g. '2011/12/30' -> ['2011', '/', '12', '/', '30']\n\n    Returns\n    -------\n    ret : datetime format string (for `strftime` or `strptime`)\n    "
    pass

class _timelex(_mod_builtins.object):
    __class__ = _timelex
    __dict__ = {}
    def __init__(self, instream):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.parsing'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def get_tokens(self):
        '\n        This function breaks the time string into lexical units (tokens), which\n        can be parsed by the parser. Lexical units are demarcated by changes in\n        the character set, so any continuous string of letters is considered\n        one unit, any continuous string of numbers is considered one unit.\n        The main complication arises from the fact that dots (\'.\') can be used\n        both as separators (e.g. "Sep.20.2009") or decimal points (e.g.\n        "4:30:21.447"). As such, it is necessary to read the full context of\n        any dot-separated strings before breaking it into tokens; as such, this\n        function maintains a "token stack", for when the ambiguous context\n        demands that multiple tokens be parsed at once.\n        '
        pass
    
    def split(self, cls, s):
        pass
    

def du_parse(timestr, parserinfo, **kwargs):
    '\n\n    Parse a string in one of the supported formats, using the\n    ``parserinfo`` parameters.\n\n    :param timestr:\n        A string containing a date/time stamp.\n\n    :param parserinfo:\n        A :class:`parserinfo` object containing parameters for the parser.\n        If ``None``, the default arguments to the :class:`parserinfo`\n        constructor are used.\n\n    The ``**kwargs`` parameter takes the following keyword arguments:\n\n    :param default:\n        The default datetime object, if this is a datetime object and not\n        ``None``, elements specified in ``timestr`` replace elements in the\n        default object.\n\n    :param ignoretz:\n        If set ``True``, time zones in parsed strings are ignored and a naive\n        :class:`datetime` object is returned.\n\n    :param tzinfos:\n        Additional time zone names / aliases which may be present in the\n        string. This argument maps time zone names (and optionally offsets\n        from those time zones) to time zones. This parameter can be a\n        dictionary with timezone aliases mapping time zone names to time\n        zones or a function taking two parameters (``tzname`` and\n        ``tzoffset``) and returning a time zone.\n\n        The timezones to which the names are mapped can be an integer\n        offset from UTC in seconds or a :class:`tzinfo` object.\n\n        .. doctest::\n           :options: +NORMALIZE_WHITESPACE\n\n            >>> from dateutil.parser import parse\n            >>> from dateutil.tz import gettz\n            >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}\n            >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)\n            datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u\'BRST\', -7200))\n            >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)\n            datetime.datetime(2012, 1, 19, 17, 21,\n                              tzinfo=tzfile(\'/usr/share/zoneinfo/America/Chicago\'))\n\n        This parameter is ignored if ``ignoretz`` is set.\n\n    :param dayfirst:\n        Whether to interpret the first value in an ambiguous 3-integer date\n        (e.g. 01/05/09) as the day (``True``) or month (``False``). If\n        ``yearfirst`` is set to ``True``, this distinguishes between YDM and\n        YMD. If set to ``None``, this value is retrieved from the current\n        :class:`parserinfo` object (which itself defaults to ``False``).\n\n    :param yearfirst:\n        Whether to interpret the first value in an ambiguous 3-integer date\n        (e.g. 01/05/09) as the year. If ``True``, the first number is taken to\n        be the year, otherwise the last number is taken to be the year. If\n        this is set to ``None``, the value is retrieved from the current\n        :class:`parserinfo` object (which itself defaults to ``False``).\n\n    :param fuzzy:\n        Whether to allow fuzzy parsing, allowing for string like "Today is\n        January 1, 2047 at 8:21:00AM".\n\n    :param fuzzy_with_tokens:\n        If ``True``, ``fuzzy`` is automatically set to True, and the parser\n        will return a tuple where the first element is the parsed\n        :class:`datetime.datetime` datetimestamp and the second element is\n        a tuple containing the portions of the string which were ignored:\n\n        .. doctest::\n\n            >>> from dateutil.parser import parse\n            >>> parse("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True)\n            (datetime.datetime(2047, 1, 1, 8, 21), (u\'Today is \', u\' \', u\'at \'))\n\n    :return:\n        Returns a :class:`datetime.datetime` object or, if the\n        ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the\n        first element being a :class:`datetime.datetime` object, the second\n        a tuple containing the fuzzy tokens.\n\n    :raises ValueError:\n        Raised for invalid or unknown string format, if the provided\n        :class:`tzinfo` is not in a valid format, or if an invalid date\n        would be created.\n\n    :raises OverflowError:\n        Raised if the parsed date exceeds the largest valid C integer on\n        your system.\n    '
    pass

def get_option(self, *args, **kwds):
    '\nget_option(pat)\n\nRetrieves the value of the specified option.\n\nAvailable options:\n\n- compute.[use_bottleneck, use_numexpr]\n- display.[chop_threshold, colheader_justify, column_space, date_dayfirst,\n  date_yearfirst, encoding, expand_frame_repr, float_format]\n- display.html.[border, table_schema, use_mathjax]\n- display.[large_repr]\n- display.latex.[escape, longtable, multicolumn, multicolumn_format, multirow,\n  repr]\n- display.[max_categories, max_columns, max_colwidth, max_info_columns,\n  max_info_rows, max_rows, max_seq_items, memory_usage, min_rows, multi_sparse,\n  notebook_repr_html, pprint_nest_depth, precision, show_dimensions]\n- display.unicode.[ambiguous_as_wide, east_asian_width]\n- display.[width]\n- io.excel.ods.[reader]\n- io.excel.xls.[reader, writer]\n- io.excel.xlsm.[reader, writer]\n- io.excel.xlsx.[reader, writer]\n- io.hdf.[default_format, dropna_table]\n- io.parquet.[engine]\n- mode.[chained_assignment, sim_interactive, use_inf_as_na, use_inf_as_null]\n- plotting.[backend]\n- plotting.matplotlib.[register_converters]\n\nParameters\n----------\npat : str\n    Regexp which should match a single option.\n    Note: partial matches are supported for convenience, but unless you use the\n    full option name (e.g. x.y.z.option_name), your code may break in future\n    versions if new options with similar names are introduced.\n\nReturns\n-------\nresult : the value of the option\n\nRaises\n------\nOptionError : if no such option exists\n\nNotes\n-----\nThe available options with its descriptions:\n\ncompute.use_bottleneck : bool\n    Use the bottleneck library to accelerate if it is installed,\n    the default is True\n    Valid values: False,True\n    [default: True] [currently: True]compute.use_numexpr : bool\n    Use the numexpr library to accelerate computation if it is installed,\n    the default is True\n    Valid values: False,True\n    [default: True] [currently: True]display.chop_threshold : float or None\n    if set to a float value, all float values smaller then the given threshold\n    will be displayed as exactly 0 by repr and friends.\n    [default: None] [currently: None]display.colheader_justify : \'left\'/\'right\'\n    Controls the justification of column headers. used by DataFrameFormatter.\n    [default: right] [currently: right]display.column_space No description available.\n    [default: 12] [currently: 12]display.date_dayfirst : boolean\n    When True, prints and parses dates with the day first, eg 20/01/2005\n    [default: False] [currently: False]display.date_yearfirst : boolean\n    When True, prints and parses dates with the year first, eg 2005/01/20\n    [default: False] [currently: False]display.encoding : str/unicode\n    Defaults to the detected encoding of the console.\n    Specifies the encoding to be used for strings returned by to_string,\n    these are generally strings meant to be displayed on the console.\n    [default: cp1252] [currently: cp1252]display.expand_frame_repr : boolean\n    Whether to print out the full DataFrame repr for wide DataFrames across\n    multiple lines, `max_columns` is still respected, but the output will\n    wrap-around across multiple "pages" if its width exceeds `display.width`.\n    [default: True] [currently: True]display.float_format : callable\n    The callable should accept a floating point number and return\n    a string with the desired format of the number. This is used\n    in some places like SeriesFormatter.\n    See formats.format.EngFormatter for an example.\n    [default: None] [currently: None]display.html.border : int\n    A ``border=value`` attribute is inserted in the ``<table>`` tag\n    for the DataFrame HTML repr.\n    [default: 1] [currently: 1]display.html.table_schema : boolean\n    Whether to publish a Table Schema representation for frontends\n    that support it.\n    (default: False)\n    [default: False] [currently: False]display.html.use_mathjax : boolean\n    When True, Jupyter notebook will process table contents using MathJax,\n    rendering mathematical expressions enclosed by the dollar symbol.\n    (default: True)\n    [default: True] [currently: True]display.large_repr : \'truncate\'/\'info\'\n    For DataFrames exceeding max_rows/max_cols, the repr (and HTML repr) can\n    show a truncated table (the default from 0.13), or switch to the view from\n    df.info() (the behaviour in earlier versions of pandas).\n    [default: truncate] [currently: truncate]display.latex.escape : bool\n    This specifies if the to_latex method of a Dataframe uses escapes special\n    characters.\n    Valid values: False,True\n    [default: True] [currently: True]display.latex.longtable :bool\n    This specifies if the to_latex method of a Dataframe uses the longtable\n    format.\n    Valid values: False,True\n    [default: False] [currently: False]display.latex.multicolumn : bool\n    This specifies if the to_latex method of a Dataframe uses multicolumns\n    to pretty-print MultiIndex columns.\n    Valid values: False,True\n    [default: True] [currently: True]display.latex.multicolumn_format : bool\n    This specifies if the to_latex method of a Dataframe uses multicolumns\n    to pretty-print MultiIndex columns.\n    Valid values: False,True\n    [default: l] [currently: l]display.latex.multirow : bool\n    This specifies if the to_latex method of a Dataframe uses multirows\n    to pretty-print MultiIndex rows.\n    Valid values: False,True\n    [default: False] [currently: False]display.latex.repr : boolean\n    Whether to produce a latex DataFrame representation for jupyter\n    environments that support it.\n    (default: False)\n    [default: False] [currently: False]display.max_categories : int\n    This sets the maximum number of categories pandas should output when\n    printing out a `Categorical` or a Series of dtype "category".\n    [default: 8] [currently: 8]display.max_columns : int\n    If max_cols is exceeded, switch to truncate view. Depending on\n    `large_repr`, objects are either centrally truncated or printed as\n    a summary view. \'None\' value means unlimited.\n\n    In case python/IPython is running in a terminal and `large_repr`\n    equals \'truncate\' this can be set to 0 and pandas will auto-detect\n    the width of the terminal and print a truncated object which fits\n    the screen width. The IPython notebook, IPython qtconsole, or IDLE\n    do not run in a terminal and hence it is not possible to do\n    correct auto-detection.\n    [default: 0] [currently: 0]display.max_colwidth : int\n    The maximum width in characters of a column in the repr of\n    a pandas data structure. When the column overflows, a "..."\n    placeholder is embedded in the output.\n    [default: 50] [currently: 50]display.max_info_columns : int\n    max_info_columns is used in DataFrame.info method to decide if\n    per column information will be printed.\n    [default: 100] [currently: 100]display.max_info_rows : int or None\n    df.info() will usually show null-counts for each column.\n    For large frames this can be quite slow. max_info_rows and max_info_cols\n    limit this null check only to frames with smaller dimensions than\n    specified.\n    [default: 1690785] [currently: 1690785]display.max_rows : int\n    If max_rows is exceeded, switch to truncate view. Depending on\n    `large_repr`, objects are either centrally truncated or printed as\n    a summary view. \'None\' value means unlimited.\n\n    In case python/IPython is running in a terminal and `large_repr`\n    equals \'truncate\' this can be set to 0 and pandas will auto-detect\n    the height of the terminal and print a truncated object which fits\n    the screen height. The IPython notebook, IPython qtconsole, or\n    IDLE do not run in a terminal and hence it is not possible to do\n    correct auto-detection.\n    [default: 60] [currently: 60]display.max_seq_items : int or None\n    when pretty-printing a long sequence, no more then `max_seq_items`\n    will be printed. If items are omitted, they will be denoted by the\n    addition of "..." to the resulting string.\n\n    If set to None, the number of items to be printed is unlimited.\n    [default: 100] [currently: 100]display.memory_usage : bool, string or None\n    This specifies if the memory usage of a DataFrame should be displayed when\n    df.info() is called. Valid values True,False,\'deep\'\n    [default: True] [currently: True]display.min_rows : int\n    The numbers of rows to show in a truncated view (when `max_rows` is\n    exceeded). Ignored when `max_rows` is set to None or 0. When set to\n    None, follows the value of `max_rows`.\n    [default: 10] [currently: 10]display.multi_sparse : boolean\n    "sparsify" MultiIndex display (don\'t display repeated\n    elements in outer levels within groups)\n    [default: True] [currently: True]display.notebook_repr_html : boolean\n    When True, IPython notebook will use html representation for\n    pandas objects (if it is available).\n    [default: True] [currently: True]display.pprint_nest_depth : int\n    Controls the number of nested levels to process when pretty-printing\n    [default: 3] [currently: 3]display.precision : int\n    Floating point output precision (number of significant digits). This is\n    only a suggestion\n    [default: 6] [currently: 6]display.show_dimensions : boolean or \'truncate\'\n    Whether to print out dimensions at the end of DataFrame repr.\n    If \'truncate\' is specified, only print out the dimensions if the\n    frame is truncated (e.g. not display all rows and/or columns)\n    [default: truncate] [currently: truncate]display.unicode.ambiguous_as_wide : boolean\n    Whether to use the Unicode East Asian Width to calculate the display text\n    width.\n    Enabling this may affect to the performance (default: False)\n    [default: False] [currently: False]display.unicode.east_asian_width : boolean\n    Whether to use the Unicode East Asian Width to calculate the display text\n    width.\n    Enabling this may affect to the performance (default: False)\n    [default: False] [currently: False]display.width : int\n    Width of the display in characters. In case python/IPython is running in\n    a terminal this can be set to None and pandas will correctly auto-detect\n    the width.\n    Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a\n    terminal and hence it is not possible to correctly detect the width.\n    [default: 80] [currently: 80]io.excel.ods.reader : string\n    The default Excel reader engine for \'ods\' files. Available options:\n    auto, odf.\n    [default: auto] [currently: auto]io.excel.xls.reader : string\n    The default Excel reader engine for \'xls\' files. Available options:\n    auto, xlrd.\n    [default: auto] [currently: auto]io.excel.xls.writer : string\n    The default Excel writer engine for \'xls\' files. Available options:\n    auto, xlwt.\n    [default: auto] [currently: auto]io.excel.xlsm.reader : string\n    The default Excel reader engine for \'xlsm\' files. Available options:\n    auto, xlrd, openpyxl.\n    [default: auto] [currently: auto]io.excel.xlsm.writer : string\n    The default Excel writer engine for \'xlsm\' files. Available options:\n    auto, openpyxl.\n    [default: auto] [currently: auto]io.excel.xlsx.reader : string\n    The default Excel reader engine for \'xlsx\' files. Available options:\n    auto, xlrd, openpyxl.\n    [default: auto] [currently: auto]io.excel.xlsx.writer : string\n    The default Excel writer engine for \'xlsx\' files. Available options:\n    auto, openpyxl, xlsxwriter.\n    [default: auto] [currently: auto]io.hdf.default_format : format\n    default format writing format, if None, then\n    put will default to \'fixed\' and append will default to \'table\'\n    [default: None] [currently: None]io.hdf.dropna_table : boolean\n    drop ALL nan rows when appending to a table\n    [default: False] [currently: False]io.parquet.engine : string\n    The default parquet reader/writer engine. Available options:\n    \'auto\', \'pyarrow\', \'fastparquet\', the default is \'auto\'\n    [default: auto] [currently: auto]mode.chained_assignment : string\n    Raise an exception, warn, or no action if trying to use chained assignment,\n    The default is warn\n    [default: warn] [currently: warn]mode.sim_interactive : boolean\n    Whether to simulate interactive mode for purposes of testing\n    [default: False] [currently: False]mode.use_inf_as_na : boolean\n    True means treat None, NaN, INF, -INF as NA (old way),\n    False means None and NaN are null, but INF, -INF are not NA\n    (new way).\n    [default: False] [currently: False]mode.use_inf_as_null : boolean\n    use_inf_as_null had been deprecated and will be removed in a future\n    version. Use `use_inf_as_na` instead.\n    [default: False] [currently: False]\n    (Deprecated, use `mode.use_inf_as_na` instead.)plotting.backend : str\n    The plotting backend to use. The default value is "matplotlib", the\n    backend provided with pandas. Other backends can be specified by\n    prodiving the name of the module that implements the backend.\n    [default: matplotlib] [currently: matplotlib]plotting.matplotlib.register_converters : bool\n    Whether to register converters with matplotlib\'s units registry for\n    dates, times, datetimes, and Periods. Toggling to False will remove\n    the converters, restoring any converters that pandas overwrote.\n    [default: True] [currently: True]\n'
    pass

nat_strings = _mod_builtins.set()
def parse_datetime_string():
    'parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

def parse_time_string():
    '\n    Try hard to parse datetime string, leveraging dateutil plus some extra\n    goodies like quarter recognition.\n\n    Parameters\n    ----------\n    arg : str\n    freq : str or DateOffset, default None\n        Helps with interpreting time string if supplied\n    dayfirst : bool, default None\n        If None uses default from print_config\n    yearfirst : bool, default None\n        If None uses default from print_config\n\n    Returns\n    -------\n    datetime, datetime/dateutil.parser._result, str\n    '
    pass

relativedelta = _mod_dateutil_relativedelta.relativedelta
def try_parse_date_and_time():
    pass

def try_parse_dates():
    pass

def try_parse_datetime_components():
    pass

def try_parse_year_month_day():
    pass

tzoffset = _mod_dateutil_tz_tz.tzoffset
