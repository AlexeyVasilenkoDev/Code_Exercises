import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.f = Fibonacci()

    def test_zero(self):
        self.assertEqual(self.f(0), 0)

    def test_negative(self):
        self.assertRaises(ValueError, self.f, -10)

    def test_biggest_number_allowed(self):
        self.assertEqual(self.f(485), 102216385354134324778078911974689347564945335253989394162085272183728832930964492342791374522266860485)  # biggest allowed value without RecursionError

    def test_too_big_number(self):
        self.assertRaises(RecursionError, self.f, 100000000)

    def test_invalid_parameter(self):
        self.assertRaises(ValueError, self.f, 'Hello')


if __name__ == "__main__":
    unittest.main()
