from py_rational.rational import Rational


def test_addition_works_as_expected() -> None:
    r1 = Rational(1, 2)
    r2 = Rational(1, 2)
    r3 = r1 + r2
    expected = Rational(1, 1)
    assert expected == r3

    r1 = Rational(1, 2)
    r2 = Rational(1, 4)
    r3 = r1 + r2
    expected = Rational(3, 4)
    assert expected == r3

    r1 = Rational(3, 8)
    r2 = Rational(1, 4)
    r3 = r1 + r2
    expected = Rational(5, 8)
    assert expected == r3


def test_subtraction_works_as_expected() -> None:
    r1 = Rational(1, 2)
    r2 = Rational(1, 2)
    r3 = r1 - r2
    expected = Rational(0, 1)
    assert expected == r3

    r1 = Rational(1, 2)
    r2 = Rational(1, 4)
    r3 = r1 - r2
    expected = Rational(1, 4)
    assert expected == r3


def test_multiplication_works_as_expected() -> None:
    r1 = Rational(1, 2)
    r2 = Rational(1, 2)
    r3 = r1 * r2
    expected = Rational(1, 4)
    assert expected == r3

    r1 = Rational(1, 2)
    r2 = Rational(4, 1)
    r3 = r1 * r2
    expected = Rational(2, 1)
    assert expected == r3


def test_division_works_as_expected() -> None:
    r1 = Rational(1, 2)
    r2 = Rational(1, 2)
    r3 = r1 / r2
    expected = Rational(1, 1)
    assert expected == r3

    r1 = Rational(1, 2)
    r2 = Rational(4, 1)
    r3 = r1 / r2
    expected = Rational(1, 8)
    assert expected == r3


def test_lcm() -> None:
    assert 21 == Rational.lcm(3, 7)
    assert 24 == Rational.lcm(8, 12)
    assert 255 == Rational.lcm(15, 17)
    assert 5940 == Rational.lcm(180, 594)


def test_gcd() -> None:
    assert 1 == Rational.gcd(3, 7)
    assert 4 == Rational.gcd(8, 12)
    assert 1 == Rational.gcd(15, 17)
    assert 18 == Rational.gcd(180, 594)
