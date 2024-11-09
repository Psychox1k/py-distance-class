from __future__ import annotations


class Distance:

    def __init__(self, km: int):
        self.km = km

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other):
        return Distance(self.km * other)

    def __truediv__(self, other):
        return Distance(round(self.km / other, 2))

    def __le__(self, other: Distance | int | float):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Distance | int | float):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __eq__(self, other: Distance | int | float):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __lt__(self, other: Distance | int | float):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | int | float):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other
