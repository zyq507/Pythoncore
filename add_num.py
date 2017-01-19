import fileinput

for line in fileinput.input(files=r'LibTest.py'):
    line = line.strip()
    num  = fileinput.lineno()
    print('%-40s #%2i'%(line,num))
    
fileinput.close()
