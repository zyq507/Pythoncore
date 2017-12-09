#!/usr/bin/env python
# --*-- encoding: iso-8859-1 --*--

import logmanager

from win32com import client
from win32com.client import constants


class ExcelColors:
    """BGR format color, my favorites :
        -REDLIGHT
        -GREENOLIVE
        -ORANGEDARK
    """
    BLACK = int("000000", 16)
    BLUE = int("FF0000", 16)
    BLUELIGHT = int("CD7418", 16)
    BLUEROYAL = int("E16941", 16)
    BROWN = int("14698B", 16)
    GRAY = int("BEBEBE", 16)
    GREEN = int("00FF00", 16)
    GREENOLIVE = int("70FFCA", 16)
    ORANGE = int("32B7FF", 16)
    ORANGEDARK = int("247FFF", 16)
    PINK = int("AB82FF", 16)
    PURPLE = int("E22B8A", 16)
    RED = int("0000FF", 16)
    REDLIGHT = int("4040FF", 16)
    WHITE = int("FFFFFF", 16)
    YELLOW = int("00D7FF", 16)


class WrapperException(Exception):
    pass


class Win32comExcelWrapper(object):
    def __init__(self):
        # avoid pop up blocking execution during automation
        self.displayAlerts = 0
        # Excel is visible
        self.visible = 0
        # you won't see what happens (faster)
        self.screenUpdating = False
        # clics on the Excel window have no effect
        # (set back to True before closing Excel)
        self.interactive = False
        self.logger = logmanager.getLogger("Excel wrapper")

#######################################################
######                                           ######
######              Basic operations             ######
######                                           ######
#######################################################

    def openExcel(self):
        """ Lauch Excel and set it's configuration"""
        self.logger.info("\n") #hack for better output
        self.logger.info("Opening Excel")
        self.xl = client.Dispatch("Excel.Application")
        self.logger.info("Setting Excel configuration")
        self.xl.DisplayAlerts = self.displayAlerts
        self.xl.Visible = self.visible
        self.xl.ScreenUpdating = self.screenUpdating
        self.xl.Interactive = self.interactive

    def getWorkbook(self, workbook_absolute_path):
        """Open a workbook and returns it"""
        self.logger.info("Opening workbook %s" %workbook_absolute_path)
        return self.xl.Workbooks.Open(workbook_absolute_path)

    def closeWorkbookWithoutSaving(self, wb):
        """close workbook without saving
            -wb : a workbook object
        """
        self.logger.info("Closing workbook without saving")
        wb.Close()

    def saveWorkbook(self, wb):
        """Save the workbook passed in parameters
            -wb : a workbook object
        """
        self.logger.info("Saving workbook")
        wb.Save()

    def saveWorkbookAs(self, wb, filename):
        """Save the workbook passed in parameters with a new name
            -wb : a workbook object
            -filename : a string
        """
        self.logger.info("Saving workbook as %s" %filename)
        wb.SaveAs(filename)

    def closeExcel(self):
        """Put back Excel interativity online and close it"""
        self.logger.info("Re-activating Excel interactivity")
        self.xl.Interactive = True
        self.logger.info("Closing Excel")
        self.xl.Quit()

