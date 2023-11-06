import random
import os
# small
smallDataset = [random.randint(0, 100000) for i in range(1000)]
smallDatasetSorted = smallDataset.copy()
smallDatasetSorted.sort()
smallDatasetReversed = smallDatasetSorted.copy()
smallDatasetReversed.sort(reverse=True)
with open('dataset\smallRandom.txt', 'w') as f:
    for item in smallDataset:
        f.write("%s\n" % item)
with open('dataset\smallSorted.txt', 'w') as f:
    for item in smallDatasetSorted:
        f.write("%s\n" % item)

with open('dataset\smallReversed.txt', 'w') as f:
    for item in smallDatasetReversed:
        f.write("%s\n" % item)

# medium
mediumDataset = [random.randint(0, 100000) for i in range(10000)]
mediumDatasetSorted = mediumDataset.copy()
mediumDatasetSorted.sort()
mediumDatasetReversed = mediumDatasetSorted.copy()
mediumDatasetReversed.sort(reverse=True)

with open('dataset\mediumRandom.txt', 'w') as f:
    for item in mediumDataset:
        f.write("%s\n" % item)

with open('dataset\mediumSorted.txt', 'w') as f:
    for item in mediumDatasetSorted:
        f.write("%s\n" % item)

with open('dataset\mediumReversed.txt', 'w') as f:
    for item in mediumDatasetReversed:
        f.write("%s\n" % item)


# Large
largeDataset = [random.randint(0, 100000) for i in range(100000)]
largeDatasetSorted = largeDataset.copy()
largeDatasetSorted.sort()
largeDatasetReversed = largeDatasetSorted.copy()
largeDatasetReversed.sort(reverse=True)

with open('dataset\largeRandom.txt', 'w') as f:
    for item in largeDataset:
        f.write("%s\n" % item)

with open('dataset\largeSorted.txt', 'w') as f:
    for item in largeDatasetSorted:
        f.write("%s\n" % item)

with open('dataset\largeReversed.txt', 'w') as f:
    for item in largeDatasetReversed:
        f.write("%s\n" % item)