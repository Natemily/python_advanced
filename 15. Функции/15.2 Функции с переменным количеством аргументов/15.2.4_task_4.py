def greet(names, *args):
    if len(args) == 0:
        return f"Hello, {names}!"
    else:
        greeting = f"Hello, {names}"
        for name in args[:-1]:
            greeting += f" and {name}"
        greeting += f" and {args[-1]}!"
        return greeting