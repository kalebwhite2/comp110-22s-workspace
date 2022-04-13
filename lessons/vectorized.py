from __future__ import annotations

from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.
        When rhs is a str, it is concatenated to every item in a new StrArray."""
        if isinstance(rhs, str):
            result: list[str] = []
            for item in self.items:
                result.append(item + rhs)
            return StrArray(result)

        else: 
            result: list[str] = []
            for i in range(len(self.items)):
                result.append(self.items[i] + " " + rhs.items[i])
            return StrArray(result)


first: StrArray = StrArray(['Armando', 'Brady', 'Caleb'])
last: StrArray = StrArray(['Bacot', 'Manek', 'Love'])

print(first + last)