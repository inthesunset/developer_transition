import sys
# trying to measure the commit density by month, i.e., the beginning month is the first commit month
from datetime import datetime
from statistics import mean, median, stdev
# datetime.utcfromtimestamp(unixtime).strftime('%Y%m%d')
# we need a rough filter on the number of commits, e.g., single commit is helpless

# Let's first have a undersstanding of the number of commits distribution, then select a threshold
# This reads in only the first column of file author.time.react.angular.commits, to calculate statistics
author2commitnum = defaultdict(int)
for line in sys.stdin:
    author2commitnum[line.strip()] += 1

data = list(author2commitnum.values())
print("Mean:\t" + str(mean(data)))
print("Median:\t" + str(median(data)))
print("Stdev:\t" + str(stdev(data)))
