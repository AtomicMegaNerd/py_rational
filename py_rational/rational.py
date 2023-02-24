from __future__ import annotations
from typing import Any


class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        self.numer = numer
        self.denom = denom
        self.reduce()

    @staticmethod
    def gcd(x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return Rational.gcd(y, x % y)

    @staticmethod
    def lcm(x: int, y: int) -> int:
        return (x * y) // Rational.gcd(x, y)

    def reduce(self) -> None:
        gcd: int = Rational.gcd(self.numer, self.denom)
        self.numer = self.numer // gcd
        self.denom = self.denom // gcd

        if self.numer < 0 and self.denom < 0:
            self.numer = abs(self.numer)
            self.denom = abs(self.denom)

    def reciprocal(self) -> Rational:
        return Rational(self.denom, self.numer)

    def __str__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other: Rational) -> Rational:
        lcm = Rational.lcm(self.denom, other.denom)
        return Rational(
            (self.numer * lcm // self.denom) + (other.numer * lcm // other.denom), lcm
        )

    def __sub__(self, other: Rational) -> Rational:
        lcm = Rational.lcm(self.denom, other.denom)
        return Rational(
            (self.numer * lcm // self.denom) - (other.numer * lcm // other.denom), lcm
        )

    def __mul__(self, other: Rational) -> Rational:
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: Rational) -> Rational:
        return self * other.reciprocal()

    def __floordiv__(self, other: Rational) -> Rational:
        return self.__truediv__(other)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        return False
