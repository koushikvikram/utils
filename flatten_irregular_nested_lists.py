# https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
from collections.abc import Iterable

input_list = [[[1, 2, 3], [4, 5]], 6]
expected_output = [1,2,3,4,5,6]

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

output = flatten(input_list)

print(list(output))            



