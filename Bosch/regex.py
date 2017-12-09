import re

m = re.match('foo', 'foo')
if m is not None:
    print m.group()

t = re.findall('foo','foo is very foo and foolish foo.')
print t
