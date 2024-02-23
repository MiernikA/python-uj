import unittest
import fracs


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = 0

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([-1, 2], [1, 2]), self.zero)
        self.assertEqual(fracs.add_frac([0, 1], [1, 2]), [1, 2])
        self.assertEqual(fracs.add_frac([3, 4], [-1, 4]), [1, 2])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(fracs.sub_frac([0, 1], [1, 2]), [-1, 2])
        self.assertEqual(fracs.sub_frac([3, 4], [-1, 4]), [1, 1])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([-1, 2], [1, 2]), [-1, 4])
        self.assertEqual(fracs.mul_frac([0, 1], [1, 2]), self.zero)
        self.assertEqual(fracs.mul_frac([3, 4], [-1, 4]), [-3, 16])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(fracs.div_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(fracs.div_frac([0, 1], [1, 2]), self.zero)
        self.assertEqual(fracs.div_frac([3, 4], [-1, 4]), [-3, 1])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([1, 2]))
        self.assertFalse(fracs.is_positive([-1, 2]))
        self.assertFalse(fracs.is_positive([0, 1]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0, -2]))
        self.assertTrue(fracs.is_zero([0, 2]))
        self.assertFalse(fracs.is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([-1, 2], [1, 2]), -1)
        self.assertEqual(fracs.cmp_frac([0, 1], [1, 2]), -1)
        self.assertEqual(fracs.cmp_frac([3, 4], [-1, 4]), 1)
        self.assertEqual(fracs.cmp_frac([1, 2], [2, 4]), 0)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([-1, 2]), -0.5)
        self.assertEqual(fracs.frac2float([0, 1]), 0.0)
        self.assertEqual(fracs.frac2float([3, 4]), 0.75)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
