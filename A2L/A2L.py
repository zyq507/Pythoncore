# -*-coding:Windows-1252-*- #
import linecache
import re


def check_block(target, types):
    goal = re.compile(r'/(begin|end) ' + types + r'.*')
    # judge the type of target, a file path or a segment that we got from the file
    try:
        with open(target, 'r') as fp:
            linenum = [line for line, part in enumerate(fp, 1) if re.match(goal, part.strip())]
    except TypeError:
        linenum = [line for line, part in enumerate(target, 1) if re.match(goal, part.strip())]
    # get the start and end index of every segment
    start = [num for n, num in enumerate(linenum) if n % 2 == 0]
    end = [num for n, num in enumerate(linenum) if n % 2 != 0]
    # get the contents of segment with the start and end index
    for block in zip(start, end):
        try:
            segment = linecache.getlines(target)[block[0]:block[1]-1]
        except TypeError:
            segment = target[block[0]:block[1]-1]
        yield segment


def check_string(itemlist, symbol):
    itnum = [num for num, item in enumerate(itemlist) if re.match(symbol + r'.*|.*' + symbol, item)]
    start = [num for n, num in enumerate(itnum) if n % 2 == 0]
    try:
        end = [num for n, num in enumerate(itnum) if n % 2 != 0]
    except TypeError:
        del(start[-1])
        end = None
    for zone in zip(start, end):
        merge = ' '.join(itemlist[zone[0]:zone[1]+1])
        del(itemlist[zone[0]:zone[1]+1])
        itemlist.insert(zone[0], merge)


def del_linecomment(item):
        goal = re.compile(r'(.*)/\*(.*)\*/')
        for num, element in enumerate(item):
            try:
                value = re.match(goal, element)
                item[num] = value.groups()[0].strip()
            except AttributeError:  # this element(string) doesn't have a comment symbol
                pass
        return item


def get_item(path):
    item = []
    for segment in check_block(path, r'MEMORY_SEGMENT'):
        for line in segment:
            
            if not re.match(r'/(begin).*|("")', line.strip()):
                item = line.strip().split(' ')
                break
        for line in check_block(segment, r'CHECKSUM'):
            line = del_linecomment(line)
            for word in line:
                splitword = word.strip().split(' ')
                try:
                    item.append(splitword[1])
                except IndexError:
                    item.append(splitword[0])
        check_string(item, r'"')
        yield item



if __name__ == '__main__':
    for seg in get_item(r'ME9u_AML_1_2_SerialProtocols.a2l'):
        print (seg)
    for seg in get_item(r'test_v6.a2l'):
        print (seg)




