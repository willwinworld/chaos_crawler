import functools

sorted_ignore_case = functools.partial(sorted, cmp = lambda x, y:cmp(x.lower(), y.lower()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])