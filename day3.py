import string
f = open("input3.txt","r")
alphabet = string.ascii_lowercase + string.ascii_uppercase

alphabetdict = dict(zip(alphabet, range(1,53)))
total = 0
for line in f:
    firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]
    total += alphabetdict[list(set(firsthalf).intersection(secondhalf))[0]]

print(total)


f = iter(open("input3.txt","r"))

total = 0
for elf1,elf2,elf3 in zip(f,f,f):
    common = list(set(elf1).intersection(elf2).intersection(elf3))
    common.remove('\n')
    total +=alphabetdict[common[0]]

print(total)