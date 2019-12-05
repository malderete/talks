import collections
"""
collections
    Counter
"""
counter = {}
for person in persons:
    name = person.name
    counter.setdefault(name, 0)
    counter[name] += 1


counter = collections.Counter()
for person in persons:
    name = person.name
    counter[name] += 1


"""
collections
    namedtuple
"""


"""
functools
    lru_cache
"""


"""
itertools
    chain
    takewhile
    dropwhile
    zip_longest
"""


"""
concurrent.futures
"""


"""
sched
"""


"""
contextlib
"""


"""
dataclass
"""


"""
requests
"""

"""
pandas
"""

"""
attrs
"""

