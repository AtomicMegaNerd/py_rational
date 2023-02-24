from typing import Self


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
        g: int = Rational.gcd(self.numer, self.denom)
        self.numer = self.numer // g
        self.denom = self.denom // g

        if self.numer < 0 and self.denom < 0:
            self.numer = abs(self.numer)
            self.denom = abs(self.denom)

    def reciprocal(self) -> Self:
        return Rational(self.denom, self.numer)

    def __str__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: Self) -> Self:
        l = Rational.lcm(self.denom, other.denom)
        return Rational(
            (self.numer * l // self.denom) + (self.numer * l // other.denom), l
        )

    def __sub__(self, other: Self) -> Self:
        l = Rational.lcm(self.denom, other.denom)
        return Rational(
            (self.numer * l // self.denom) - (self.numer * l // other.denom), l
        )

    def __mul__(self, other: Self) -> Self:
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: Self) -> Self:
        return self * other.reciprocal()

    def __floordiv__(self, other: Self) -> Self:
        return self.__truediv__(other)
