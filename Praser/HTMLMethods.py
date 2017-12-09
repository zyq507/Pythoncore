"""
HTML Method Library
"""


class HTMLMethods:
    """
    These Methods are used for HTML files
    """
    def __init__(self):
        self.text = None

    def chapter(self, text):
        return (self.__str_connect(items) for items in text.find_all('h1'))

    @staticmethod
    def traverse(text):
        for child in text.children:
            print child

    @staticmethod
    def __str_connect(text):
        return ''.join([item.get_text() for item in text.find_all('span', recursive=False)])