#######################################################
######                                           ######
######           workbook operations             ######
######                                           ######
#######################################################

    def getWorksheet(self, wb, ws_name_or_number):
        """Returns a worksheet object corresponding to ws_name
            -wb : a workbook object
            -ws_name : string containing the worksheet name or int for it's number
        """
        self.logger.info("Getting worksheet %s" %ws_name_or_number)
        return wb.Sheets(ws_name_or_number)

    def copyWorksheet(self, wb, source_sheet, new_name):
        """Copy a worksheet, source_sheet must be the name of the
        worksheet in a String, you cannot use an integer"""
        self.logger.info("Duplicating worksheet %s to %s" %(source_sheet, new_name))
        ws = wb.Sheets(source_sheet)
        ws.Copy(Before=wb.Sheets(source_sheet))
        ws = wb.Sheets(source_sheet + " (2)")
        ws.Name = new_name

    def deleteworksheet(self, wb, ws_name_or_number):
        """Delete a worksheet, you can use the number of the sheet,
        or it's actual name as a string, the first worksheet is 1"""
        self.logger.info("Deleting worksheet %s" %ws_name_or_number)
        ws = wb.Sheets(ws_name_or_number)
        ws.Delete()

    def insertWorksheet(self, wb, position, name):
        """Insert a new worksheet 1 step behind position
            -wb : workbook object from openWorkbook()
            -position : name or number of a sheet
            -name : name of the new worksheet
        """
        self.logger.info("inserting new worksheet %s before %s" %(name, position))
        wb.Sheets(position).Select()
        new_ws = wb.Worksheets.Add()
        new_ws.Name = name

    def moveWorksheet(self, wb, ws_name_or_number, new_position):
        """Moves a worksheet to a new position
            -wb : workbook object from openWorkbook()
            -ws_name_or_number : the worksheet to move
            -new_position : an int
        """
        self.logger.info("moving worksheet %s just before %s" %(ws_name_or_number, new_position))
        wb.Sheets(ws_name_or_number).Move(Before=wb.Sheets(new_position+1))

    def renameworkSheet(self, wb, ws_name_or_number, new_name):
        """Renames a worksheet
            -wb : workbook object from openWorkbook()
            -ws_name_or_number : the worksheet to rename
            -new_name : the new name
        """
        self.logger.info("Renaming worksheet %s to %s" %(ws_name_or_number, new_name))
        wb.Sheets(ws_name_or_number).Name = new_name

    def hideSheet(self, wb, ws_name_or_number):
        """Hide a worksheet by name or position"""
        self.logger.info("Hiding worksheet %s" %ws_name_or_number)
        wb.Sheets(ws_name_or_number).Visible = False

    def unhideSheet(self, wb, ws_name):
        """Unhide a worksheet by name (a hidden sheet has no position)"""
        self.logger.info("Unhiding worksheet %s" %ws_name)
        wb.Sheets(ws_name).Visible = True

#######################################################
######                                           ######
######              Write operations             ######
######                                           ######
#######################################################

    def writeCellValue(self, ws, row, column, value):
        """Write a value inside a cell
            -ws : worksheet object aquired by calling getWorksheet()
            -row : int representing cell row location
            -column : int representing cell column location
            -value : the value to be written
        """
        self.logger.info("Writing cell(%s, %s) value %s" %(row, column, value))
        ws.Cells(row, column).Value = value

    def writeCellFormula(self, ws, row, column, formula):
        """Write a formula inside a cell
            -ws : worksheet object aquired by calling getWorksheet()
            -row : int representing cell row location
            -column : int representing cell column location
            -formula : the formula to be written
        """
        self.logger.info("Writing cell(%s, %s) formula %s" %(row, column, formula))
        ws.Cells(row, column).FormulaR1C1 = formula

    def writeCell(self, ws, row, column, value):
        """Write a value inside a cell, autodetect forumula by cheking for '='
            -ws : worksheet object aquired by calling getWorksheet()
            -row : int representing cell row location
            -column : int representing cell column location
            -value : the value/formula to be written
        """
        def isFormulaR1C1(value):
            return isinstance(value, (str, unicode)) and len(value) > 1 and value[0] == '='
        if isFormulaR1C1(value):
            self.writeCellFormula(ws, row, column, value)
        else:
            self.writeCellValue(ws, row, column, value)

    def writeAreaCellByCell(self, ws, ul_row, ul_col, data):
        """write the content of data in an excel worksheet, autodetect formula,
        unrecommended for large amount of data, very slow
            -ws : worksheet object aquired by calling getWorksheet()
            -ul_row : upper left row of the location where the data mus be writen
            -ul_col : upper left column of the location where the data mus be writen
            -data : data stored in a list of list, each list is a row
        """
        for row in data:
            paste_column = ul_col
            for value in row:
                self.writeCell(ws, ul_row, paste_column, value)
                paste_column = paste_column +1
            ul_row = ul_row + 1

    def writeAreaInOneCall(self, ws, ul_row, ul_col, data):
        """Write an area in one call, 100 times faster than writing by cell
            -ws : worksheet object aquired by calling getWorksheet()
            -ul_row : upper left row of the location where the data mus be writen
            -ul_col : upper left column of the location where the data mus be writen
            -data : data store in a list of list, each list is a row
        """
        length = len(data)
        width = len(data[0])
        lr_row = ul_row+length-1
        lr_col = ul_col+width-1
        self.logger.info("writring data at location %s,%s to %s,%s" %(ul_row, ul_col, lr_row, lr_col))
        ws.Range(ws.Cells(ul_row, ul_col), ws.Cells(lr_row, lr_col)).Value = data

