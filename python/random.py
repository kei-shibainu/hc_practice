import random

def create_random_group(group):
    type = random.randint(2, 3)
    groupA = sorted(random.sample(group, type))
    groupB = sorted([name for name in group if name not in groupA])
    return (groupA, groupB)

names = ('A','B','C','D','E','F')
groupA, groupB = create_random_group(names)
print(groupA)
print(groupB)