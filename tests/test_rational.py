from unittest import TestCase

from py_rational.rational import Rational


class TestRational(TestCase):
    def test_addition_works_as_expected(self) -> None:
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 + r2
        expected = Rational(1, 1)
        self.assertEqual(expected, r3)

        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        r3 = r1 + r2
        expected = Rational(3, 4)
        self.assertEqual(expected, r3)

        r1 = Rational(3, 8)
        r2 = Rational(1, 4)
        r3 = r1 + r2
        expected = Rational(5, 8)
        self.assertEqual(expected, r3)

    def test_subtraction_works_as_expected(self) -> None:
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 - r2
        expected = Rational(0, 1)
        self.assertEqual(expected, r3)

        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        r3 = r1 - r2
        expected = Rational(1, 4)
        self.assertEqual(expected, r3)

    def test_multiplication_works_as_expected(self) -> None:
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 * r2
        expected = Rational(1, 4)
        self.assertEqual(expected, r3)

        r1 = Rational(1, 2)
        r2 = Rational(4, 1)
        r3 = r1 * r2
        expected = Rational(2, 1)
        self.assertEqual(expected, r3)

    def test_division_works_as_expected(self) -> None:
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 / r2
        expected = Rational(1, 1)
        self.assertEqual(expected, r3)

        r1 = Rational(1, 2)
        r2 = Rational(4, 1)
        r3 = r1 / r2
        expected = Rational(1, 8)
        self.assertEqual(expected, r3)

    def test_lcm(self) -> None:
        self.assertEqual(21, Rational.lcm(3, 7))
        self.assertEqual(24, Rational.lcm(8, 12))
        self.assertEqual(255, Rational.lcm(15, 17))
        self.assertEqual(5940, Rational.lcm(180, 594))

    def test_gcd(self) -> None:
        self.assertEqual(1, Rational.gcd(3, 7))
        self.assertEqual(4, Rational.gcd(8, 12))
        self.assertEqual(1, Rational.gcd(15, 17))
        self.assertEqual(18, Rational.gcd(180, 594))
