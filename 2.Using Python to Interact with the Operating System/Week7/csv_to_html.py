
#!/usr/bin/env python3
# regexr.com
# print(sorted(names))

import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)


fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
import operator
sorted(fruit.items(), key=operator.itemgetter(0))
sorted(fruit.items(), key=operator.itemgetter(1))