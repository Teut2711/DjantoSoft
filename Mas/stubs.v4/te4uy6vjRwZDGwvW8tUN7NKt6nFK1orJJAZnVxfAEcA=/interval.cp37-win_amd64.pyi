import builtins as _mod_builtins
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps

class Float64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Float64ClosedBothIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Float64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Float64ClosedLeftIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Float64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Float64ClosedNeitherIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Float64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Float64ClosedRightIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Int64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Int64ClosedBothIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Int64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Int64ClosedLeftIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Int64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Int64ClosedNeitherIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Int64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Int64ClosedRightIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Interval(IntervalMixin):
    "\n    Immutable object implementing an Interval, a bounded slice-like interval.\n\n    Parameters\n    ----------\n    left : orderable scalar\n        Left bound for the interval.\n    right : orderable scalar\n        Right bound for the interval.\n    closed : {'right', 'left', 'both', 'neither'}, default 'right'\n        Whether the interval is closed on the left-side, right-side, both or\n        neither. See the Notes for more detailed explanation.\n\n    See Also\n    --------\n    IntervalIndex : An Index of Interval objects that are all closed on the\n        same side.\n    cut : Convert continuous data into discrete bins (Categorical\n        of Interval objects).\n    qcut : Convert continuous data into bins (Categorical of Interval objects)\n        based on quantiles.\n    Period : Represents a period of time.\n\n    Notes\n    -----\n    The parameters `left` and `right` must be from the same type, you must be\n    able to compare them and they must satisfy ``left <= right``.\n\n    A closed interval (in mathematics denoted by square brackets) contains\n    its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the\n    conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.\n    An open interval (in mathematics denoted by parentheses) does not contain\n    its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the\n    conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.\n    Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is\n    described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is\n    described by ``0 < x <= 5`` (``closed='right'``).\n\n    Examples\n    --------\n    It is possible to build Intervals of different types, like numeric ones:\n\n    >>> iv = pd.Interval(left=0, right=5)\n    >>> iv\n    Interval(0, 5, closed='right')\n\n    You can check if an element belongs to it\n\n    >>> 2.5 in iv\n    True\n\n    You can test the bounds (``closed='right'``, so ``0 < x <= 5``):\n\n    >>> 0 in iv\n    False\n    >>> 5 in iv\n    True\n    >>> 0.0001 in iv\n    True\n\n    Calculate its length\n\n    >>> iv.length\n    5\n\n    You can operate with `+` and `*` over an Interval and the operation\n    is applied to each of its bounds, so the result depends on the type\n    of the bound elements\n\n    >>> shifted_iv = iv + 3\n    >>> shifted_iv\n    Interval(3, 8, closed='right')\n    >>> extended_iv = iv * 10.0\n    >>> extended_iv\n    Interval(0.0, 50.0, closed='right')\n\n    To create a time interval you can use Timestamps as the bounds\n\n    >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),\n    ...                         pd.Timestamp('2018-01-01 00:00:00'),\n    ...                         closed='left')\n    >>> pd.Timestamp('2017-01-01 00:00') in year_2017\n    True\n    >>> year_2017.length\n    Timedelta('365 days 00:00:00')\n\n    And also you can create string intervals\n\n    >>> volume_1 = pd.Interval('Ant', 'Dog', closed='both')\n    >>> 'Bee' in volume_1\n    True\n    "
    def __add__(self, value):
        'Return self+value.'
        return Interval()
    
    __class__ = Interval
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
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
        "\n    Immutable object implementing an Interval, a bounded slice-like interval.\n\n    Parameters\n    ----------\n    left : orderable scalar\n        Left bound for the interval.\n    right : orderable scalar\n        Right bound for the interval.\n    closed : {'right', 'left', 'both', 'neither'}, default 'right'\n        Whether the interval is closed on the left-side, right-side, both or\n        neither. See the Notes for more detailed explanation.\n\n    See Also\n    --------\n    IntervalIndex : An Index of Interval objects that are all closed on the\n        same side.\n    cut : Convert continuous data into discrete bins (Categorical\n        of Interval objects).\n    qcut : Convert continuous data into bins (Categorical of Interval objects)\n        based on quantiles.\n    Period : Represents a period of time.\n\n    Notes\n    -----\n    The parameters `left` and `right` must be from the same type, you must be\n    able to compare them and they must satisfy ``left <= right``.\n\n    A closed interval (in mathematics denoted by square brackets) contains\n    its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the\n    conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.\n    An open interval (in mathematics denoted by parentheses) does not contain\n    its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the\n    conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.\n    Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is\n    described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is\n    described by ``0 < x <= 5`` (``closed='right'``).\n\n    Examples\n    --------\n    It is possible to build Intervals of different types, like numeric ones:\n\n    >>> iv = pd.Interval(left=0, right=5)\n    >>> iv\n    Interval(0, 5, closed='right')\n\n    You can check if an element belongs to it\n\n    >>> 2.5 in iv\n    True\n\n    You can test the bounds (``closed='right'``, so ``0 < x <= 5``):\n\n    >>> 0 in iv\n    False\n    >>> 5 in iv\n    True\n    >>> 0.0001 in iv\n    True\n\n    Calculate its length\n\n    >>> iv.length\n    5\n\n    You can operate with `+` and `*` over an Interval and the operation\n    is applied to each of its bounds, so the result depends on the type\n    of the bound elements\n\n    >>> shifted_iv = iv + 3\n    >>> shifted_iv\n    Interval(3, 8, closed='right')\n    >>> extended_iv = iv * 10.0\n    >>> extended_iv\n    Interval(0.0, 50.0, closed='right')\n\n    To create a time interval you can use Timestamps as the bounds\n\n    >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),\n    ...                         pd.Timestamp('2018-01-01 00:00:00'),\n    ...                         closed='left')\n    >>> pd.Timestamp('2017-01-01 00:00') in year_2017\n    True\n    >>> year_2017.length\n    Timedelta('365 days 00:00:00')\n\n    And also you can create string intervals\n\n    >>> volume_1 = pd.Interval('Ant', 'Dog', closed='both')\n    >>> 'Bee' in volume_1\n    True\n    "
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
    
    def __mul__(self, value):
        'Return self*value.'
        return Interval()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return Interval()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return Interval()
    
    def __rmul__(self, value):
        'Return value*self.'
        return Interval()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Interval()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Interval()
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return Interval()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def _repr_base(self):
        pass
    
    _typ = 'interval'
    def _validate_endpoint(self):
        pass
    
    @property
    def closed(self):
        '\n    Whether the interval is closed on the left-side, right-side, both or\n    neither.\n    '
        pass
    
    @property
    def left(self):
        '\n    Left bound for the interval.\n    '
        pass
    
    def overlaps(self):
        "\n        Check whether two Interval objects overlap.\n\n        Two intervals overlap if they share a common point, including closed\n        endpoints. Intervals that only have an open endpoint in common do not\n        overlap.\n\n        .. versionadded:: 0.24.0\n\n        Parameters\n        ----------\n        other : Interval\n            Interval to check against for an overlap.\n\n        Returns\n        -------\n        bool\n            True if the two intervals overlap.\n\n        See Also\n        --------\n        IntervalArray.overlaps : The corresponding method for IntervalArray.\n        IntervalIndex.overlaps : The corresponding method for IntervalIndex.\n\n        Examples\n        --------\n        >>> i1 = pd.Interval(0, 2)\n        >>> i2 = pd.Interval(1, 3)\n        >>> i1.overlaps(i2)\n        True\n        >>> i3 = pd.Interval(4, 5)\n        >>> i1.overlaps(i3)\n        False\n\n        Intervals that share closed endpoints overlap:\n\n        >>> i4 = pd.Interval(0, 1, closed='both')\n        >>> i5 = pd.Interval(1, 2, closed='both')\n        >>> i4.overlaps(i5)\n        True\n\n        Intervals that only have an open endpoint in common do not overlap:\n\n        >>> i6 = pd.Interval(1, 2, closed='neither')\n        >>> i4.overlaps(i6)\n        False\n        "
        pass
    
    @property
    def right(self):
        '\n    Right bound for the interval.\n    '
        pass
    