#######################################################
######                                           ######
######              Read operations              ######
######                                           ######
#######################################################

    def readCellValue(self, ws, row, col):
        """Read the value of a cell
            -ws : the worksheet object
            -row : int containing the row number
            -col : int containing the column number
            -return : value of the cell, type chosed by Excel
        """
        self.logger.debug("Reading cell (%s, %s)" %(row, col))
        return ws.Cells(row, col).Value

    def readCellValueExn(self, ws, location):
        """Read the value of a cell using the Excel notation (Exn)
           for example the cell(1,1) is A1
            -ws : the worksheet object
            -location : Excel Address of the cell (G7 or $G$7, both work)
            -return : value of the cell, type chosed by Excel
        """
        self.logger.debug("Reading cell %s" %(location))
        return ws.Range(location).Value

    def readRowValue(self, ws, row):
        """I don't see the point of doing that (you'll get TONS of None value),
        use read area

        or use ws.Rows(row_number).Value[0]

        """
        self.logger.warn("readRowValue is NOT implemented")

    def readRowsValue(self, ws, top_row, bottom_row):
        """I don't see the point of doing that (you'll get TONS of None value),
        use read area

        or use ws.Range(
                        ws.Rows(top_row_number),
                        ws.Rows(bottom_row_number)
                        ).Value

        """
        self.logger.warn("readRowsValue is NOT implemented")

    def readColumnValue(self, ws, column):
        """I don't see the point of doing that (you'll get TONS of None value),
        use read area

        or use ws.Columns(col_number_or_letter)

        """
        self.logger.warn("readColumnValue is NOT implemented")

    def readColumnsValue(self):
        """I don't see the point of doing that (you'll get TONS of None value),
        use read area

        or use ws.Range(ws.Columns(lef_col), ws.Columns(right_col))

        """
        self.logger.warn("readColumnsValue is NOT implemented")

    def readAreaValues(self, ws, coord):
        """
        Read the values of a rectangular area
            -ws : a worksheet object
            -coord : a excelwrapper.RangeCoordinate object
            -return : a tuple of tuples
        """
        self.logger.info("Reading area ((%s, %s),(%s, %s)) value(s)" %(coord.tline, coord.tcol, coord.bline, coord.bcol))
        return ws.Range(
                         ws.Cells(coord.tline, coord.tcol),
                         ws.Cells(coord.bline, coord.bcol)
                        ).Value

    def readAreaValuesExn(self, ws, exn_coord):
        """
        Read the values of an area using the excel coordinate
        (string looking like that A8:B5 or $A$8:$B$5 both work)
            -ws : a worksheet object
            -exn_coord : a string containing the excel coord of the area
                         (can be a cell, a row, a column, a square, etc)
            -return: depends of the area, a tuple for a cell, a tuple of tuples
                     for a square, etc
        """
        self.logger.info("Reading area %s value(s)" %exn_coord)
        return ws.Range(exn_coord).Value

