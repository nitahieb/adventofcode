f = open("input6.txt","r").read()

last4 = []
for i in range(len(f)):
    if len(last4)<4:
        last4.append(f[i])
        continue
    if len(set(last4)) == 4:
        print(i)
        break
    last4.pop(0)
    last4.append(f[i])

#part 2
f = open("input6.txt","r").read()

last14 = []
for i in range(len(f)):
    if len(last14)<14:
        last14.append(f[i])
        continue
    if len(set(last14)) == 14:
        print(i)
        break
    last14.pop(0)
    last14.append(f[i])


