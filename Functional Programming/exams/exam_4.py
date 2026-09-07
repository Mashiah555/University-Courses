# מבחן תשפה מועד ב
from functools import reduce


def height(tree):
    if not tree:
        return -1
    return 1 + max(height(tree[1]), height(tree[2]))

def add(tree, key):
    if not tree:
        return [key, [], []]

    if key < tree[0]:
        return [tree[0], add(tree[1], key), tree[2]]
    return [tree[0], tree[1], add(tree[2], key)]

def buildTree(keys):
    return reduce(add, keys, [])

def searchPath(tree, key):
    if not tree:
        return []
    if key == tree[0]:
        return [tree[0]]
    if key < tree[0]:
        return [tree[0]] + searchPath(tree[1], key)
    return [tree[0]] + searchPath(tree[2], key)


keys = [10,5,3,7,20,15,17,25]
tr = buildTree(keys)

print(tr)
print(height(tr))
print(searchPath(tr, 17))
print(searchPath(tr, 4))