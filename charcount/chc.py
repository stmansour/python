import sys

# file1 = open('out.txt','r')
# lines = file1.readlines()
# print("Lines: ", len(lines))

m = {} # dictionary of counts indexed by letter
for line in sys.stdin:
    for c in line:
        if ord(c) != 10:
            if c in m.keys():
                m[c] += 1
            else:
                m[c] = 1;

# initilize idx with an indexed array of keys to m
l = len(m.keys())
idx = []
i = 0
for k in m.keys():
    idx.append(k)

#-------------------------------------------
# Sort the counts largest to smallest...
#-------------------------------------------
for i in range(0,l-2):                  # idx[i] represents largest value from m[idx[i] through m[idx[l-2]]
    max = idx[i]                        # assume idx[i] points to largest val
    for j in range(i+1,l-1):            # [j] represents all values from m[idx[i+1]] through m[idx[l-1]]
        if ( m[idx[j]] > m[idx[i]]):    # larger value?
            idx[i] = idx[j]             # now idx[i] points to the largest value so far
            idx[j] = max                # swap these indeces
            max = idx[i]                # this is now the largest value so far

for i in idx:
    print(i,"-",m[i])
