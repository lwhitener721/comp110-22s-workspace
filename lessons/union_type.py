"""Union type gives flecibility to singe vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str of int!"""
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("hello")
log(110)