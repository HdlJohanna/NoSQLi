import typing as t


class SQL(str):
    """A string that is ready to be safely inserted into an SQL
    document, either because it was escaped or because it was marked
    safe.
    Passing an object to the constructor converts it to text and wraps
    it to mark it safe without escaping. To escape the text, use the
    :meth:`escape` class method instead.
    >>> SQL('SELECT * FROM test')
    SQL('SELECT * FROM test')
    >>> SQL(42)
    SQL('42')
    >>> SQL.escape("SELECT * FROM test")
    SQL('"SELECT * FROM test"')
    Passing an object that implements ``__sql__()`` will wrap the
    output of that method, marking it safe.
    >>> class Foo:
    ...     def __sql__(self):
    ...         return 'SELECT * FROM test'
    ...
    >>> SQL(Foo())
    SQL('SELECT * FROM test')
    This is a subclass of :class:`str`. It has the same methods, but
    escapes their arguments and returns a ``SQL`` instance.
    """

    __slots__ = ()

    def __new__(
        cls, base: t.Any = "", encoding: t.Optional[str] = None, errors: str = "strict"
    ) -> "SQL":
        if hasattr(base, "__html__"):
            base = base.__html__()

        if encoding is None:
            return super().__new__(cls, base)

        return super().__new__(cls, base, encoding, errors)
    
    def __sql__(self) -> "SQL":
        return self
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"
    
    @classmethod
    def escape(cls, s:t.AnyStr):
        """Escape and Secure an SQL String"""
        sq = escape(s)
        
        if sq.__class__ != cls:
            return cls(sq)
        
        return sq
        
from ._native import escape
