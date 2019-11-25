import sys
from collections import defaultdict
import json

author2pkgs = defaultdict(set)

for line in sys.stdin:
    items = line.strip().split(';')
    author = items[4]
    pkgs = items[0]
    author2pkgs[author].update(set(pkgs.split(',')))

# dump result for statistics
for author, pkgs in author2pkgs.items():
    print(author+';'+str(len(pkgs))+';'+','.join(sorted(list(pkgs))))
# now learn statistics through shell commands
# 1. cat result | cut -d\; -f1 | sort -u | wc
# 2. cat result | cut -d\; -f2 | sort | uniq -c
# 3. cat result | cut -d\; -f3 | grep react, vue, angular, ember | wc
# 4. cat result | cut -d\; -f3 | sort | uniq -c