#######################################################
######                                           ######
######          Location operations              ######
######                                           ######
#######################################################

    def computeColumnLastLine(self, ws, column):
        """
            Compute the last line of a column
                -ws: the worksheet object
                -column : the column number (int) or letter(s) (str)
                -return : an int
        """
        self.logger.debug("Computing column %s.%s last line" %(ws.Name, column))
        used_range = ws.UsedRange
        return ws.Cells(
                        used_range.Row + used_range.Rows.Count,
                        column
                        ).End(constants.xlUp).Row

    def computeLastColumn(self, ws):
        """
            Compute the last column of a worksheet
                -ws : worksheet object
                -return : an int
        """
        self.logger.info("Computing last column of %s" %ws.Name)
        return ws.UsedRange.Column + ws.UsedRange.Columns.Count - 1

#######################################################
######                                           ######
######         conversion operations             ######
######                                           ######
#######################################################

    #TODO : store the last opened workbook to do calculations?
    def computeCellExcelAddress(self, ws, row, col):
        """
            Compute a cell excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -row : row number as int
                -col : column number as int
                -return : excel Address in a string (ex : $G$7 for cell 7, 3)
        """
        self.logger.info("Converting cell %s, %s Address" %(row, col))
        return ws.Cells(row, col).GetAddress()

    def computeAreaExcelAddress(self, ws, coord):
        """
            Compute an area excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -coord : a excelwrapper.RangeCoordinate object
                -return : excel Address in a string
                          (ex : $C$1:$G$13 for RangeCoordinate(1, 3, 13, 7))
        """
        self.logger.info("Converting area ((%s, %s),(%s, %s)) Address" %(coord.tline, coord.tcol, coord.bline, coord.bcol))
        return ws.Range(
                        ws.Cells(coord.tline, coord.tcol),
                        ws.Cells(coord.bline, coord.bcol)
                        ).GetAddress()

    def ComputeColumnExcelAddress(self, ws, col):
        """
            Compute a column excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -col : column number as an int
                -return : excel Address in a string (ex : $J:$J for col 10)
        """
        self.logger.info("Converting column %s Address" %col)
        return ws.Columns(col).GetAddress()

    def computeColumnsExcelAddress(self, ws, left_col, right_col):
        """
            Compute a range of columns excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -col : column number as an int
                -return : excel Address in a string (ex : $E:$I for cols 5 to 9)
        """
        self.logger.info("Converting colums %s to %s Address" %(left_col, right_col))
        return ws.Range(
                        ws.Columns(left_col),
                        ws.Columns(right_col)
                        ).GetAddress()

    def computeRowExcelAddress(self, ws, row):
        """
            Compute a row excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -row : row number as an int
                -return : excel Address in a string (ex : $7:$7 for row 7)
        """
        self.logger.info("Converting row %s Address" %row)
        return ws.Rows(row).GetAddress()

    def computeRowsExcelAddress(self, ws, top_row, bottom_row):
        """
            Compute a rows range excel Address from numerical coordinate
                -ws : a worksheet object, any worksheet, it's in fact excel
                      which will compute the cell Address from the coordinate
                -top_row : top row number as an int
                -bottom_row : bottom row number as an int
                -return : excel Address in a string (ex : $7:$8 for row 7 to 8)
        """
        self.logger.info("Converting rows %s to %s Address" %(top_row, bottom_row))
        return ws.Range(
                        ws.Rows(top_row),
                        ws.Rows(bottom_row)
                        ).GetAddress()

    def computeAreaAddressFromData(self, ws, start_row, start_col, data):
        """
            Compite the Address of and area from data (list of lists or tuple
            of tuples), the area start from start_row and start_col obviously
                -ws : a worsheet object
                -start_row : start row as a int
                -start_col as an int
                -data : list of lists or tuple of tuples
                -return : Excel Address string like EY32:ZZ55
        """
        self.logger.info("Computing adress occupied by a data block starting"
                         + "at (%s, %s)" %(start_row, start_col))
        return ws.Range(
                        ws.Cells(start_row, start_col),
                        ws.Cells(start_row + len(data) - 1,
                                 start_col + len(data[0]) - 1)
                        ).GetAddress(RowAbsolute=False, ColumnAbsolute=False)

