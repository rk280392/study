from iteration_utilities import deepflatten

def flatten(l):
    return[item for sublist in l for item in sublist]

l = [[1,2,3],[3]]

print(flatten(l))


# if you don't know how deep the list is nested
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]

print(list(deepflatten(l, depth=3)))
