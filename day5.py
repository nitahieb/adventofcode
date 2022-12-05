f = open("input5.txt","r")

inp = ["TRGWQMFP","RFH","DSHGVRZP","GWFBPHQ","HJMSP","LPRSHTZM","LMNHTP","RQDF","HPLNCSD"]
for line in f:
    if line[0:4]!="move":
        continue
    listline = line.split(" ")
    amount = int(listline[1])
    frombox = int(listline[3])
    tobox = int(listline[5])
    inp[tobox-1] = inp[frombox-1][0:amount][::-1] + inp[tobox-1]
    inp[frombox-1] = inp[frombox-1][amount:]


print(inp)

#part 2 
f = open("input5.txt","r")

inp = ["TRGWQMFP","RFH","DSHGVRZP","GWFBPHQ","HJMSP","LPRSHTZM","LMNHTP","RQDF","HPLNCSD"]
for line in f:
    if line[0:4]!="move":
        continue
    listline = line.split(" ")
    amount = int(listline[1])
    frombox = int(listline[3])
    tobox = int(listline[5])
    inp[tobox-1] = inp[frombox-1][0:amount] + inp[tobox-1]
    inp[frombox-1] = inp[frombox-1][amount:]


print(inp)