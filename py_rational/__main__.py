"""
This is the main program.
"""


from py_rational.rational import Rational


def main() -> None:
    r0 = Rational(3, 8)
    r1 = Rational(1, 4)
    r2 = Rational(1, 4)
    r3 = Rational(11, 17)

    res0: Rational = r0 + r2
    res1: Rational = r2 - r1
    res2: Rational = r1 * r2
    res3: Rational = r3 / r1

    print(res0)
    print(res1)
    print(res2)
    print(res3)


if __name__ == "__main__":
    main()
