import unittest

from pylogic.syntax import Symbol


class TestSymbol(unittest.TestCase):
    def test_atomic_symbol(self):
        s1 = Symbol('s1')
        s2 = Symbol('s2')
        s1_ = Symbol('s1')

        self.assertEqual(s1.__str__(), 's1')
        self.assertFalse(s1 == s2)
        self.assertTrue(s1 == s1_)

    def test_multiple_symbol_creation(self):
        s1, s2 = Symbol('s1', 's2')

        self.assertEqual(s1.__str__(), 's1')
        self.assertEqual(s2.__str__(), 's2')

        with self.assertRaises(TypeError):
            s3 = Symbol()


if __name__ == '__main__':
    unittest.main()
