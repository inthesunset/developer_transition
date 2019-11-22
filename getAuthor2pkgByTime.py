import sys
from collections import defaultdict
import bisect
import json

author2pkgs = defaultdict(list)
for line in sys.stdin:
    items = line.strip().split(';')
    pkgs = items[0]
    author = items[5]
    time = int(items[4])
    bisect.insort(author2pkgs[author], (time, pkgs))
#print(json.dumps(author2pkgs, ensure_ascii=False))

# Let's parse each author
# Regarding cases, please refer to ReadMe.md
for author, values in author2pkgs:
    # get the trace of pkg use
    trace = [value[1] for value in values]
    # detect case 1, if is coherent always
    if len(set(trace)) == 1 and ',' not in set(trace)[0]:
        print(author + ';' + 'case 1;' + values[0][1])
        continue
    # detect case 2
    prev = 0
    dump_trace = []
    for i in range(len(trace)):
        if prev != trace[i]:
            dump_trace.append(trace[i])
            prev = trace[i]
    if ',' not in '.'.join(dump_trace):
        # exclude cases where single blob involves multiple frameworks
        if len(dump_trace) == len(set(dump_trace)):
            print(author + ';' + 'case 2;' + ';'.join(dump_trace))
        else:
            # indicating that loops exists, including case 3, 4, 5. need more analysis
            print(author + ';' + 'case 3,4,5;' + ';'.join(dump_trace))
            # detect case 3, 4, 5
        continue
    print(author + ';' + ' multiple involved in sigle blob;' + ';'.join(dump_trace))
