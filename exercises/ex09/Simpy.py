"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730409578"


class Simpy:
    """Fake numpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Builds a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Creates a string representation of the Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, fill_float: float, times: int) -> None:
        """Fills the Simpy object with a singular float a given number of times."""
        result: list[float] = []
        for i in range(times):
            result.append(fill_float)
        self.values = result
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Like the fill method, but will fill a Simpy object with a range of floats."""
        assert step != 0.0
        result: list[float] = []
        i: float = start
        if i < stop:
            while i < stop:
                result.append(i)
                i += step
            self.values = result
        if i > stop:
            while i > stop:
                result.append(i)
                i += step
            self.values = result

    def sum(self) -> float:
        """Sums the numbers in the Simpy object."""
        return sum(self.values)

    def __add__(self, lhs: Union[Simpy, float]) -> Simpy:
        """Addition operator overload."""
        result: list[float] = []
        
        if isinstance(lhs, float):
            for value in self.values:
                result.append(lhs + value)

        else:
            for i in range(len(self.values)):
                result.append(lhs.values[i] + self.values[i])

        return Simpy(result)

    def __pow__(self, lhs: Union[Simpy, float]) -> Simpy:
        """Exponential operator overload."""
        result: list[float] = []
        
        if isinstance(lhs, float):
            for value in self.values:
                result.append(value ** lhs)

        else:
            for i in range(len(self.values)):
                result.append(self.values[i] ** lhs.values[i])

        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equals operator overload."""
        result: list[bool] = []
        
        if isinstance(rhs, float):
            for value in self.values:
                if rhs == value:
                    result.append(True)
                else:
                    result.append(False)

        else:
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than operator overload."""
        result: list[bool] = []
        
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)

        else:
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]

        else:
            result_list: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result_list.append(self.values[i])
            return Simpy(result_list)