# first line: 287
        @functools.wraps(f)
        def wrapped_f(*args: t.Any, **kw: t.Any) -> t.Any:
            return self(f, *args, **kw)