#######################################################
######                                           ######
######          delete/insert operations         ######
######                                           ######
#######################################################

    def deleteColumn(self, ws, columns):
        """
            Delete on or several columns, the shifting is set to left (like in excel)
                -ws : a worksheet object
                -columns : an int for a single column, a string for several ones (ex : D:K)
                           computeColumn(s)ExcelAdress can be used to get that string
        """
        self.logger.info("Deleting column(s) %s from %s" %(columns, ws.Name))
        ws.Columns(columns).Delete(Shift=constants.xlToLeft)

    def deleteRow(self, ws, rows):
        """
            Delete on or several rows, the shifting is set Up (like in excel)
                -ws : a worksheet object
                -rows : an int for a single row, a string for several ones (ex : '7:15')
                        computeRow(s)ExcelAdress can be used to get that string
        """
        self.logger.info("Deleting row(s) %s from %s" %(rows, ws.Name))
        ws.Rows(rows).Delete(Shift=constants.xlUp)

    def insertEmptyColumn(self, ws, column):
        """
            insert one column, the shifting is set to Right (like in excel)
                -ws : a worksheet object
                -columns : an int for a single column or a string containing it's Excel adress
        """
        self.logger.info("Inserting empty column at %s in %s" %(column, ws.Name))
        ws.Columns(column).Insert(Shift=constants.xlToRight,
                                  CopyOrigin=constants.xlFormatFromLeftOrAbove)

    def insertEmptyRow(self, ws, row):
        """insert a new row, the shifting is set to down (like in excel)
            -ws : a worksheet object
            -row : an int for a single row, or a string (ex : '7:7' for row 7)
        """
        self.logger.info("Inserting empty row at %s in %s" %(row, ws.Name))
        ws.Rows(row).Insert(Shift=constants.xlDown,
                            CopyOrigin=constants.xlFormatFromLeftOrAbove)

    def clearCell(self, ws, row, col):
        """
            Clear a cell : reset everything, you get a blank cell
            No formula, color, value remaining
                -ws : a worksheet object
                -row : int containing the row of the cell
                -col : int containing the columns of the cell
        """
        self.logger.info("Clearing cell %s.%s on %s" %(row, col, ws.Name))
        ws.Cells(row, col).ClearContents()

    def clearArea(self, ws, exnadr):
        """
            Clear an area : reset everything, you get a blank cell
            No formula, color, value remaining
                -ws : a worksheet object
                -exnadr : excel adress, can be converted from numerical values
                          using the computeXXXXExcelAddress methods
        """
        self.logger.info("Clearing area %s in %s" %(exnadr, ws.Name))
        ws.Range(exnadr).ClearContents()

