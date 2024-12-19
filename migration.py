# Imports libraries
import ezodf

class Migration():
    """Allows to migrate data from file"""

    def __init__(self, url):
        self.doc = ezodf.opendoc(url)
        self.sheet = self.doc.sheets[0]
        self.array = []

    def find_value(self, row, position):
        """Returns value for each cell"""
        for i, cell in enumerate(row):
             if i == position:
                 return cell.value

    def find_pos(self):
        """Finds position of columns in migrated file"""
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
        """Fixes data to Database model"""
        self.find_pos()
        for row in self.sheet.rows():
            if row[0].value and row[0].value != 'Data':
                self.array.append({ 'Date': self.find_value(row, self.data_pos),
                                    'PKOSA': self.find_value(row, self.pkosa_pos),
                                    'Mbank': self.find_value(row, self.mbank_pos),
                                    'Revolut': self.find_value(row, self.revolut_pos),})
        return self.array


