import unittest
import context


class TestHelpers(unittest.TestCase):

    def test_basic_return(self):
        expected = None
        got = context.core.entrypoint()

        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
