# -*- coding: utf-8 -*-
import win32com.client as win32
import re


class ExcelApp:

    def __init__(self):
        self.xlApp = win32.gencache.EnsureDispatch('Excel.Application')          # 静态调度，会进行缓存
        self.xlApp.Visible = True
        self.xlBook = self.xlApp.Workbooks.Add()
        self.xlSheet = self.xlBook.ActiveSheet

        self.title = self.xlSheet.Range(self.xlSheet.Cells(1, 1), self.xlSheet.Cells(1, 15))
        self.title.Value = ('*', 'Mark', 'Xref', 'Class', 'Name', 'Description', 'Width',
                       'Type', 'LSB', 'Offset', 'Min', 'Max', 'Deci', 'Unit/Enum', 'Parent')

        self.title.Font.Bold = True
        self.title.Font.Name = 'MS UI Gothic'
        self.title.Font.Size = 9
        # set the value of column CenterAlign
        self.title.HorizontalAlignment = 3
        # self.title.EntireColumn.AutoFit()
        # self.title.EntireColumn.ColumnWidth = 15
        # self.title.ShrinkToFit = True
        # title.Font.ColorIndex = 3
        self.line = 2

    def insert_item(self, item):
        for i, it in enumerate(item):
            self.xlSheet.Cells(self.line, i+1).Value = it
        self.xlSheet.Range(self.xlSheet.Cells(2, 1), self.xlSheet.Cells(self.line, 15)).Font.Name = 'Arial'
        self.xlSheet.Range(self.xlSheet.Cells(2, 1), self.xlSheet.Cells(self.line, 15)).Font.Size = 10
        self.line = self.line + 1
        self.title.EntireColumn.AutoFit()

    def save_excel(self):
        self.xlBook.SaveAs(r'C:\Users\sd\Desktop\Bosch\test')


if __name__ == '__main__':

    excel = ExcelApp()
    rawItem1 = ' - -LOC-RAM-EdgeFalling Long name-EdgeFalling-1-Float32-1-0-0-10000-0- - '
    rawItem2 = ' - -LOC-RAM-EdgeFalling Long name-EdgeFalling-1-Float32-1-0-0-10000-0- - '
    item1 = re.split('-', rawItem1)
    item2 = re.split('-', rawItem2)
    excel.insert_item(item1)
    excel.insert_item(item2)
    excel.save_excel()




