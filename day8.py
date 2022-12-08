f = open("input8.txt","r")

text = [line.strip() for line in f.readlines()]

def checkvisible(val,coords,text):
    if coords[1] == 0 or coords[1] == len(text)-1 or coords[0] == 0 or coords[0] == len(text[0])-1:
        return True
    covered = [False,False,False,False]
    for i in range(0,coords[0]):
        if int(text[coords[1]][i]) >= val:
            covered[0] = True
            break
    for i in range(coords[0]+1,len(text[0])):
        if int(text[coords[1]][i]) >= val:
            covered[1] = True
            break
    for i in range(0,coords[1]):
        if int(text[i][coords[0]]) >= val:
            covered[2] = True
            break
    for i in range(coords[1]+1,len(text)):
        if int(text[i][coords[0]]) >= val:
            covered[3] = True
            break
    return False in covered
        
sum = 0
for y in range(len(text)):
    for x in range(len(text[y])):
        sum += checkvisible(int(text[y][x]),(x,y),text)
print(sum)

#part 2

f = open("input8.txt","r")

text = [line.strip() for line in f.readlines()]

def mostview(val,coords,text):
    covered = [0,0,0,0]
    for i in reversed(range(0,coords[0])):
        covered[0] += 1
        if int(text[coords[1]][i]) >= val:
            break
    for i in range(coords[0]+1,len(text[0])):
        covered[1] += 1
        if int(text[coords[1]][i]) >= val:
            break
    for i in reversed(range(0,coords[1])):
        covered[2] += 1
        if int(text[i][coords[0]]) >= val:
            break
    for i in range(coords[1]+1,len(text)):
        covered[3] += 1
        if int(text[i][coords[0]]) >= val:
            break
    return covered[0]*covered[1]*covered[2]*covered[3]
        
highest = 0
for y in range(len(text)):
    for x in range(len(text[y])):
        temphighest = mostview(int(text[y][x]),(x,y),text)
        if highest < temphighest:
            highest=temphighest
        
        
print(highest)