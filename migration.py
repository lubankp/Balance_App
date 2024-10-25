from datetime import datetime
import ezodf

class Migration():

    def __init__(self, url):
        self.doc = ezodf.opendoc(url)
        self.sheet = self.doc.sheets[0]
        self.array = []

    def find_value(self, row, position):
        for i, cell in enumerate(row):
             if i == position:
                 # print('{}, {}'.format(cell.value, type(cell.value)))
                 return cell.value

    def find_pos(self):
        for row in self.sheet.rows():
            for i, cell in enumerate(row):
                if cell.value == 'Data':
                    self.data_pos = i
                elif cell.value == 'PKOSA':
                    self.pkosa_pos = i
                elif cell.value == 'Mbank':
                    self.mbank_pos = i
                elif cell.value == 'Revolut':
                    self.revolut_pos = i

    def fix_data(self):
        self.find_pos()
        for row in self.sheet.rows():
            if row[0].value and row[0].value != 'Data':
                self.array.append({ 'Date': self.find_value(row, self.data_pos),
                                    'PKOSA': self.find_value(row, self.pkosa_pos),
                                    'Mbank': self.find_value(row, self.mbank_pos),
                                    'Revolut': self.find_value(row, self.revolut_pos),})
        return self.array


