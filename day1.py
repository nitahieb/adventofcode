f = open("adv1input.txt","r")
#part 1
max_sum = 0
temp_sum = 0
for line in f:
    if line == "\n":
        if temp_sum > max_sum:
            max_sum = temp_sum
        temp_sum = 0
    else:
        temp_sum+=int(line)

print(max_sum)

#part 2
from sortedcontainers import SortedList
f = open("adv1input.txt","r")
sum_list = SortedList()
temp_sum = 0
for line in f:
    if line == "\n":
        sum_list.add(temp_sum)     
        temp_sum = 0
    else:
        temp_sum+=int(line)
print(sum_list.pop()+sum_list.pop()+sum_list.pop())