# import os

# with open('cc', 'r') as f:
#     cc = f.readlines()
# with open('all', 'r') as f:
#     all = f.readlines()
# counter = 0
# for c in cc:
#     if counter < 8000:
#         if c not in all:
#             counter += 1
#             with open('false', 'a') as f:
#                 f.write(c)
#     else:
#         break
import random


with open('true', 'r') as f:
    tt = f.readlines()

random.shuffle(tt)

with open('false', 'r') as f:
    ff = f.readlines()

random.shuffle(ff)

for t in tt[0:2000]:
    with open('test', 'a') as f:
        f.write(t.rstrip() + ": true\n")

for t in ff[0:2000]:
    with open('test', 'a') as f:
        f.write(t.rstrip() + ": false\n")

for t in tt[2000:]:
    with open('train', 'a') as f:
        f.write(t.rstrip() + ": true\n")

for t in ff[2000:]:
    with open('train', 'a') as f:
        f.write(t.rstrip() + ": false\n")