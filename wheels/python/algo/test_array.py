from arrays.del_nth import dn
from arrays.flat import f_, f
from arrays.garage import g
from arrays.lnr import lnr
from arrays.zeros_to_end import ze
from arrays.rot_arr import r0, r1, r2, r3
from arrays.two_sum import ts
from arrays.three_sum import ths
from arrays.missing_ranges import mr
from arrays.summary_ranges import sr
from arrays.plus_one import po0, po1

import unittest


class TestArrays(unittest.TestCase):

    def test_delete_nth(self):

        self.assertListEqual(dn([1, 2, 1, 2, 3, 1], n=1), [1, 2, 3])
        self.assertListEqual(dn([3, 3, 2, 2, 2, 2], n=3), [3, 3, 2, 2, 2])
        self.assertListEqual(dn([], n=5), [])
        self.assertListEqual(dn([1, 2, 3, 1, 2, 1], n=0), [])

    def test_flatten(self):

        self.assertEqual(f_([1, [2, [3, []]]]), [1, 2, 3])

    def test_flatten_iter(self):

        a = [1, [2, [3, []]]]
        fa = f(a)
        self.assertEqual(next(fa), 1)
        self.assertEqual(next(fa), 2)
        self.assertEqual(next(fa), 3)
        self.assertRaises(StopIteration, next, fa)

    def test_garage(self):

        i = [1, 2, 3, 0, 4]
        o = [0, 3, 2, 1, 4]
        o2 = [4, 3, 2, 0, 1]

        s, q = g(i, o)
        s2, q2 = g(i, o2)

        self.assertEqual(s, 4)
        #                        [1, 2, 3, 0, 4],
        self.assertListEqual(q, [[0, 2, 3, 1, 4],
                                 [2, 0, 3, 1, 4],
                                 [2, 3, 0, 1, 4],
                                 [0, 3, 2, 1, 4]])

        self.assertEqual(s2, 6)
        #                         [1, 2, 3, 0, 4],
        self.assertListEqual(q2, [[0, 2, 3, 1, 4],
                                  [4, 2, 3, 1, 0],
                                  [4, 2, 3, 0, 1],
                                  [4, 0, 3, 2, 1],
                                  [4, 3, 0, 2, 1],
                                  [4, 3, 2, 0, 1]])

    def test_longest_non_repeat(self):

        self.assertEqual(lnr('pwwkew'), 'wke')

    def test_move_zeros(self):

        self.assertListEqual(ze([0, 1, 'ra', [], None, 0, True, 0]),
                             [1, 'ra', [], None, True, 0, 0, 0])

    def test_rotate(self):

        a = [1, 2, 3, 4, 5]
        r = [4, 5, 1, 2, 3]
        k = 2

        self.assertListEqual(r0(a, k), r)
        self.assertListEqual(r1(a, k), r)
        self.assertListEqual(r2(a, k), r)
        self.assertListEqual(r3(a, k), r)

    def test_two_sums(self):

        a = [1, 1, 2, 3, 4]
        r = [(2, 3), (1, 4)]
        t = 5

        self.assertListEqual(ts(a, t), r)

    def test_three_sum(self):

        a = [-4, 0, 1, 3, 4]

        self.assertEqual(ths(a, 0), {(-4, 0, 4), (-4, 1, 3)})
        self.assertEqual(ths(a, 6), set())

    def test_missing_ranges(self):

        a = [2, 3, 8]
        b = []
        p, q = 1, 10

        self.assertListEqual(mr(a, p, q), [(1, 1), (4, 7), (9, 10)])
        self.assertListEqual(mr(b, p, q), [(1, 10)])

    def test_summary_ranges(self):

        a = [0, 1, 2, 4, 5, 7]
        b = [2]

        self.assertListEqual(sr(a), [(0, 2), (4, 5), (7, 7)])
        self.assertListEqual(sr(b), [(2, 2)])

    def test_plus_one(self):

        a = [0]

        for i in range(101):
            po0(a)

        self.assertListEqual(a, [1, 0, 1])

        for i in range(101):
            po1(a)

        self.assertListEqual(a, [2, 0, 2])


if __name__ == '__main__':

    unittest.main()
