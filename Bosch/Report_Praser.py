from bs4 import BeautifulSoup
import MethodBox


class HTMLReport:
    """
    THis is  a HTML report.
    """
    def __init__(self, path):
        with open(path, 'r') as fp:
            self.report = BeautifulSoup(fp, "lxml")
        self.head = self.report.head
        self.body = self.report.body


if __name__ == '__main__':

    report = HTMLReport(r'C:\Users\sd\Desktop\sldemo_engine\root.html')
    praser = MethodBox.MethodBox('HTML')
    praser.get_func('traverse', report.body)

