f = open("input2.txt","r")

rpsdict = {
  "X": 1,
  "Y": 2,
  "Z": 3,
  "A": 1,
  "B": 2,
  "C": 3
}
def rps(opp,you):
    score = rpsdict[you]
    if rpsdict[you] == rpsdict[opp]:
        score += 3
    if opp == "A" and you == "Y":
        score += 6
    if opp == "B" and you == "Z":
        score +=6
    if opp == "C" and you == "X":
        score += 6
    return score
totalscore = 0
for line in f:
    totalscore += rps(line[0],line[2])
print(totalscore)

#Part 2

windict = {
  "A": 2,
  "B": 3,
  "C": 1
}
losedict = {
  "A": 3,
  "B": 1,
  "C": 2
}
f = open("input2.txt","r")
totalscore=0
for line in f:
    if line[2] == "X":
        totalscore += losedict[line[0]]
    if line[2] == "Y":
        totalscore += rpsdict[line[0]] + 3
    if line[2] == "Z":
         totalscore += windict[line[0]] + 6

print(totalscore)