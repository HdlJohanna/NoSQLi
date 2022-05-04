from . import SQL
import typing as t

def escape(string:t.AnyStr):
    """
This function prepends backslashes to the following characters: 
`\x00`, `\n`, `\r`, `\`, `'`, `"`, `*`, `=` and `\x1a`
    If the object has an ``__sql__`` method, it is called and the
    return value is assumed to already be safe for SQL.
    
    :param string: An object to be converted to a string and escaped.
    :return: A :class:`SQL` string with the escaped text.
    """
    
    if hasattr(string, "__sql__"):
        return string.__sql__()
    return SQL(
        string.replace("\x00","\\x00")
        .replace("\n","\\n")
        .replace("\r","\\r")
        .replace("\ ","\\ ")
        .replace("\x1a","\\x1a")
        .replace("'","\\'")
        .replace('"','\"')
        .replace('*','\*')
        .replace('=','\=')
    )

def escape_silent(s: t.Optional[t.AnyStr]) -> SQL:
    """Like :func:`escape` but treats ``None`` as the empty string.
    Useful with optional values, as otherwise you get the string
    ``'None'`` when the value is ``None``.
    >>> escape(None)
    SQL('None')
    >>> escape_silent(None)
    SQL('')
    """
    if s is None:
        return SQL()

    return escape(s)
