# -*-coding:utf-8-*- #
import linecache
import re


def check_block(target, types):
    goal = re.compile(r'/(begin|end) ' + types + r'.*')
    try:
        with open(target, 'r') as fp:
            sliceindex = find_slice_inlist(fp, goal)
    except TypeError:
        sliceindex = find_slice_inlist(target, goal)
    for block in sliceindex:
        try:
            segment = linecache.getlines(target)[block[0]:block[1]+1]
            segment = split_segment(segment)
            segment = clear_itemlist(segment)
        except TypeError:
            segment = target[block[0]:block[1]+1]
        yield segment


def merge_slice(itemlist, sliceindex):
    for zone in sliceindex:
        merge = ' '.join(itemlist[zone[0]:zone[1]+1])
        itemlist[zone[0]:zone[1]+1] = [merge] + ['$$']*(zone[1]-zone[0])


def merge_tag(itemlist, sliceindex):
    for zone in sliceindex:
        start_tag = ' '.join(itemlist[zone[0]:zone[0]+2])
        end_tag = ' '.join(itemlist[zone[1]:zone[1]+2])
        itemlist[zone[0]:zone[0] + 2] = [start_tag] + ['$$']
        itemlist[zone[1]:zone[1] + 2] = [end_tag] + ['$$']


def find_slice_inlist(target, regx):
    region = [index for index, element in enumerate(target)
              if re.match(regx, element.strip())]
    start_index = [num for n, num in enumerate(region) if n % 2 == 0]
    end_index = [num for n, num in enumerate(region) if n % 2 != 0]
    return zip(start_index, end_index)


def del_slice(itemlist, regx):
    return [item for item in itemlist if not re.match(regx, item)]


def split_segment(segment):
    seglist = []
    for line in segment:
        linelist = line.strip().split(' ')
        seglist += linelist
    return seglist


def clear_itemplaceholder(itemlist):
    temp = [item for item in itemlist if item != '$$' and item != '']
    return temp


def clear_itemlist(tablelist):
    del_commentwithvalue(tablelist)
    merge_tag(tablelist, find_slice_inlist(tablelist, r'/(begin|end)'))
    merge_slice(tablelist, find_slice_inlist(tablelist, r'".*[^"]$|^[^"].*"'))
    merge_slice(tablelist, find_slice_inlist(tablelist, r'/\*|\*/'))
    return clear_itemplaceholder(del_slice(tablelist, r'/\*|\*/'))


def del_commentwithvalue(tablelist):
    for num, item in enumerate(tablelist):
        try:
            t = re.match(r'(.*)/\*(.+)\*/(.*)', item).groups()
            tablelist[num] = t[0] + t[2]
        except AttributeError:
            pass


if __name__ == '__main__':
    for seg in check_block(r'G:\PythonCore\A2L\test_v6.a2l', r'MEASUREMENT'):
        print(seg)



