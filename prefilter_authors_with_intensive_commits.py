import sys
import numpy as np
#from statistics import mean, median, stdev, only works on python3, drop it.
from collections import defaultdict
# we need a rough filter on the number of commits, e.g., single commit is helpless
# Let's first have a undersstanding of the number of commits distribution, then select a threshold
# This reads in only the first column of file author.time.react.angular.commits, to calculate statistics
author2commitnum = defaultdict(int)
for line in sys.stdin:
    author2commitnum[line.strip()] += 1

# data = list(author2commitnum.values())
# #print("Mean:\t" + str(mean(data)))
# #print("Median:\t" + str(median(data)))
# #print("Stdev:\t" + str(stdev(data)))
# for i in range(5, 10):
#     print(str(i*10)+ "%:\t" + str(np.percentile(data, i*10)))
# # got result:
# # 50%:	7.0
# # 60%:	9.0
# # 70%:	13.0
# # 80%:	19.0
# # 90%:	33.0
# # choose top 10%, that is 33

# now output the list of targeted authors
for author, num in author2commitnum.items():
    if num >= 33:
        print(author)
