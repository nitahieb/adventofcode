f = open("input4.txt","r")
total = 0
for line in f:
    sections = line.split(",")
    firstSection = sections[0].split("-")
    secondSection = sections[1].split("-")
    rangefirst = set(range(int(firstSection[0]),int(firstSection[1])+1))
    rangesecond = set(range(int(secondSection[0]),int(secondSection[1])+1))
    intersect = rangefirst.intersection(rangesecond)
    if intersect == rangefirst or intersect == rangesecond:
        total+=1

print(total)

#part 2 

f = open("input4.txt","r")
total = 0
for line in f:
    sections = line.split(",")
    firstSection = sections[0].split("-")
    secondSection = sections[1].split("-")
    rangefirst = set(range(int(firstSection[0]),int(firstSection[1])+1))
    rangesecond = set(range(int(secondSection[0]),int(secondSection[1])+1))
    intersect = rangefirst.intersection(rangesecond)
    if intersect:
        total+=1

print(total)