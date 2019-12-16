# among top 10 percent authors,
# 1. filter out non trials,
# 2. calculate the ratio of angular for each half time span for each developer
# 3. print the statistics
#  read in 10percentauthors.react.angular as filter

import sys

# read in 10 percent authors
authors_file = sys.argv[1]
authors = set([])
with open(authors_file, 'r') as f:
    for line in f:
        authors.add(line.strip())

# get all data from stdin
# in order to make it easy, I will add one "ending line" to stdin, i.e. author.time.react.angular.commits
current_author = ""
time2counts = {}
for line in sys.stdin:
    items = line.strip().split(';')
    author = items[0]
    if author not in authors:
        continue
    cmt_time = items[1]
    if author == current_author:
        time2counts[cmt_time] = ','.join(items[2].split(',')[:2])
        continue
    else:
        # calculate the ratio, then get next author
        timeRange = sorted(time2counts.keys())
        mid_time = (int(timeRange[0]) + int(timeRange[1]))/2
        react_pre_counts = 0
        angular_pre_counts = 0
        react_aft_counts = 0
        angular_aft_counts = 0
        for t in timeRange:
            countR, countA = time2counts[t].split(',')[:2]
            if int(t) < mid_time:
                react_pre_counts += int(countR)
                angular_pre_counts += int(countA)
            else:
                react_aft_counts += int(countR)
                angular_aft_counts += int(countA)
        pre_ratio = angular_pre_counts/float(angular_pre_counts + react_pre_counts)
        aft_ratio = angular_aft_counts/float(react_aft_counts + angular_aft_counts)
        print(';'.join([author, str(pre_ratio), str(aft_ratio), str(pre_ratio > aft_ratio)]))
        # re-initiate
        current_author = author
        time2counts = {}
