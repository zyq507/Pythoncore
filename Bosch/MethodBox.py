"""
THis is the python file of different methods.
"""


class MethodBox:
    """
    The method box that can be used to prase the report
    It can be used with HTML and other prasers
    """
    def __init__(self, typ):
        self.typ = typ
        try:
            self.methods = eval(''.join([self.typ, 'Methods', '()']))
            print '%s_Methodbox is loaded.' % typ
        except NameError:
            print 'There is no %s_Methodbox' % typ

    def get_func(self, func_name, text):
        method = getattr(self.methods, func_name, None)
        if callable(method):
            return method(text)
        else:
            print 'This methodbox does not have this function' + " '%s'" % func_name + '.'


class HTMLMethods:
    """
    These Methods are used for HTML files
    """
    def __init__(self):
        pass

    @staticmethod
    def traverse(text):
        for child in text.children:
            print child
