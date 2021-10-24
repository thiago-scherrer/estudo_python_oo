import csv
import os


class Agenda:
    def __init__(self):
        self.header = ['name', 'telephone']
        tmp_csv_file = '/tmp/agenda.csv'

        try:
            self.csv_file = os.environ['CSV_FILE']
        except KeyError:
            self.csv_file = tmp_csv_file
            print(f'Env CSV_FILE not found, using {tmp_csv_file}')

    def header_check(self):
        try:
            with open(self.csv_file, 'r', encoding='UTF8') as file:
                reader = csv.reader(file)

                for index, line in enumerate(reader, 1):

                    if line.count('name') != 1:
                        self.saver(self.header)
                        return False

                    break

        except FileNotFoundError:
            self.saver(self.header)
            return False

    def saver(self, filds):
        with open(self.csv_file, 'a', encoding='UTF8', newline='') as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(filds)


if __name__ == "__main__":
    Agenda().header_check()