class IntervalMixin(_mod_builtins.object):
    __class__ = IntervalMixin
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _check_closed_matches(self):
        "Check if the closed attribute of `other` matches.\n\n        Note that 'left' and 'right' are considered different from 'both'.\n\n        Parameters\n        ----------\n        other : Interval, IntervalIndex, IntervalArray\n        name : str\n            Name to use for 'other' in the error message.\n\n        Raises\n        ------\n        ValueError\n            When `other` is not closed exactly the same as self.\n        "
        pass
    
    @property
    def closed_left(self):
        '\n        Check if the interval is closed on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        pass
    
    @property
    def closed_right(self):
        '\n        Check if the interval is closed on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        pass
    
    @property
    def is_empty(self):
        "\n        Indicates if an interval is empty, meaning it contains no points.\n\n        .. versionadded:: 0.25.0\n\n        Returns\n        -------\n        bool or ndarray\n            A boolean indicating if a scalar :class:`Interval` is empty, or a\n            boolean ``ndarray`` positionally indicating if an ``Interval`` in\n            an :class:`~arrays.IntervalArray` or :class:`IntervalIndex` is\n            empty.\n\n        Examples\n        --------\n        An :class:`Interval` that contains points is not empty:\n\n        >>> pd.Interval(0, 1, closed='right').is_empty\n        False\n\n        An ``Interval`` that does not contain any points is empty:\n\n        >>> pd.Interval(0, 0, closed='right').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='left').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='neither').is_empty\n        True\n\n        An ``Interval`` that contains a single point is not empty:\n\n        >>> pd.Interval(0, 0, closed='both').is_empty\n        False\n\n        An :class:`~arrays.IntervalArray` or :class:`IntervalIndex` returns a\n        boolean ``ndarray`` positionally indicating if an ``Interval`` is\n        empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'),\n        ...        pd.Interval(1, 2, closed='neither')]\n        >>> pd.arrays.IntervalArray(ivs).is_empty\n        array([ True, False])\n\n        Missing values are not considered empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'), np.nan]\n        >>> pd.IntervalIndex(ivs).is_empty\n        array([ True, False])\n        "
        pass
    
    @property
    def length(self):
        '\n        Return the length of the Interval.\n        '
        pass
    
    @property
    def mid(self):
        '\n        Return the midpoint of the Interval.\n        '
        pass
    
    @property
    def open_left(self):
        '\n        Check if the interval is open on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        pass
    
    @property
    def open_right(self):
        '\n        Check if the interval is open on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n        '
        pass
    