#######################################################
######                                           ######
######         copy/paste operations             ######
######                                           ######
#######################################################

    def copyPasteColumns(self, src_ws, dst_ws, sourceColumns, destColumn, cut=False):
        """
            you can copy one or several columns, if only one then use it's int
            number or excel adress (ex ; 'J:J') the destination can be used the same way.
            If copying several columns then use the excel adress for the source (ex : 'B:R')
            and use for the destColmun it's int number or excel adress.

            you can also copy over the same worksheet using src_ws == dst_ws
            And yes, if you use 2 ws from different workbook, it will paste across them.

            If you copy several columns then the left column will correspond
            to destColumn
                -src_ws : a worksheet object
                -dst_ws : a worksheet object
                -souceColumns : Excel adress of one or several columns
                                ('J:J' = column J, 'J:K' = col J to K)
                                Adress can be converted from int with computeColumnsExcelAddress
                -destColumn : int or Excel adress of ONE column
                -cut : set to True to cut/paste instead of copy/paste
        """
        if cut:
            src_ws.Columns(sourceColumns).Cut()
        else:
            src_ws.Columns(sourceColumns).Copy()
        dst_ws.Paste(dst_ws.Columns(destColumn))

    def copyPasteRows(self, src_ws, dst_ws, sourceRows, destRow, cut=False):
        """
            you can copy one or several rows, if only one then use it's int
            number or excel adress (ex ; 'J:J') the destination can be used the same way.
            If copying several rows then use the excel adress for the source (ex : '7:10')
            and use for the destRow it's int number or excel adress.

            you can also copy over the same worksheet using src_ws == dst_ws
            And yes, if you use 2 ws from different workbook, it will paste across them.

            If you copy several Rows then the top row will correspond to destRow
                -src_ws : a worksheet object
                -dst_ws : a worksheet object
                -souceRows : Excel adress of one or several Rows
                             ('J:J' = column J, 'J:K' = col J to K)
                             Adress can be converted from int with computeRowsExcelAddress
                -destRow : int or Excel adress of ONE row
                -cut : set to True to cut/paste instead of copy/paste
        """
        if cut:
            src_ws.Rows(sourceRows).Cut()
        else:
            src_ws.Rows(sourceRows).Copy()
        dst_ws.Paste(dst_ws.Rows(destRow))

    def copyPasteArea(self, src_ws, dst_ws, sourceArea, destCell, cut=False):
        """
            copy and paste an area, use only excel addresses (you can convert numerical value
            using computeAreaExcelAddress and computeCellExcelAdress)

            And yes, if you use 2 ws from different workbook, it will paste across them.

            -src_ws : source worksheet object
            -dst_ws : destination worksheet object (you can use src == dst to copy on the same sheet)
            -sourceArea : an area excel address ('C23' for a single cell, 'A35:G42' an area)
            -destCell : a cell excel address (ex : 'C23) it will correspond the the top left corner
                        of the area to paste
        """
        if cut:
            src_ws.Range(sourceArea).Cut()
        else:
            src_ws.Range(sourceArea).Copy()
        dst_ws.Paste(dst_ws.Range(destCell))

#######################################################
######                                           ######
######          Advanced operations              ######
######                                           ######
#######################################################

    def changeCharColor(self, ws, row, col, color):
        """
            Change the color of the text in a cell
                -ws : a worksheet object
                -row : int containing the row number of the cell
                -col : int containing the col number of the cell
                -color : BGR int representing a color (you can use the ExcelColors class)
        """
        ws.Cells(row, col).Font.Color = color

    def readCharColor(self, ws, row, col):
        """
            Change the color of the text in a cell
                -ws : a worksheet object
                -row : int containing the row number of the cell
                -col : int containing the col number of the cell
                -return : BGR int representing a color
        """
        return ws.Cells(row, col).Font.Color

    def changeCellColor(self, ws, row, col, color):
        """
            Change the color of a cell
                -ws : a worksheet object
                -row : int containing the row number of the cell
                -col : int containing the col number of the cell
                -color : BGR int representing a color (you can use the ExcelColors class)
        """
        ws.Cells(row, col).Interior.Color = color

    def readCellColor(self, ws, row, col):
        """
            Change the color of a cell
                -ws : a worksheet object
                -row : int containing the row number of the cell
                -col : int containing the col number of the cell
                -return : BGR int representing a color
        """
        return ws.Cells(row, col).Interior.Color

    def sortArea(self, ws, exn_coord, column, orientation):
        """
            Sort an area, do not put the header of the area in the selection!
                -ws : a worksheet object
                -exn_coor : an excel address in a string (ex : 'A2:G255')
                -column : the column witch is going to matter as an int or string (2 or 'B:B')
                -orientation : constants.xlDescending or constants.xlAscending
        """
        ws.Range(exn_coord).Sort(
                                 Key1=ws.Columns(column),
                                 Order1=orientation,
                                 SortMethod=constants.xlPinYin,
                                 Orientation = constants.xlTopToBottom
                                 )

    class RangeCoordinate():
        """
        Class representing a Range Coordinate, typical use :

        data = ws.Range(
                         ws.Cells(coord.tline, coord.tcol),
                         ws.Cells(coord.bline, coord.bcol)
                        ).Value
        """
        def __init__(self, tline, tcol, bline, bcol):
            """Constructor
                -tline : top left line, int
                -tcol : top left column, int
                -bline : bottom right line, int
                -bcol : bottom right column, int
            """
            self.tline = tline
            self.tcol = tcol
            self.bline = bline
            self.bcol = bcol
