def multiply(a, b):
    """
    Multiplies a and b.

    >>> a, b = 2, 5
    >>> multiply(a, b)
    10

    >>> multiply('A', 'B')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in multiply
    TypeError: can't multiply sequence by non-int of type 'str'

    # Using traceback
    >>> multiply(1, 2, 3)
    Traceback (most recent call last):
    TypeError: multiply() takes 2 positional arguments but 3 were given
    """

    return a * b
