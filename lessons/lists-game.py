"""Learning lists. Adds random dice rolls to a list until the numeber 1 is rolled."""

from random import randint


rolls: list[int] = list()
i: int = 0

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    if len(rolls) != 0:
        rolls.pop()
    i += 1
    rolls.append(randint(1, 6))

print(i)
print(rolls)