# trying to measure the commit density by month, i.e., the beginning month is the first commit month
from datetime import datetime
# datetime.utcfromtimestamp(unixtime).strftime('%Y%m%d')
import sys
from collections import defaultdict
#read in file 10percentauthors.react.angular as targeted author
targeted_authorFile = sys.argv[1]
targeted_author = set()
with open(targeted_authorFile, 'r') as f:
    for line in f:
        targeted_author.add(line.strip())

author2month = defaultdict(dict)
for line in sys.stdin:
    items = line.strip()
    author = items[0]
    if author in  targeted_author:
        unixtime = items[1]
        react, angular, commit_num = items[3].split(',')
        month = datetime.utcfromtimestamp(unixtime).strftime('%Y%m')
        current_num = author2month[author].get(month, [0, 0])
        author2month[author][month] = [sum for i in zip(current_num, [int(react), int(angular)])]

# leave the gap empty
# dump data
for author, months in author2month:
    s = sorted(list(months.keys()))
    for month in s:
        print(author+';'+month+';'+','.join(map(str, months[s])))
