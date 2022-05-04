# NoSQLi
NoSQLi is a Python Library to offer barebones Protection against  
SQL Injections by escaping Trigger Characters

## Installing
Install and update using pip:

    pip install -U git+https://github.com/hdljohanna/nosqli

Installing via PolyP:

    polyp install hdljohanna.nosqli

## Examples
```py
>>> from nosqli import SQL, escape

>>> # Let's try to prevent a SQL Injection!
>>> myname = "' OR 'a'='a"
>>> command = f"SELECT * FROM test WHERE name = '{myname}';"
>>> command
"SELECT * FROM test WHERE name = '' OR 'a'='a'"

>>> # This is insecure, since myname could be something like `' OR 't'='t`. While unlikely, trust me, Hackers can be patient
>>> # Now let's secure this
>>> command = f"SELECT * FROM test WHERE name = '{escape(myname)}';"
>>> command 
"SELECT * FROM test WHERE name = '\\' OR \\'a\\'=\\'a'"
>>> # Wrap in SQL to mark text as Safe and not escaping it
>>> SQL(f"SELECT * FROM test WHERE name = 'test';")
SQL("SELECT * FROM test WHERE name = 'test';")
>>> escape(SQL("SELECT * FROM test WHERE name = 'test';"))
SQL("SELECT * FROM test WHERE name = 'test';")

```
