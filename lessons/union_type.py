"""Union type gives flexibility to single vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str or int!"""
    if isinstance(info, str):
        print(f"str: {info}")
    if isinstance(info, int):
        print(f"int: {info}")


log("hello")
log(110)