class IntervalTree(IntervalMixin):
    'A centered interval tree\n\n    Based off the algorithm described on Wikipedia:\n    http://en.wikipedia.org/wiki/Interval_tree\n\n    we are emulating the IndexEngine interface\n    '
    __class__ = IntervalTree
    def __init__(self):
        "\n        Parameters\n        ----------\n        left, right : np.ndarray[ndim=1]\n            Left and right bounds for each interval. Assumed to contain no\n            NaNs.\n        closed : {'left', 'right', 'both', 'neither'}, optional\n            Whether the intervals are closed on the left-side, right-side, both\n            or neither. Defaults to 'right'.\n        leaf_size : int, optional\n            Parameter that controls when the tree switches from creating nodes\n            to brute-force search. Tune this parameter to optimize query\n            performance.\n        "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __pyx_fuse_0get_indexer(self):
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        pass
    
    def __pyx_fuse_0get_indexer_non_unique(self):
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        pass
    
    def __pyx_fuse_1get_indexer(self):
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        pass
    
    def __pyx_fuse_1get_indexer_non_unique(self):
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        pass
    
    def __pyx_fuse_2get_indexer(self):
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        pass
    
    def __pyx_fuse_2get_indexer_non_unique(self):
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _is_overlapping(self):
        pass
    
    @property
    def _left_sorter(self):
        pass
    
    @property
    def _right_sorter(self):
        pass
    
    def clear_mapping(self):
        pass
    
    @property
    def closed(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    def get_indexer(self, target):
        'Return the positions corresponding to unique intervals that overlap\n        with the given array of scalar targets.\n        '
        pass
    
    def get_indexer_non_unique(self, target):
        'Return the positions corresponding to intervals that overlap with\n        the given array of scalar targets. Non-unique positions are repeated.\n        '
        pass
    
    @property
    def is_monotonic_increasing(self):
        '\n        Return True if the IntervalTree is monotonic increasing (only equal or\n        increasing values), else False\n        '
        pass
    
    @property
    def is_overlapping(self):
        '\n        Determine if the IntervalTree contains overlapping intervals.\n        Cached as self._is_overlapping.\n        '
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_sorter(self):
        'How to sort the left labels; this is used for binary search\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_sorter(self):
        'How to sort the right labels\n        '
        pass
    
    @property
    def root(self):
        pass
    

NODE_CLASSES = _mod_builtins.dict()
Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
class Uint64ClosedBothIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Uint64ClosedBothIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Uint64ClosedLeftIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Uint64ClosedLeftIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Uint64ClosedNeitherIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Uint64ClosedNeitherIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

class Uint64ClosedRightIntervalNode(_mod_builtins.object):
    'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
    __class__ = Uint64ClosedRightIntervalNode
    def __init__(self, *args, **kwargs):
        'Non-terminal node for an IntervalTree\n\n    Categorizes intervals by those that fall to the left, those that fall to\n    the right, and those that overlap with the pivot.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def center_left_indices(self):
        pass
    
    @property
    def center_left_values(self):
        pass
    
    @property
    def center_right_indices(self):
        pass
    
    @property
    def center_right_values(self):
        pass
    
    def counts(self):
        '\n        Inspect counts on this node\n        useful for debugging purposes\n        '
        pass
    
    @property
    def indices(self):
        pass
    
    @property
    def is_leaf_node(self):
        pass
    
    @property
    def leaf_size(self):
        pass
    
    @property
    def left(self):
        pass
    
    @property
    def left_node(self):
        pass
    
    @property
    def max_right(self):
        pass
    
    @property
    def min_left(self):
        pass
    
    @property
    def n_center(self):
        pass
    
    @property
    def n_elements(self):
        pass
    
    @property
    def pivot(self):
        pass
    
    def query(self, result, point):
        'Recursively query this node and its sub-nodes for intervals that\n        overlap with the query point.\n        '
        pass
    
    @property
    def right(self):
        pass
    
    @property
    def right_node(self):
        pass
    

_VALID_CLOSED = _mod_builtins.frozenset()
__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\interval.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.interval'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Float64ClosedBothIntervalNode():
    pass

def __pyx_unpickle_Float64ClosedLeftIntervalNode():
    pass

def __pyx_unpickle_Float64ClosedNeitherIntervalNode():
    pass

def __pyx_unpickle_Float64ClosedRightIntervalNode():
    pass

def __pyx_unpickle_Int64ClosedBothIntervalNode():
    pass

def __pyx_unpickle_Int64ClosedLeftIntervalNode():
    pass

def __pyx_unpickle_Int64ClosedNeitherIntervalNode():
    pass

def __pyx_unpickle_Int64ClosedRightIntervalNode():
    pass

def __pyx_unpickle_IntervalMixin():
    pass

def __pyx_unpickle_IntervalTree():
    pass

def __pyx_unpickle_Uint64ClosedBothIntervalNode():
    pass

def __pyx_unpickle_Uint64ClosedLeftIntervalNode():
    pass

def __pyx_unpickle_Uint64ClosedNeitherIntervalNode():
    pass

def __pyx_unpickle_Uint64ClosedRightIntervalNode():
    pass

__test__ = _mod_builtins.dict()
def intervals_to_interval_bounds():
    '\n    Parameters\n    ----------\n    intervals : ndarray\n        Object array of Intervals / nulls.\n\n    validate_closed: bool, default True\n        Boolean indicating if all intervals must be closed on the same side.\n        Mismatching closed will raise if True, else return None for closed.\n\n    Returns\n    -------\n    tuple of tuples\n        left : (ndarray, object, array)\n        right : (ndarray, object, array)\n        closed: str\n    '
    pass

def is_monotonic(arr, timelike):
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    pass

def le(a, b):
    'Same as a <= b.'
    pass

def lt(a, b):
    'Same as a < b.'
    pass

