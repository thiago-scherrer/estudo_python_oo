import context
import csv
import mock
import os
import unittest


class TestPrompter(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'tests/test_file.csv'
        os.environ['CSV_FILE'] = self.csv_file
        self.prompter = context.prompter.Input()

        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_prompter(self):
        expected = 2
        mock_user = 'foo'

        with mock.patch('builtins.input', return_value=mock_user):
            self.prompter.add_contact()

            with open(self.csv_file, 'r', encoding='UTF8') as file:
                reader = csv.reader(file)

                for index, line in enumerate(reader, 1):
                    self.assertEqual(line.count(mock_user), expected)
                    break


if __name__ == '__main__':
    unittest.main()
