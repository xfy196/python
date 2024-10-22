# from copy import deepcopy

# l = [1,2,3]
# _l = l.copy()
# _l[0] = -1
# print(_l)
# print(l)
from copy import deepcopy
l = [[1],[2],3]
_l = deepcopy(l)
_l[0][0] = -1
print(_l)
print(l)