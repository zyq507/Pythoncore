"""
THis is the python file of different methods.
"""
import HTMLMethods


class MethodBox:
    """
    The method box that can be used to prase the report
    It can be used with HTML and other prasers
    """
    def __init__(self, typ):
        self.typ = typ
        try:
            classname = ''.join([self.typ, 'Methods'])
            self.methods = eval(''.join([classname, '.', classname, '()']))
            print '%s_Methodbox is loaded.' % typ
        except NameError:
            print 'There is no %s_Methodbox' % typ

    def get_func(self, func_name, text):
        method = getattr(self.methods, func_name, None)
        if hasattr(method, '__call__'):
            return method(text)
        else:
            print 'This methodbox does not have this function' + " '%s'" % func_name + '.'


