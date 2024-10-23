import pandas


class Migration():


    def __init__(self, url):
        self.doc = pandas.read_excel(url, engine="odf")
        print(type(self.doc))
