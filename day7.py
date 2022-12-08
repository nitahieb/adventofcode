lines = open("input7.txt","r")

directories = dict()
        
def recfun(directory,total): 
    line = lines.readline()
    if not line:
        return total
    if line[0:4] == "$ cd":
        if line[5:] == "..\n":          
            return total
        else:
            newdirectory = directory + (f"/{line[5:]}".strip(),)           
            directories[newdirectory] = recfun(newdirectory,0)
            if directory not in directories:
                directories[directory] = 0
            total +=directories[newdirectory]
            directories[directory] +=  total
    if line[0] != "$" and line[0] !="d":
        total += int(line.split(" ")[0])
    return recfun(directory,total)


biggest = recfun((),0)
print(sum([x for x in directories.values() if x <= 100000]))
print(min([x for x in directories.values() if x >= 30000000-(70000000-biggest)]))
