# -*- coding: utf-8 -*-
import win32com.client as win32


xlApp = win32.gencache.EnsureDispatch('Excel.Application')          # 静态调度，会进行缓存
xlApp.Visible = True
xlBook = xlApp.Workbooks.Add()
xlSheet = xlBook.ActiveSheet

title = xlSheet.Range(xlSheet.Cells(1, 1), xlSheet.Cells(1, 5))
title.Value = ('*', 'Mark', 'Xref', 'Class', 'Name')
title.Font.Bold = True


xlBook.SaveAs(r'C:\Users\sd\Desktop\Bosch\test')


