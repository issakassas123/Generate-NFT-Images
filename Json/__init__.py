import json
import os


class JSON:

    def __init__(self, filename):
        self.filename = filename

    def readFromFile(self):
        return json.load(open(file=self.filename))

