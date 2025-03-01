counts = dict()
names = ['csev', 'cwen', 'jc', 'nh', 'nh', 'nh', 'jc', 'csev', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1 
print(counts)


counts2 = dict()
names2 = ['csev', 'cwen', 'jc', 'nh', 'nh', 'nh', 'jc', 'csev', 'cwen', 'JP']
for name in names2 :
    counts2[name] = counts.get(name, 0) + 1
print(counts2)