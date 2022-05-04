"""Imported Check from CS32 PSET 2"""


def check_arg(arg: object, ttype: type, arg_name: str):
    if not isinstance(arg, ttype):
        raise TypeError(
            f"The argument {arg_name} is of type {type(arg)}, but this function requires {ttype}"
        )