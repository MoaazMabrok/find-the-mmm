from collections import Counter
numb = [3,4,2,2,2,2,2,1,0,0,0]
no = len(numb)
val = Counter(numb)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]
if len(mode) == no:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
print(findMode)

no = len(numb)
summ = sum(numb)
mean = summ / no
print("The mean of all these numbers (", numb, ") is", str(mean))

no = len(numb)
numb.sort()
if no % 2 == 0:
    median1 = numb[no//2]
    median2 = numb[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = numb[no//2]
print("The median of the given numbers  (", numb, ") is", str(median))