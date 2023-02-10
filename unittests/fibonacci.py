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

    def test_zero(self):
        self.assertEqual(Fibonacci()(0), 0)

    def test_negative(self):
        self.assertRaises(ValueError, Fibonacci(), -10)

    def test_biggest_number_allowed(self):
        """Biggest allowed value without RecursionError"""
        self.assertEqual(Fibonacci()(485), 102216385354134324778078911974689347564945335253989394162085272183728832930964492342791374522266860485)

    def test_too_big_number(self):
        self.assertRaises(RecursionError, Fibonacci(), 100000000)

    def test_invalid_parameter(self):
        self.assertRaises(ValueError, Fibonacci(), 'Hello')


if __name__ == "__main__":
    unittest.main()
