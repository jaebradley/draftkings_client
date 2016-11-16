class DateTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(date_string):
        return int(date_string[6:-2])