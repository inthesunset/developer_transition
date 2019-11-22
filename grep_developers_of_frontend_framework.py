import sys
import re

key_frameworks = ['react', 'angular', 'ember', 'vue']
for line in sys.stdin:
    items = line.strip().split(';')
    used_framework = []
    for framework in key_frameworks:
        if re.search(r'\b'+framework+r'\b', '.'.join(items[5:]), flags=re.IGNORECASE):
            used_framework.append(framework)
    if used_framework:
        print(','.join(used_framework)+';'+line.strip())
