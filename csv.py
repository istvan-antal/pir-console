class CSVFile(object):
    def __init__(self, file_name, headers):
        try:
            with open(file_name) as f:
                pass
        except IOError:
            self.create_file(file_name, headers)
        self.file_name = file_name

    def create_file(self, file_name, headers):
        with open(file_name, 'w') as f:
            f.write(','.join(headers) + '\n')

    def add_row(self, columns):
        with open(self.file_name, 'a') as f:
            f.write(','.join(columns) + '\n')

#csv_file = CSVFile("stats.csv", ['time'])
#csv_file.add_row(['x'])