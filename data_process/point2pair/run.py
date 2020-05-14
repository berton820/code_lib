import sys
import logging
import traceback
import itertools


def data_load():
    sys.stdin = open('./hexi.txt', 'r', encoding='utf-8')
    for (sen_1, group) in itertools.groupby(
            iter([(yield line.strip().split('\t')) for line in sys.stdin]),
            lambda item: item[0]):
        try:
            if not sen_1:
                continue
            handle(group)
        except:
            logging.warning(traceback.format_exc())
            continue


def handle(group):
    all_data = []
    for i in group:
        if i in all_data:
            continue
        all_data.append(i)
    if len(all_data) == 1:
        print('\t'.join(str(i) for i in all_data[0]))
        return

    opt = {}
    for i in all_data:
        k = str(i[0]) + '-' + str(i[1]) + '-' + str(i[2])
        if k not in opt:
            opt[k] = []
        for j in all_data:
            if int(i[2]) > int(j[2]):
                if j not in opt[k]:
                    opt[k].append(j)
    for k in opt:
        if len(opt[k]) == 0:
            continue
        for v in opt[k]:
            p = k.strip().split('-') + v
            print('\t'.join(str(i) for i in p))


if __name__ == '__main__':
    data_load()