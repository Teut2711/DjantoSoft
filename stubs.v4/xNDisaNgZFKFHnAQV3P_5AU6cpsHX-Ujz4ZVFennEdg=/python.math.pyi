__doc__ = 'This module provides access to the mathematical functions\ndefined by the C standard.'
__name__ = 'math'
__package__ = ''
def acos(x):
    'Return the arc cosine (measured in radians) of x.'
    pass

def acosh(x):
    'Return the inverse hyperbolic cosine of x.'
    pass

def asin(x):
    'Return the arc sine (measured in radians) of x.'
    pass

def asinh(x):
    'Return the inverse hyperbolic sine of x.'
    pass

def atan(x):
    'Return the arc tangent (measured in radians) of x.'
    pass

def atan2(y, x):
    'Return the arc tangent (measured in radians) of y/x.\n\nUnlike atan(y/x), the signs of both x and y are considered.'
    pass

def atanh(x):
    'Return the inverse hyperbolic tangent of x.'
    pass

def ceil(x):
    'Return the ceiling of x as an Integral.\n\nThis is the smallest integer >= x.'
    pass

def comb(n, k):
    'Number of ways to choose k items from n items without repetition and without order.\n\nEvaluates to n! / (k! * (n - k)!) when k <= n and evaluates\nto zero when k > n.\n\nAlso called the binomial coefficient because it is equivalent\nto the coefficient of k-th term in polynomial expansion of the\nexpression (1 + x)**n.\n\nRaises TypeError if either of the arguments are not integers.\nRaises ValueError if either of the arguments are negative.'
    pass

def copysign(x, y):
    'Return a float with the magnitude (absolute value) of x but the sign of y.\n\nOn platforms that support signed zeros, copysign(1.0, -0.0)\nreturns -1.0.\n'
    pass

def cos(x):
    'Return the cosine of x (measured in radians).'
    pass

def cosh(x):
    'Return the hyperbolic cosine of x.'
    pass

def degrees(x):
    'Convert angle x from radians to degrees.'
    pass

def dist(p, q):
    'Return the Euclidean distance between two points p and q.\n\nThe points should be specified as sequences (or iterables) of\ncoordinates.  Both inputs must have the same dimension.\n\nRoughly equivalent to:\n    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))'
    pass

e = 2.718281828459045
def erf(x):
    'Error function at x.'
    pass

def erfc(x):
    'Complementary error function at x.'
    pass

def exp(x):
    'Return e raised to the power of x.'
    pass

def expm1(x):
    'Return exp(x)-1.\n\nThis function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.'
    pass

def fabs(x):
    'Return the absolute value of the float x.'
    pass

def factorial(x):
    'Find x!.\n\nRaise a ValueError if x is negative or non-integral.'
    pass

def floor(x):
    'Return the floor of x as an Integral.\n\nThis is the largest integer <= x.'
    pass

def fmod(x, y):
    'Return fmod(x, y), according to platform C.\n\nx % y may differ.'
    pass

def frexp(x):
    'Return the mantissa and exponent of x, as pair (m, e).\n\nm is a float and e is an int, such that x = m * 2.**e.\nIf x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.'
    pass

def fsum(seq):
    'Return an accurate floating point sum of values in the iterable seq.\n\nAssumes IEEE-754 floating point arithmetic.'
    pass

def gamma(x):
    'Gamma function at x.'
    pass

def gcd(x, y):
    'greatest common divisor of x and y'
    pass

def hypot(*coordinates):
    'hypot(*coordinates) -> value\n\nMultidimensional Euclidean distance from the origin to a point.\n\nRoughly equivalent to:\n    sqrt(sum(x**2 for x in coordinates))\n\nFor a two dimensional point (x, y), gives the hypotenuse\nusing the Pythagorean theorem:  sqrt(x*x + y*y).\n\nFor example, the hypotenuse of a 3/4/5 right triangle is:\n\n    >>> hypot(3.0, 4.0)\n    5.0\n'
    pass

inf = float('inf')
def isclose(a, b):
    'Determine whether two floating point numbers are close in value.\n\n  rel_tol\n    maximum difference for being considered "close", relative to the\n    magnitude of the input values\n  abs_tol\n    maximum difference for being considered "close", regardless of the\n    magnitude of the input values\n\nReturn True if a is close in value to b, and False otherwise.\n\nFor the values to be considered close, the difference between them\nmust be smaller than at least one of the tolerances.\n\n-inf, inf and NaN behave similarly to the IEEE 754 Standard.  That\nis, NaN is not close to anything, even itself.  inf and -inf are\nonly close to themselves.'
    pass

def isfinite(x):
    'Return True if x is neither an infinity nor a NaN, and False otherwise.'
    pass

def isinf(x):
    'Return True if x is a positive or negative infinity, and False otherwise.'
    pass

def isnan(x):
    'Return True if x is a NaN (not a number), and False otherwise.'
    pass

def isqrt(n):
    'Return the integer part of the square root of the input.'
    pass

def ldexp(x, i):
    'Return x * (2**i).\n\nThis is essentially the inverse of frexp().'
    pass

def lgamma(x):
    'Natural logarithm of absolute value of Gamma function at x.'
    pass

def log(x, base=math.e):
    'log(x, [base=math.e])\nReturn the logarithm of x to the given base.\n\nIf the base not specified, returns the natural logarithm (base e) of x.'
    pass

def log10(x):
    'Return the base 10 logarithm of x.'
    pass

def log1p(x):
    'Return the natural logarithm of 1+x (base e).\n\nThe result is computed in a way which is accurate for x near zero.'
    pass

def log2(x):
    'Return the base 2 logarithm of x.'
    pass

def modf(x):
    'Return the fractional and integer parts of x.\n\nBoth results carry the sign of x and are floats.'
    pass

nan = float('nan')
def perm(n, k):
    'Number of ways to choose k items from n items without repetition and with order.\n\nEvaluates to n! / (n - k)! when k <= n and evaluates\nto zero when k > n.\n\nIf k is not specified or is None, then k defaults to n\nand the function returns n!.\n\nRaises TypeError if either of the arguments are not integers.\nRaises ValueError if either of the arguments are negative.'
    pass

pi = 3.141592653589793
def pow(x, y):
    'Return x**y (x to the power of y).'
    pass

def prod(iterable):
    'Calculate the product of all the elements in the input iterable.\n\nThe default start value for the product is 1.\n\nWhen the iterable is empty, return the start value.  This function is\nintended specifically for use with numeric values and may reject\nnon-numeric types.'
    pass

def radians(x):
    'Convert angle x from degrees to radians.'
    pass

def remainder(x, y):
    'Difference between x and the closest integer multiple of y.\n\nReturn x - n*y where n*y is the closest integer multiple of y.\nIn the case where x is exactly halfway between two multiples of\ny, the nearest even value of n is used. The result is always exact.'
    pass

def sin(x):
    'Return the sine of x (measured in radians).'
    pass

def sinh(x):
    'Return the hyperbolic sine of x.'
    pass

def sqrt(x):
    'Return the square root of x.'
    pass

def tan(x):
    'Return the tangent of x (measured in radians).'
    pass

def tanh(x):
    'Return the hyperbolic tangent of x.'
    pass

tau = 6.283185307179586
def trunc(x):
    'Truncates the Real x to the nearest Integral toward 0.\n\nUses the __trunc__ magic method.'
    pass

