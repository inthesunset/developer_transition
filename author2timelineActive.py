import sys
from collections import defaultdict
import bisect

authorListFile = sys.argv[1]
authorSet = set()
with open(authorListFile, 'r') as f:
    for line in f:
        authorSet.add(line.strip())

# read from 4frameworks.c2PtabPKG.{0..31}, which is sorted by commit hash.
# there are cases where both frameworks are used in single commit.

# Let's aggregate frameworks on commit
# author2timeline = defaultdict(dict)
# here, others stand for (time, frameworks)
author2commit2others = defaultdict(dict)
for line in sys.stdin:
    items = line.strip().split(';')
    author = items[4]
    if author in authorSet:
        frameworks = items[0].split(',')
        time = items[3]
        commit = items[1]
        if commit not in author2commit2others[author]:
            author2commit2others[author][commit] = time+','+','.join(frameworks)
        else:
            current = author2commit2others[author][commit]
            current_frameworks = current.split(',')[1:]
            author2commit2others[author][commit] = time + ',' + ','.join(list(set(current_frameworks + frameworks)))

# if you want clean author,commit,time,frameworks, please dump author2commit2others

#re-arrange author2commit2others to author2timeline
author2timeline = defaultdict(dict)
# list contains of tuples (time, 0/1/n, 0/1/n, sum), basically, the time, the number of commits that affteced 'react'
# affected 'angular', the total number of commits at a givem time
for author, commits in author2commit2others.items():
    for commit, others in commits.items():
        items = others.split(',')
        time = items[0]
        # hard code here: react, angular
        react = 0
        angular = 0
        frameworks = items[1:]
        if 'react' in frameworks:
            react = 1
        if 'angular' in frameworks:
            angular = 1
        # end hard code here
        if time not in author2timeline[author]:
            author2timeline[author][time] = [react, angular, 1]
        else:
            currentValue = author2timeline[author][time]
            currentValue[0] += react
            currentValue[1] += angular
            currentValue[2] += 1

# dump author2timeline in time order per developer
# output format author, time, react, angular, commits
# print a head here:
print('author id; time (sorted); react commit #; angular commit #; total releant commits #')
for author, timelines in author2timeline.items():
    for timepoint in sorted(timelines.keys()):
        print(author + ';' + timepoint + ';' + ','.join(author2timeline[author][timepoint]))
