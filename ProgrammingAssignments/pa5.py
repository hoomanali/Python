# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 5 - Phylogenetics

# Enter 3 strings, A, B, and C
seqA = input("Enter sequence A: ")
seqB = input("Enter sequence B: ")
seqC = input("Enter sequence C: ")

# Convert strings to upper
seqA = seqA.upper()
seqB = seqB.upper()
seqC = seqC.upper()

# If preconditions not met, print error and quit()
# Check pre1: All sequences are of same length
if len(seqA) != len(seqB):
    print("Sequence A and B not of same length, exiting.")
    quit()
elif len(seqA) != len(seqC):
    print("Sequence A and C not of same length, exiting.")
    quit()
elif len(seqB) != len(seqC):
    print("Sequence B and C not of same length, exiting.")
    quit()

size = len(seqA)

# Check pre2: No chars other than A, C, G, T
if any(c not in "ACGT" for c in seqA):
    print("Sequence A has invalid characters, exiting.")
    quit()
if any(c not in "ACGT" for c in seqB):
    print("Sequence B has invalid characters, exiting.")
    quit()
if any(c not in "ACGT" for c in seqC):
    print("Sequence C has invalid characters, exiting.")
    quit()

# Compute genetic distance (number of differing chars)
# A vs B
distanceAB = 0
for i in range(0, size):
    if seqA[i] != seqB[i]:
        distanceAB += 1

# A vs C
distanceAC = 0
for i in range(0, size):
    if seqA[i] != seqC[i]:
        distanceAC += 1

# B vs C
distanceBC = 0
for i in range(0, size):
    if seqB[i] != seqC[i]:
        distanceBC += 1

# Print pair with most recent common ancestor
# Pair with shortest distance
if distanceAB < distanceAC and distanceAB < distanceBC:
    print("A and B have the most recent common ancestor.")
if distanceAC < distanceAB and distanceAC < distanceBC:
    print("A and C have the most recent common ancestor.")
if distanceBC < distanceAB and distanceBC < distanceAC:
    print("B and C have the most recent common ancestor.")
