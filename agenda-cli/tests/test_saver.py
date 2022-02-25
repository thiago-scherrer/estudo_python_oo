import context
import csv
import os
import unittest


class TestSaver(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'tests/test_file.csv'
        os.environ['CSV_FILE'] = self.csv_file
        self.agenda = context.saver.Agenda()

        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_header_check(self):
        expected = False
        got = self.agenda.header_check()
        self.assertEqual(expected, got)

    def test_saver(self):
        self.agenda.header_check()

        name_want = 'foo'
        telephone_want = '42'
        self.agenda.saver([name_want, telephone_want])

        with open(self.csv_file, 'r', encoding='UTF8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                telephone = row['telephone']
                self.assertEqual(name, name_want)
                self.assertEqual(telephone, telephone_want)


if __name__ == '__main__':
    unittest.main()
