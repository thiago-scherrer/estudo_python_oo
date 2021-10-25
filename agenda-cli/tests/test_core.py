import context
import mock
import unittest


class TestHelpers(unittest.TestCase):

    def test_basic_return(self):
        expected = None

        with mock.patch('builtins.input', return_value='foo'):
            got = context.core.entrypoint()
            self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
